# K-Means Clustering with Parallel Processing

## Algorithm and Parallelization Method
This project implements the K-Means clustering algorithm using both sequential and parallel approaches. The sequential version is implemented in `kmeans_sequential.py`, while the parallel version utilizes Dask for distributed computing in `kmeans_parallel.py`.

## Instructions to Reproduce Results
1. **Clone the Repository**:
`https://github.com/KarinaFed/PAforASD2024.git`
`cd PAforASD2024`
3. **Install Required Libraries**:
Make sure you have Python installed, then install the required libraries:
`pip install pandas matplotlib scikit-learn dask[complete] dask-ml`
4. **Run the Benchmark**:
Execute the benchmark script to generate synthetic data and compare the performance of the sequential and parallel implementations:
`python3 benchmark.py`
5. **Data Generation**:
The dataset is generated within the benchmark script using `make_blobs` from `sklearn`. No external data files are needed.

## Parallelization Details
The parallelization is achieved using Dask, which allows for efficient distribution of the K-Means algorithm across multiple processes. The data is split into chunks that can be processed in parallel, significantly reducing computation time.

## Speedup Calculation
The following results were obtained during benchmarking:

- Sequential time: 6.17 seconds
- Parallel time (2 processes): 3.02 seconds
- Parallel time (4 processes): 1.87 seconds
- Parallel time (8 processes): 1.76 seconds

### Speedups:
- Speedup for 2 processes: 2.05
- Speedup for 4 processes: 3.30
- Speedup for 8 processes: 3.50
  
### Graph
The graph is generated: `speedup_graph.png`: Displays speedup as a function of the number of processes.
