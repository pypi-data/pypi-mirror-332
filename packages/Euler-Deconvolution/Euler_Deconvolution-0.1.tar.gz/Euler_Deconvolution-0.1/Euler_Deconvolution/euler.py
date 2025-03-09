import numpy as np
import scipy.linalg as la

class EulerDeconvolution:
    def __init__(self, x, y, z, T, window_size=5, structural_index=1):
        """
        Initialize Euler Deconvolution.
        
        Parameters:
        x, y, z: Coordinates of data points (numpy arrays)
        T: Magnetic field intensity (numpy array)
        window_size: Number of points in a local window for computation
        structural_index: Structural index (SI) of the source
        """
        self.x = np.asarray(x)
        self.y = np.asarray(y)
        self.z = np.asarray(z)
        self.T = np.asarray(T)
        self.window_size = window_size
        self.structural_index = structural_index

    def compute_derivatives(self):
        """Compute spatial derivatives of the magnetic field."""
        dTx = np.gradient(self.T, self.x, edge_order=1)
        dTy = np.gradient(self.T, self.y, edge_order=1)
        dTz = np.gradient(self.T, self.z, edge_order=1)
        return dTx, dTy, dTz

    def solve_euler(self):
        """Solve Euler's equation to estimate source location and depth."""
        dTx, dTy, dTz = self.compute_derivatives()
        solutions = []
        
        for i in range(len(self.x) - self.window_size):
            X = np.array([
                self.x[i:i+self.window_size],
                self.y[i:i+self.window_size],
                self.z[i:i+self.window_size],
                np.ones(self.window_size)
            ]).T

            B = -self.structural_index * self.T[i:i+self.window_size]
            A = np.array([dTx[i:i+self.window_size], 
                          dTy[i:i+self.window_size], 
                          dTz[i:i+self.window_size], 
                          B]).T

            try:
                solution, _, _, _ = la.lstsq(A, B, lapack_driver='gelsd')
                solutions.append(solution)
            except la.LinAlgError:
                continue
        
        return np.array(solutions)

    def run(self):
        """Execute Euler deconvolution and return estimated source locations."""
        solutions = self.solve_euler()
        if solutions.size == 0:
            print("No valid solutions found.")
        return solutions
