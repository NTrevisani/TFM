"""
VQE
---
10-qbits problem
python3 loop_scan.py cost 1   10 22 VQE
python3 loop_scan.py cvar 0.5 10 22 VQE
python3 loop_scan.py cvar 0.2 10 22 VQE

11-qbits problem
python3 loop_scan.py cost 1   11 27 VQE
python3 loop_scan.py cvar 0.5 11 27 VQE
python3 loop_scan.py cvar 0.2 11 27 VQE

12-qbits problem
python3 loop_scan.py cost 1   12 33 VQE
python3 loop_scan.py cvar 0.5 12 33 VQE
python3 loop_scan.py cvar 0.2 12 33 VQE

13-qbits problem
python3 loop_scan.py cost 1   13 39 VQE
python3 loop_scan.py cvar 0.5 13 39 VQE
python3 loop_scan.py cvar 0.2 13 39 VQE

16-qbits problem
python3 loop_scan.py cost 1   16 60 VQE
python3 loop_scan.py cvar 0.5 16 60 VQE
python3 loop_scan.py cvar 0.2 16 60 VQE

18-qbits problem
python3 loop_scan.py cost 1   18 76 VQE
python3 loop_scan.py cvar 0.5 18 76 VQE
python3 loop_scan.py cvar 0.2 18 76 VQE

Alternative 10-qbits problems
python3 loop_scan.py cost 1   10 10 VQE
python3 loop_scan.py cost 1   10 15 VQE
python3 loop_scan.py cost 1   10 20 VQE
python3 loop_scan.py cost 1   10 25 VQE
python3 loop_scan.py cost 1   10 30 VQE
python3 loop_scan.py cost 1   10 35 VQE
python3 loop_scan.py cost 1   10 40 VQE
python3 loop_scan.py cost 1   10 45 VQE

QAOA
---
10-qbits problem
python3 loop_scan.py cost 1   10 22 QAOA

11-qbits problem
python3 loop_scan.py cost 1   11 27 QAOA

12-qbits problem
python3 loop_scan.py cost 1   12 33 QAOA

13-qbits problem
python3 loop_scan.py cost 1   13 39 QAOA

16-qbits problem
python3 loop_scan.py cost 1   16 60 QAOA

18-qbits problem
python3 loop_scan.py cost 1   18 76 QAOA
"""

import sys, os

n_vertices = 10
n_edges    = 20

if len(sys.argv) < 5:
    raise ValueError("Please insert:\n cost function type\n CVaR alpha value\n number of vertices\n number of edges\ algorithm")
cost       = sys.argv[1]
alpha      = sys.argv[2]
n_vertices = sys.argv[3]
n_edges    = sys.argv[4]
n_algo     = sys.argv[5]

# keep the ratio n_edges/max(n_edges) constant for all n_vertices values
#n_edges = int(0.5*int(n_vertices)*(int(n_vertices)-1) * 0.5)

shots_list = [1, 2, 4, 8, 12, 16, 24, 32, 64, 96, 128, 192, 256, 512]

for shots in shots_list:
    command = "python3.7 scan_script.py {0} {1} {2} {3} {4} {5}&".format(shots,
                                                                     cost,
                                                                     alpha,
                                                                     n_vertices,
                                                                     n_edges,
                                                                     n_algo)
    print(command)
    os.system(command)
