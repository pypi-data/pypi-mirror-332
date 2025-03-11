import numpy as np
import pytest
import xarray as xr

from haplo.internal.mcmc_output_analysis import slice_iteration_of_mcmc_output_xarray_dataset, \
    mcmc_output_xarray_dataset_to_pandas_data_frame


@pytest.fixture
def sample_dataset():
    number_of_iterations = 10
    number_of_cpus = 4
    number_of_chains = 2
    number_of_parameters = 3

    iterations = np.arange(number_of_iterations)
    cpus = np.arange(number_of_cpus)
    chains = np.arange(number_of_chains)
    parameters = np.arange(number_of_parameters)

    parameter_data = np.random.rand(number_of_iterations, number_of_cpus, number_of_chains, number_of_parameters)
    log_likelihood_data = np.random.rand(number_of_iterations, number_of_cpus, number_of_chains)

    dataset = xr.Dataset({
        'parameter': (['iteration', 'cpu', 'chain', 'parameter_index'], parameter_data),
        'log_likelihood': (['iteration', 'cpu', 'chain'], log_likelihood_data)
    }, coords={
        'iteration': iterations,
        'cpu': cpus,
        'chain': chains,
        'parameter_index': parameters
    })

    return dataset


def test_slice_iteration_of_mcmc_output_xarray_dataset(sample_dataset):
    start_iteration = 2
    end_iteration = 5

    sliced_dataset = slice_iteration_of_mcmc_output_xarray_dataset(
        sample_dataset, start_iteration, end_iteration
    )

    assert len(sliced_dataset['iteration']) == end_iteration - start_iteration
    assert all(value in range(start_iteration, end_iteration) for value in sliced_dataset['iteration'].values)


def test_mcmc_output_xarray_dataset_to_pandas_data_frame(sample_dataset):
    data_frame = mcmc_output_xarray_dataset_to_pandas_data_frame(sample_dataset)

    parameter_columns = [f'parameter{parameter_index}' for parameter_index in sample_dataset['parameter_index'].values]
    expected_columns = parameter_columns + ['log_likelihood']
    assert list(data_frame.columns) == expected_columns

    expected_rows = sample_dataset['iteration'].size * sample_dataset['cpu'].size * sample_dataset['chain'].size
    assert data_frame.shape[0] == expected_rows

    assert (data_frame.loc[5, 2, 1]['parameter1'] ==
            sample_dataset.sel({'iteration': 5, 'cpu': 2, 'chain': 1})['parameter'][1].item())


def test_mcmc_output_xarray_dataset_to_pandas_data_frame_with_limit_from_end(sample_dataset):
    data_frame = mcmc_output_xarray_dataset_to_pandas_data_frame(sample_dataset, limit_from_end=10)

    assert data_frame.shape[0] == 10


def test_mcmc_output_xarray_dataset_to_pandas_data_frame_with_sample_size(sample_dataset):
    data_frame = mcmc_output_xarray_dataset_to_pandas_data_frame(sample_dataset, random_sample_size=10)

    assert data_frame.shape[0] == 10
