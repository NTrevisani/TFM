"""
python mkConvergenceTest.py 10 22 2
"""

import sys, os

os.system("cp ../Functions.py .")

# Import all the functions needed
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from qiskit.visualization import plot_histogram
from Functions import VQE_circuit, convergence_tester, cost_function_C
from Functions import random_graph_producer, brute_force_solver

# Define PI
PI = np.pi

# Input arguments
if len(sys.argv) < 4:
    raise ValueError("""Please insert: 
    number of qbits 
    number of edges
    circuit depth""")

# Define parameters
n_qbits = int(sys.argv[1])
n_edge  = int(sys.argv[2])
n_depth = int(sys.argv[3])

# Print input values
print("N qubits:      {0}".format(n_qbits))
print("N edges:       {0}".format(n_edge))
print("Circuit depth: {0}".format(n_depth))
print("------------------")

# Create random max-cut problem 
M = random_graph_producer(n_vert = n_qbits, 
                          n_edge = n_edge, 
                          seed = 2000, 
                          verbosity = False)

# Get the solution
brute_solution, brute_cost, eig = brute_force_solver(M, verbosity = False)

theta_0       = np.repeat(PI/2, n_qbits)
theta_0.shape = (1, n_qbits)
theta_1       = np.zeros((n_depth, n_qbits))
x_0           = np.concatenate((theta_0, theta_1), axis = 0) 

# Variables definition
shots_list    = [1, 2, 4, 8, 12, 16, 24, 32, 64, 96, 128, 256, 512]
rep           = 1000

# Create folder for figures
folder_name  = "figures/convergence/{0}qbits_{1}edges_ry_ansatz/".format(n_qbits, n_edge)
save_command = "mkdir -p {0}".format(folder_name)
os.system(save_command)

# Loop over number of shots
for shot in shots_list:

    print("Testing {} shots".format(shot))
    
    ref_eig, ref_cost, test_eig, test_cost = convergence_tester(n_qbits     = n_qbits, 
                                                                n_edges     = n_edge, 
                                                                depth       = n_depth, 
                                                                shots       = shot,
                                                                x0          = x_0,
                                                                repetitions = rep)



    save_as = "{0}{1}_shots".format(folder_name, shot)

    fig, ax = plt.subplots()

    y, x, _ = plt.hist(test_cost, 
                       bins = int(1.5*brute_cost), 
                       range = (-1.5*brute_cost, 0), 
                       density = True)

    ax.text(0.05, 0.90, "Reference = {:.1f}".format(ref_cost), 
            transform=ax.transAxes)
    ax.text(0.05, 0.84, "Mean = {:.1f}".format(np.mean(test_cost)), 
            transform=ax.transAxes)
    ax.text(0.05, 0.78, "Sigma = {:.1f}".format(np.std(test_cost)), 
            transform=ax.transAxes)
    ax.text(0.05, 0.72, "Range = ({:.1f}, {:.1f})".format(np.min(test_cost), np.max(test_cost)), 
            transform=ax.transAxes)

    # Save as png and pdf
    if save_as != "":
        plt.savefig(save_as + '.png')
        plt.savefig(save_as + '.pdf')

    # Close
    plt.close()

# Create new directory in upper folder
new_dir_command = "mkdir -p ../{0}".format(folder_name)
os.system(new_dir_command)

# Copy file there
copy_command = "cp {0}/* ../{1}/".format(folder_name, folder_name)
os.system(copy_command)

# Finally, delete the original output folder
delete_command = "rm -r {0}".format(folder_name)
os.system(delete_command)
