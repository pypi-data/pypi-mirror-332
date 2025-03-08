import numpy as np
import jax
jax.config.update("jax_enable_x64", True)
from flax import nnx

import jax.numpy as jnp
from jax import random as jrnd

import random
import math

from functools import partial
from tqdm import tqdm
import time

from jax_tqdm import scan_tqdm

import matplotlib.tri as tri
import matplotlib.pyplot as plt


class SensX():

    def __init__(self\
                , model\
                , QOI \
                , global_fmin\
                , global_fmax\
                , q_min=0\
                , q_max=1\
                ):

        self.qoi = partial(QOI, model=model)

        self.features_reshape = global_fmin.shape
        self.n_f = np.prod(self.features_reshape)

        self.q_min = q_min
        self.q_max = q_max
        self.q_range = q_max - q_min

        self.fmin = global_fmin.flatten()
        self.fmax = global_fmax.flatten()
        self.frange = self.fmax - self.fmin




    # xx is single input
    def get_OAT_perts(self\
                , xx\
                , delta_arr=None\
                ):

        features_reshape = xx.shape()

        if delta_arr is None:
            delta_arr = np.linspace(0.2, 1, num=50)

        xx = xx.flatten()

        n_f = len(xx)

        k = len(delta_arr)
        
        X = np.tile(xx, (k, 1))
        
        # Creating perts OAT
        
        P_low = np.zeros((k, n_f))
        P_high = np.zeros((k, n_f))
        
        for f_idx in range(n_f):
            
            this_low = xx[f_idx] - delta_arr * self.frange[f_idx]
            this_high = xx[f_idx] + delta_arr * self.frange[f_idx]
        
            this_low = np.maximum(this_low, self.fmin[f_idx])
            this_high = np.minimum(this_high, self.fmax[f_idx])
        
            P_low[:, f_idx] = this_low
            P_high[:, f_idx] = this_high
        
        
        # Computing OAT
        
        def OAT(carry, f_idx, X, qoi):
        
            P = carry
        
            X = X.at[:, f_idx].set(P[:, f_idx])
        
            return P, qoi(X)
        
        
        X = jnp.array(X)
        P_low = jnp.array(P_low)
        P_high = jnp.array(P_high)
        
        OAT_wrapper = partial(OAT, X=X, qoi=self.qoi)
        
        _, OAT_low_res = jax.lax.scan(OAT_wrapper, P_low, xs=jnp.arange(n_f))
        
        _, OAT_high_res = jax.lax.scan(OAT_wrapper, P_high, xs=jnp.arange(n_f))

        return delta_arr, OAT_low_res, OAT_high_res


    # xx is single input
    def get_AST_perts(self\
                , xx\
                , delta_arr=None\
                ):

        features_reshape = xx.shape()

        if delta_arr is None:
            delta_arr = np.linspace(0.02, 1, num=50)

        xx = xx.flatten()

        n_f = len(xx)

        nn = 100

        kk = len(delta_arr)
        
        key = jrnd.key(random.randint(0,10000))

        keys = jrnd.split(key, num=kk)
        
        def single_delta(xs, xx, fmin, fmax, frange, qoi):
        
            d, key = xs
        
            low = jnp.maximum(xx - d*frange, fmin)
            high = jnp.minimum(xx + d*frange, fmax)
        
            PP = jrnd.uniform(key, shape=(nn, n_f), minval=low, maxval=high)
        
            return None, qoi(PP)
        
        wrapper = partial(single_delta, xx=xx, fmin=self.fmin, fmax=self.fmax, frange=self.frange, qoi=self.qoi)
        
        _, sample_perts_QOI = jax.lax.scan(wrapper, None, xs=(delta_arr,keys))
        
        
        return delta_arr, sample_perts_QOI


    def get_local_hypercubes(self, xx_flat, delta_star):

        if isinstance(delta_star, float):

            all_low_hypercube = xx_flat - (delta_star * self.frange)
            all_high_hypercube = xx_flat + (delta_star * self.frange)

        else:

            all_low_hypercube = np.zeros_like(xx_flat)
            all_high_hypercube = np.zeros_like(xx_flat)

            for sample_idx in range(xx_flat.shape[0]):

                all_low_hypercube[sample_idx] = xx_flat[sample_idx] - (delta_star[sample_idx] * self.frange)
                all_high_hypercube[sample_idx] = xx_flat[sample_idx] + (delta_star[sample_idx] * self.frange)


        for sample_idx in range(xx_flat.shape[0]):

            all_low_hypercube[sample_idx] = np.maximum(all_low_hypercube[sample_idx], self.fmin)
            all_high_hypercube[sample_idx] = np.minimum(all_high_hypercube[sample_idx], self.fmax)

        return all_low_hypercube, all_high_hypercube


    def get_perturbed_qoi_all_info(self\
                            , xx\
                            , nn_global=1000\
                            , delta_arr=None\
                         ):


        n_s = xx.shape[0]

        batch_size = n_s
        
        n_f = self.n_f
        features_reshape = self.features_reshape

        if delta_arr is None:
            delta_arr = np.linspace(0.02, 1, num=50)

        kk = len(delta_arr)

        xx_flat = np.reshape(xx, (n_s, n_f))

        non_zero_ranges = np.argwhere(self.frange != 0).flatten()

        nz_f = len(non_zero_ranges)

        def qoi_batch(batch, features_reshape):

            batch = jnp.reshape(batch, (batch.shape[0], *features_reshape))

            return self.qoi(batch)

        qoi_batch_wrapper = nnx.jit(partial(qoi_batch, features_reshape=features_reshape))


        # Setting up global perts
        
        key = jrnd.key(random.randint(0,10000))
        
        keys = jrnd.split(key, num=kk)

        sample_perts_qoi = jnp.zeros((kk, nn_global))

        all_qoi = jnp.zeros((n_s, kk, nn_global))

        def single_sample_step1(carry, xs, sample_perts_qoi, fmin, fmax, frange):

            all_qoi  = carry

            s_idx, sample = xs

            #@scan_tqdm(kk, print_rate=10)
            def single_delta(carry, xs):

                sample_perts_qoi = carry

                d_idx, d, key = xs

                low = jnp.maximum(sample - d*frange, fmin)
                high = jnp.minimum(sample + d*frange, fmax)
                
                PP = jrnd.uniform(key, shape=(nn_global, n_f), minval=low, maxval=high)

                sample_perts_qoi = sample_perts_qoi.at[d_idx].set(qoi_batch_wrapper(PP))
    
                return sample_perts_qoi, None

            sample_perts_qoi, _ =\
                    jax.lax.scan(single_delta, sample_perts_qoi, (jnp.arange(kk), delta_arr, keys))
            
            all_qoi = all_qoi.at[s_idx].set(sample_perts_qoi)

            return all_qoi, None


        single_sample_step1_wrapper = partial(single_sample_step1\
                                        , sample_perts_qoi=sample_perts_qoi\
                                        , fmin=self.fmin\
                                        , fmax=self.fmax\
                                        , frange=self.frange)

        all_qoi, _ =\
                jax.lax.scan(single_sample_step1_wrapper, all_qoi, (jnp.arange(n_s), xx_flat))

        all_qoi = np.array(all_qoi)

        return all_qoi, delta_arr



    # ASSUMING all_qoi IS BATCH OF INPUTS
    def get_delta_star(self, all_qoi, delta_arr, tau_r=0.1, tau_a=0.1):

        thresh_rel = tau_r*self.q_range
        thresh_abs = tau_a*self.q_range

        all_median = np.median(all_qoi, axis=-1)

        step_sizes = np.ediff1d(delta_arr)

        n_s  = all_median.shape[0]
        
        delta_star_arr = np.zeros(n_s)
        
        for ss in range(n_s):
        
            n_d = all_median.shape[1] - 1
        
            this_med = all_median[ss]
        
            maxx = this_med[n_d]
            minn = this_med[n_d]
        
            while n_d > 1:
        
                grad = abs((this_med[n_d] - this_med[n_d-1])/step_sizes[n_d-1])
        
                maxx = max(maxx, this_med[n_d-1])
                minn = min(minn, this_med[n_d-1])
        
                abs_diff = maxx - minn
        
                if grad > thresh_rel or abs_diff > thresh_abs:
                    break
        
                n_d = n_d - 1
        
            delta_star_arr[ss] = delta_arr[n_d]
        
        
        return delta_star_arr

        

    # xx has to be a batch
    # to pass single input, use expand_dims axis = 0
    def sensi_batch_inputs(self\
                            , xx\
                            , delta_star=1.0\
                            , nw=100\
                            ):

        assert np.amax(delta_star) <= 1
        assert np.amin(delta_star) >= 0

        n_s = xx.shape[0]

        batch_size = n_s
        
        n_f = self.n_f
        features_reshape = self.features_reshape

        xx_flat = np.reshape(xx, (n_s, n_f))

        non_zero_ranges = np.argwhere(self.frange != 0).flatten()

        nz_f = len(non_zero_ranges)

        def qoi_batch(batch, features_reshape):

            batch = jnp.reshape(batch, (batch.shape[0], *features_reshape))

            return self.qoi(batch)

        qoi_batch_wrapper = nnx.jit(partial(qoi_batch, features_reshape=features_reshape))


        ################################
        # STUPID WAY FIRST
        all_low_hypercube, all_high_hypercube = self.get_local_hypercubes(xx_flat, delta_star)
        ################################


        ##----------------------
        ## Sensitivity computation
        ##----------------------

        #tic = time.time()

        init_QOI = self.qoi(xx)

        key = jrnd.key(random.randint(0,10000))
        
        keys = jrnd.split(key, num=nw)

        # GENERATE RANDOM WALKS
        all_walks = np.zeros((nw, nz_f), dtype=int)
        for w_idx in range(nw):
            all_walks[w_idx] = np.random.permutation(non_zero_ranges)



        sensi = jnp.zeros((n_s, n_f))

        XX = jnp.array(xx_flat)

        all_low_hypercube_jnp = jnp.array(all_low_hypercube)
        all_high_hypercube_jnp = jnp.array(all_high_hypercube)


        def single_walk(sensi, xs, XX, init_QOI, all_low_hypercube_jnp, all_high_hypercube_jnp):

            key, walk = xs

            end_points = jrnd.uniform(key=key, shape=(n_s, n_f)\
                                            , minval=all_low_hypercube_jnp\
                                            , maxval=all_high_hypercube_jnp)

            #@scan_tqdm(nz_f, print_rate=10000)
            def single_step(carry, xs):

                s_idx = xs

                f_idx = walk[s_idx]

                #f_idx = xs

                sensi, XX, prev_QOI = carry

                delta = end_points[:, f_idx] - XX[:, f_idx]

                XX = XX.at[:,f_idx].set(end_points[:,f_idx])

                this_QOI = qoi_batch_wrapper(XX)

                this_sensi = jnp.abs((this_QOI - prev_QOI)/delta)

                sensi = sensi.at[:, f_idx].add(this_sensi)

                return (sensi, XX, this_QOI), None


            (sensi, _, _), _ = jax.lax.scan(single_step\
                                            , (sensi, XX, init_QOI)\
                                            , jnp.arange(nz_f))
                                            #, walk)

            return sensi, None



        single_walk_wrapper = partial(single_walk\
                                        , XX=XX\
                                        , init_QOI=init_QOI\
                                        , all_low_hypercube_jnp=all_low_hypercube_jnp\
                                        , all_high_hypercube_jnp=all_high_hypercube_jnp)


        sensi, _ = jax.lax.scan(single_walk_wrapper, sensi, (keys, all_walks))


        #jax.block_until_ready(1)
        #toc = time.time()
        #print(f'sensi FINAL in {toc-tic} seconds')

        return np.reshape(sensi, (n_s, *features_reshape)) 



    # xx has to be a batch
    # to pass single input, use expand_dims axis = 0
    def sensi_batch_features(self\
                    , xx\
                    , delta_star=1.0\
                    , nw=100\
                    , batch_size=1000\
                    ):
    
        assert np.amax(delta_star) <= 1
        assert np.amin(delta_star) >= 0

        n_s = xx.shape[0]
        
        n_f = self.n_f
        features_reshape = self.features_reshape

        xx_flat = np.reshape(xx, (n_s, n_f))

        batch_size = min(n_f, batch_size)
    
        self.frange = self.fmax - self.fmin
    
        non_zero_ranges = np.argwhere(self.frange != 0).flatten()

        def qoi_batch(batch, features_reshape):

            batch = jnp.reshape(batch, (batch.shape[0], *features_reshape))

            return self.qoi(batch)

        qoi_batch_wrapper = nnx.jit(partial(qoi_batch, features_reshape=features_reshape))


        ##----------------------
        ## Sensitivity computation
        ##----------------------

        init_QOI = self.qoi(xx)

        key = jrnd.key(random.randint(0,10000))
        
        keys = jrnd.split(key, num=nw)

        nz_f = len(non_zero_ranges)

        BB = int(math.floor(nz_f/batch_size))
        LL = nz_f - BB*batch_size

        print(f'BB {BB} number of batches, LL {LL} steps in last batch.')

        batch_iter = jnp.arange(batch_size)

        loop_iter = jnp.arange(BB)


        batch = jnp.zeros((batch_size, n_f))

        # OPTION 1: pre-compute local hypercubes : will use more device memory as compared to OPTION 2
        # Get local hypercubes
        all_low_hypercube, all_high_hypercube = self.get_local_hypercubes(xx_flat, delta_star)

        ##############################################################
        # GENERATE RANDOM WALKS
        all_walks = np.zeros((nw, nz_f), dtype=int)
        for w_idx in range(nw):
            all_walks[w_idx] = np.random.permutation(non_zero_ranges)
        ##############################################################


        def single_sample_step2(sample\
                                , sample_QOI\
                                , end_points\
                                , all_walks\
                                , batch\
                                , BB\
                                , LL\
                                , batch_size\
                                , nw\
                                , n_f\
                                ):

            # 'step' should be initialized to sample
            def single_walk(carry, xs, step, sample_QOI, all_batch_results, BB, LL, batch_size):

                #sensi_record, batch = carry
                sensi_sum, batch = carry

                end_point, walk = xs

                delta = end_point - step

                # Create new batch of 'steps'
                def update_batch(carry, ptr):
                
                    step, batch, s_idx = carry
                
                    f_idx = walk[s_idx]
                
                    step = step.at[f_idx].set(end_point[f_idx])
                
                    batch = jax.lax.dynamic_update_index_in_dim(batch, step, ptr, axis=0)
                
                    return (step, batch, s_idx+1), None

                # Loop batches
                #@scan_tqdm(BB, print_rate=10)
                def loop(carry, xs):
    
                    step, batch, s_idx, all_batch_results = carry
    
                    # create batch
                    (step, batch, s_idx), _ =\
                            jax.lax.scan(update_batch, (step, batch, s_idx), jnp.arange(batch_size))
    
                    batch_out = qoi_batch_wrapper(batch)

                    all_batch_results = jax.lax.dynamic_update_index_in_dim(all_batch_results, batch_out, xs, axis=0)
                    
                    return (step, batch, s_idx, all_batch_results), None


                (step, _, s_idx, all_batch_results), _ =\
                                    jax.lax.scan(loop, (step, batch, 0, all_batch_results), jnp.arange(BB))

                # Last batch of features
                (step, batch, s_idx), _ = jax.lax.scan(update_batch, (step, batch, s_idx), jnp.arange(LL))
                
                last_batch_out = qoi_batch_wrapper(batch)

                all_batch_results_flat = jnp.hstack([all_batch_results.flatten(), last_batch_out[:LL]])

                init_diff = all_batch_results_flat[0] - sample_QOI

                diff = jnp.ediff1d(all_batch_results_flat, to_begin=init_diff)

                sensi_sum = sensi_sum.at[walk].add(jnp.abs(diff/delta[walk]))

                return (sensi_sum, batch), None


            all_batch_results = jnp.zeros((BB, batch_size))

            single_walk_wrapper = partial(single_walk\
                                        , step=sample\
                                        , sample_QOI=sample_QOI\
                                        , all_batch_results=all_batch_results\
                                        , BB=BB\
                                        , LL=LL\
                                        , batch_size=batch_size\
                                        )

            sensi_sum = jnp.zeros(n_f)

            (sensi_sum, _), _ =\
                                jax.lax.scan(single_walk_wrapper\
                                            , (sensi_sum, batch)\
                                            , (end_points, all_walks)\
                                            )


            return sensi_sum

        all_walks = jnp.array(all_walks)

        single_sample_step2_wrapper = partial(single_sample_step2\
                                        , all_walks=all_walks\
                                        , batch=batch\
                                        , BB=BB\
                                        , LL=LL\
                                        , batch_size=batch_size\
                                        , nw=nw\
                                        , n_f=n_f\
                                        )

        all_samples_sensi = np.zeros((n_s, n_f))

        for sample_idx in range(n_s):

            sample = xx_flat[sample_idx]

            this_low_hypercube = all_low_hypercube[sample_idx]
            this_high_hypercube = all_high_hypercube[sample_idx]

            this_end_points = np.random.uniform(low=np.expand_dims(this_low_hypercube, axis=0)\
                                                , high=np.expand_dims(this_high_hypercube, axis=0)\
                                                , size = (nw, n_f))

            this_end_points_jnp = jnp.array(this_end_points)

            all_samples_sensi[sample_idx] =\
                    np.array(single_sample_step2_wrapper(sample, init_QOI[sample_idx], this_end_points_jnp))



        return np.reshape(all_samples_sensi, (n_s, *features_reshape))



    # sample has to be a single sample
    def compute_important_ranks_single_sample(self\
                                , sample\
                                , face_vals\
                                , delta_arr=None\
                                , topn_arr=None\
                                , nn_global=1000\
                                , qoi_thresh=0.5\
                                , acc_thresh=0.01
                                ):
    
        
        sample_flat = sample.flatten()
    
        face_vals_flat = face_vals.flatten()
    
        if delta_arr is None:
            delta_arr = jnp.linspace(0.02, 1, num=50)
    
    
        if topn_arr is None:
    
            topn_arr = []
    
            topn = 1
    
            while topn < self.n_f:
                topn_arr.append(topn)
                topn = math.ceil(1.5*topn)
    
            if topn_arr[-1] != self.n_f:
                topn_arr.append(self.n_f)
    
            topn_arr = jnp.array(topn_arr)
    
    
        features_reshape = self.features_reshape
        def qoi_batch(batch, features_reshape):

            batch = jnp.reshape(batch, (batch.shape[0], *features_reshape))

            return self.qoi(batch)
    
        qoi_batch_wrapper = nnx.jit(partial(qoi_batch, features_reshape=features_reshape))
    
        sensi_order = np.argsort(-face_vals_flat)
    
        plt_delta = []
        plt_acc = []
        plt_topn = []
    
        for this_delta in delta_arr:
    
            print(f'Doing delta {this_delta}...')
    
            sample_low = sample_flat - this_delta * self.frange
            sample_high = sample_flat + this_delta * self.frange
    
            sample_low = np.maximum(sample_low, self.fmin)
            sample_high = np.minimum(sample_high, self.fmax)
    
            sample_range = sample_high - sample_low
    
            rnd_seed = random.randint(0,10000)
            key = jrnd.key(rnd_seed)
    
            flag = 0
    
            for topn in tqdm(topn_arr):
    
                static_features = sensi_order[topn:]
                
                this_low = sample_low.copy()
                this_high = sample_high.copy()
                
                this_low[static_features] = sample_flat[static_features]
                this_high[static_features] = sample_flat[static_features]
                
                pert_XX = jax.random.uniform(key=key, minval=this_low, maxval=this_high\
                                            , shape=(nn_global, self.n_f))
                
                pert_QOI = qoi_batch_wrapper(pert_XX)
    
                acc = np.sum(pert_QOI > qoi_thresh)/nn_global
    
                if acc < acc_thresh:
                    flag = 1
                    break
    
            if flag:
                plt_delta.append(this_delta)
                plt_acc.append(acc)
                plt_topn.append(topn)
    
    
        pareto_optimal_delta, pareto_optimal_topn = self.get_pareto_optimal(plt_delta, plt_topn)
    
        return plt_delta, plt_topn, pareto_optimal_delta, pareto_optimal_topn
    
    
    def get_pareto_optimal(self, delta_arr, topn_arr):
    
        pareto = np.array(delta_arr)**2 + (np.log(np.array(topn_arr))/math.log(self.n_f))**2
    
        pareto_optimal_idx = np.argmin(pareto)
    
        pareto_optimal_delta = round(delta_arr[pareto_optimal_idx],6)
        pareto_optimal_topn = topn_arr[pareto_optimal_idx]
    
        return pareto_optimal_delta, pareto_optimal_topn


        

        
    def get_pareto_optimal_from_landscape(self, landscape_delta, landscape_topn, landscape_qoi):

        idxs = np.argwhere(plt_median_qoi <= 0.5)

        print(idxs)

        
    
        pareto = np.array(delta_arr)**2 + (np.log(np.array(topn_arr))/math.log(self.n_f))**2
    
        pareto_optimal_idx = np.argmin(pareto)
    
        pareto_optimal_delta = round(delta_arr[pareto_optimal_idx],6)
        pareto_optimal_topn = topn_arr[pareto_optimal_idx]
    
        return pareto_optimal_delta, pareto_optimal_topn





        

    def get_pareto_optimal_general(self, arr1, arr2\
                                       , arr1_max=1\
                                       , arr2_max=1\
                                       , arr1_scale=None\
                                       , arr2_scale=None):

        if arr1_scale=='log':
            arr1_rescale = np.log(np.array(arr1))/math.log(arr1_max)
        else:
            arr1_rescale = np.array(arr1)/arr1_max

        if arr2_scale=='log':
            arr2_rescale = np.log(np.array(arr2))/math.log(arr2_max)
        else:
            arr2_rescale = np.array(arr2)/arr2_max

        pareto = arr1_rescale**2 + arr2_rescale**2

        pareto_optimal_idx = np.argmin(pareto)

        return arr1[pareto_optimal_idx], arr2[pareto_optimal_idx]
        
        


    # sample has to be a single sample
    def compute_ranks_QOI_landscape(self\
                                , sample\
                                , face_vals\
                                , delta_arr=None\
                                , topn_arr=None\
                                , nn_global=1000\
                                , qoi_thresh=0.5\
                                , acc_thresh=0.01
                                ):
    
        
        sample_flat = sample.flatten()
    
        face_vals_flat = face_vals.flatten()
    
        if delta_arr is None:
            delta_arr = jnp.linspace(0.02, 1, num=50)
    
    
        if topn_arr is None:
    
            topn_arr = []
    
            topn = 1
    
            while topn < self.n_f:
                topn_arr.append(topn)
                topn = math.ceil(1.5*topn)
    
            if topn_arr[-1] != self.n_f:
                topn_arr.append(self.n_f)
    
            topn_arr = jnp.array(topn_arr)
    
    
        features_reshape = self.features_reshape
        def qoi_batch(batch, features_reshape):

            batch = jnp.reshape(batch, (batch.shape[0], *features_reshape))

            return self.qoi(batch)
    
        qoi_batch_wrapper = nnx.jit(partial(qoi_batch, features_reshape=features_reshape))
    
        sensi_order = np.argsort(-face_vals_flat)
    
        plt_delta = []
        plt_qoi = []
        plt_topn = []
    
        for this_delta in delta_arr:
    
            # print(f'Doing delta {this_delta}...')
    
            sample_low = sample_flat - this_delta * self.frange
            sample_high = sample_flat + this_delta * self.frange
    
            sample_low = np.maximum(sample_low, self.fmin)
            sample_high = np.minimum(sample_high, self.fmax)
    
            sample_range = sample_high - sample_low
    
            rnd_seed = random.randint(0,10000)
            key = jrnd.key(rnd_seed)
    
            for topn in topn_arr:
    
                static_features = sensi_order[topn:]
                
                this_low = sample_low.copy()
                this_high = sample_high.copy()
                
                this_low[static_features] = sample_flat[static_features]
                this_high[static_features] = sample_flat[static_features]
                
                pert_XX = jax.random.uniform(key=key, minval=this_low, maxval=this_high\
                                            , shape=(nn_global, self.n_f))
                
                pert_QOI = qoi_batch_wrapper(pert_XX)
    
                # acc = np.sum(pert_QOI > qoi_thresh)/nn_global
    
                plt_delta.append(this_delta)
                plt_qoi.append(pert_QOI)
                plt_topn.append(topn)
    
    
        return plt_delta, plt_topn, plt_qoi



        

    def plot_qoi_sensx_pert_landscape(self, plt_delta, plt_topn, plt_qoi, n_levels=10):

        plt_median_qoi = np.median(plt_qoi, axis=-1)

        
        # -----------------------
        # Interpolation on a grid
        # -----------------------
        # A contour plot of irregularly spaced data coordinates
        # via interpolation on a grid.
        
        ngridx = 100
        ngridy = 200
        
        n_features = np.amax(np.array(plt_topn))
        print(f'number features {n_features}')
                             
        # Create grid values first.
        xi = np.linspace(0, 1, ngridx)
        yi = np.linspace(1, n_features, ngridy)

        
        x = plt_delta
        y = plt_topn
        z = plt_median_qoi
        
        triang = tri.Triangulation(x, y)
        interpolator = tri.LinearTriInterpolator(triang, z)
        Xi, Yi = np.meshgrid(xi, yi)
        zi = interpolator(Xi, Yi)


        plt.contour(xi, yi, zi, levels=n_levels, linewidths=0.5, colors='k')
        
        # CS = plt.contour(xi, yi, zi, [0.5])
        # plt.clabel(CS, inline=True, fontsize=18)
        
        cntr1 = plt.contourf(xi, yi, zi, levels=n_levels, cmap="RdBu", alpha=0.8)
        
        # plt.yscale('log')
        cb = plt.colorbar()
        
        cb.set_label(label=f'median QOI',fontsize=18)
        
        plt.xlabel('perturbation factor', fontsize=14)
        plt.ylabel('topn SENSEX ranks perturbed', fontsize=14)
        
        plt.ylim([1, n_features])

        return plt




