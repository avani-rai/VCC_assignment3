import multiprocessing as mp
import numpy as np
import time

def matrix_multiply(size):
    """Performs matrix multiplication to stress the CPU."""
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    return np.dot(A, B)

def worker(task_id, size, duration):
    """Worker function for multiprocessing, runs for a specified duration."""
    start_time = time.time()
    while time.time() - start_time < duration:
        result = matrix_multiply(size)
    print(f"Task {task_id} completed after {duration} seconds")
    return result

def main(num_workers=4, matrix_size=1000, duration=60):
    """Main function to spawn worker processes."""
    print(f"Starting {num_workers} workers with matrix size {matrix_size}x{matrix_size} for {duration} seconds")
    with mp.Pool(num_workers) as pool:
        pool.starmap(worker, [(i, matrix_size, duration) for i in range(num_workers)])

if __name__ == "__main__":
    num_workers = mp.cpu_count()  # Scale based on available CPU cores
    matrix_size = 2000  # Increase size for higher CPU load
    duration = 600  # Run continuously for 10 minutes
    main(num_workers, matrix_size, duration)
