import numpy as np
from scipy.optimize import basinhopping

def MLE(pdf, x, p0):
    nll = lambda p: -np.sum(np.log(np.maximum(pdf(x, p), 1e-300))
    return basinhopping(nll, p0, niter=200, minimizer_kwargs={"method": "Neldeer-Mead"}).x
