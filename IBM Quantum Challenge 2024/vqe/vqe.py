!pip install qiskit-aer

!pip install qiskit-ibm-runtime # Install qiskit-ibm-runtime which includes qiskit_serverless

from qiskit_aer import AerSimulator
import logging
from typing import Optional
import time
import numpy as np
from scipy.optimize import minimize

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import ( # Now this import should work
    EstimatorV2 as Estimator,
    SamplerV2 as Sampler,
    QiskitRuntimeService,
    Session,
)
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

Logging = logging.getLogger(__name__)

def run(params, ansatz, hamiltonian, estimator, callback_dict):
    """Return callback function that uses Estimator instance,
    and stores intermediate values into a dictionary.

    Parameters:
        params (ndarray): Array of ansatz parameters
        ansatz (QuantumCircuit): Parameterized ansatz circuit
        hamiltonian (SparsePauliOp): Operator representation of Hamiltonian
        estimator (Estimator): Estimator primitive instance
        callback_dict (dict): Mutable dict for storing values

    Returns:
        Callable: Callback function object
    """
    result = estimator.run([(ansatz, [hamiltonian], [params])]).result()
    energy = result[0].data.evs[0]

    # Keep track of the number of iterations
    callback_dict["iters"] += 1
    # Set the prev_vector to the latest one
    callback_dict["prev_vector"] = params
    # Compute the value of the cost function at the current vector
    callback_dict["cost_history"].append(energy)
    # Grab the current time
    current_time = time.perf_counter()
    # Find the total time of the execute (after the 1st iteration)
    if callback_dict["iters"] > 1:
        callback_dict["_total_time"] += current_time - callback_dict["_prev_time"]
    # Set the previous time to the current time
    callback_dict["_prev_time"] = current_time
    # Compute the average time per iteration and round it
    time_str = (
        round(callback_dict["_total_time"] / (callback_dict["iters"] - 1), 2)
        if callback_dict["_total_time"]
        else "-"
    )
    # Print to screen on single line
    print(
        "Iters. done: {} [Avg. time per iter: {}]".format(
            callback_dict["iters"], time_str
        ),
        end="\r",
        flush=True,
    )

    return energy, result


def cost_func(*args, **kwargs):
    """Return estimate of energy from estimator

    Parameters:
        params (ndarray): Array of ansatz parameters
        ansatz (QuantumCircuit): Parameterized ansatz circuit
        hamiltonian (SparsePauliOp): Operator representation of Hamiltonian
        estimator (Estimator): Estimator primitive instance

    Returns:
        float: Energy estimate
    """
    energy, result = run(*args, **kwargs)
    return energy


def run_vqe(initial_parameters, ansatz, operator, estimator, method):
    callback_dict = {
        "prev_vector": None,
        "iters": 0,
        "cost_history": [],
        "_total_time": 0,
        "_prev_time": None,
    }

    result = minimize(
        cost_func,
        initial_parameters,
        args=(ansatz, operator, estimator, callback_dict),
        method=method,
    )
    return result, callback_dict


if __name__ == "__main__":
    # Removed call to get_arguments, replace with how you want to get arguments
    # For example, you might get them from command line using argparse 
    # Or you might hardcode them for testing
    service = None # Replace with your service if needed
    ansatz =  QuantumCircuit(2) # Replace with your ansatz
    operator = None # Replace with your operator
    method = "COBYLA" 
    initial_parameters = None # Or
