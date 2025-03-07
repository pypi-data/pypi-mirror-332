import pytest
import time
import numpy as np
from topovelo.model.model_util import (
    knnx0_index,
    knnx0_index_parallel,
    init_params,
    init_params_parallel,
    reinit_params,
    reinit_params_parallel
)
import matplotlib.pyplot as plt

def test_knnx0_runtime():
    # Example input data and expected outputs
    tmax = 20
    run_time = [[], []]
    num_list = np.power(10, np.arange(2, 5.5, 0.5)).astype(int)
    dt = (0.03*tmax, 0.06*tmax)
    k = 30
    radius = 0.05
    # Used to eliminate overhead from parallelization
    t = np.random.rand(100) * tmax
    z = np.random.normal(size=(100, 5))
    xy = np.random.rand(100, 2)
    t_query = np.random.rand(50) * tmax
    z_query = np.random.normal(size=(50, 5))
    xy_query = np.random.rand(50, 2)
    result_2 = knnx0_index_parallel(
        t, z, xy, t_query, z_query, xy_query, dt, k, radius, hist_eq=True
    )
    for n in num_list:
        n_query = n//2
        t = np.random.rand(n) * tmax
        z = np.random.normal(size=(n, 5))
        xy = np.random.rand(n, 2)
        t_query = np.random.rand(n_query) * tmax
        z_query = np.random.normal(size=(n_query, 5))
        xy_query = np.random.rand(n_query, 2)
        
        # Call the function
        t0 = time.time()
        result = knnx0_index(
            t, z, xy, t_query, z_query, xy_query, dt, k, radius, hist_eq=True, verbose=False
        )
        run_time[0].append(time.time()-t0)
        t0 = time.time()
        result_2 = knnx0_index_parallel(
            t, z, xy, t_query, z_query, xy_query, dt, k, radius, hist_eq=True
        )
        run_time[1].append(time.time()-t0)

        assert len(result) == len(result_2), f"Length of results do not match ({len(result)} != {len(result_2)})"
        for i in range(len(result)):
            assert np.all(result[i] == result_2[i]), f"Results do not match at index {i}"
    
    fig, ax = plt.subplots()
    ax.plot(num_list, run_time[0], label='Uni-Core')
    ax.plot(num_list, run_time[1], label='Multi-Core')
    ax.set_xlabel('Number of points')
    ax.set_ylabel('Runtime (s)')
    ax.grid()
    ax.legend()
    plt.tight_layout()
    plt.savefig('test_knnx0_runtime.png')


def test_init_params():
    print(__name__)
    n_cell = 100000
    percent = 95
    min_sigma_u = 0.1
    min_sigma_s = 0.1
    num_list = np.power(10, np.arange(2, 3.5, 0.5)).astype(int)
    run_time = [[], []]
    for n_gene in num_list:
        u = np.random.rand(n_cell, n_gene)
        s = np.random.rand(n_cell, n_gene)
        t0 = time.time()
        params = init_params(
            u, s, percent, min_sigma_u=min_sigma_u, min_sigma_s=min_sigma_s
        )
        run_time[0].append(time.time()-t0)
        t0 = time.time()
        params_2 = init_params_parallel(
            u, s, percent, min_sigma_u=min_sigma_u, min_sigma_s=min_sigma_s
        )
        run_time[1].append(time.time()-t0)
        for param, param_2 in zip(params, params_2):
            assert np.all(param == param_2), "Results do not match"
    fig, ax = plt.subplots()
    ax.plot(num_list, run_time[0], label='Uni-Core')
    ax.plot(num_list, run_time[1], label='Multi-Core')
    ax.legend()
    ax.set_xlabel('Number of genes')
    ax.set_ylabel('Runtime (s)')
    ax.grid()
    plt.tight_layout()
    plt.savefig('test_init_params.png')


def test_reinit_params():
    print(__name__)
    n_cell = 100000
    tmax = 20
    num_list = np.power(10, np.arange(2, 3.5, 0.5)).astype(int)
    run_time = [[], []]
    for n_gene in num_list:
        u = np.random.rand(n_cell, n_gene)
        s = np.random.rand(n_cell, n_gene)
        t = np.random.rand(n_cell) * tmax
        ton = np.random.rand(n_gene) * tmax * 0.5
        t0 = time.time()
        params = reinit_params(
            u, s, t, ton
        )
        run_time[0].append(time.time()-t0)
        t0 = time.time()
        params_2 = reinit_params_parallel(
            u, s, t, ton
        )
        run_time[1].append(time.time()-t0)
        for param, param_2 in zip(params, params_2):
            assert np.all(param == param_2), "Results do not match"
    fig, ax = plt.subplots()
    ax.plot(num_list, run_time[0], label='Uni-Core')
    ax.plot(num_list, run_time[1], label='Multi-Core')
    ax.legend()
    ax.set_xlabel('Number of genes')
    ax.set_ylabel('Runtime (s)')
    ax.grid()
    plt.tight_layout()
    plt.savefig('test_reinit_params.png')


# Setup additional test functions to cover different scenarios, invalid inputs, etc.
if __name__ == "__main__":
    # pytest.main()
    test_knnx0_runtime()
    #test_init_params()
    #test_reinit_params()