def get_qoi_sensx_pert_landscape(plt_delta\
                                  , plt_topn\
                                  , plt_qoi\
                                  , ngridx=100\
                                  , ngridy=100\
                                  , n_levels=10):

    plt_median_qoi = np.median(plt_qoi, axis=-1)
    
    # -----------------------
    # Interpolation on a grid
    # -----------------------
    # A contour plot of irregularly spaced data coordinates
    # via interpolation on a grid.
    
    ngridx = 100
    ngridy = 200
    
    n_features = np.amax(np.array(plt_topn))
                         
    # Create grid values first.
    xi = np.linspace(0, 1, ngridx)
    yi = np.linspace(1, n_features, ngridy)

    x = plt_delta
    y = plt_topn
    z = plt_median_qoi
    
    triang = tri.Triangulation(x, y)
    interpolator = tri.LinearTriInterpolator(triang, z)
    Xi, Yi = np.meshgrid(xi, yi)
    zi = interpolator(Xi, Yi)

    return Xi, Yi, zi


def get_pareto_optimal(xx, yy, n_f):

    delta_arr = np.array(xx)
    topn_arr = np.array(yy)

    pareto = np.array(delta_arr)**2 + (np.log(np.array(topn_arr))/math.log(n_f))**2

    pareto_optimal_idx = np.argmin(pareto)

    pareto_optimal_delta = round(delta_arr[pareto_optimal_idx],6)
    pareto_optimal_topn = topn_arr[pareto_optimal_idx]

    return pareto_optimal_delta, pareto_optimal_topn



