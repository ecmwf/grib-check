import os

# grib-check does not use BLAS, but importing numpy starts a BLAS thread pool sized to the
# number of cores in every process. With many worker processes (-j) this oversubscribes the
# machine and can exhaust the thread limit, causing worker hangs. Default to single-threaded
# BLAS unless the user explicitly configured it. Must run before numpy is imported.
for _var in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_var, "1")
