# Time series functions ---------------------------------------------------------------------------

# Libraries ---------------------------------------------------------------------------------------
import numpy as np
from scipy.interpolate import (
    CubicSpline,
    PchipInterpolator,
    Akima1DInterpolator
)


# 1. Fill missing values in a time series using spline interpolation -------------------------------
def fill_spline(
    x,
    inside=True,
    outside=True,
    back=False,
    method="natural"
):
    """
    Fill missing values using spline interpolation.

    Parameters
    ----------
    x : array-like
        Time series containing numeric values and NaN values.

    inside : bool, default=True
        Fill missing values between the first and last non-NA values.

    outside : bool, default=True
        Fill missing values outside the observed range.

    back : bool, default=False
        If True, fill missing values before the first non-NA value.

    method : str, default="natural"
        Interpolation method. Choose one of:
        "natural", "not-a-knot", "periodic", "pchip", "akima".

    Returns
    -------
    numpy.ndarray
        Time series with missing values filled.
    """

    # Available methods
    methods = [
        "natural",
        "not-a-knot",
        "periodic",
        "pchip",
        "akima"
    ]

    # Check method
    if method not in methods:
        raise ValueError(
            f"Invalid method '{method}'. "
            f"Choose one of: {', '.join(methods)}"
        )

    # Convert to numeric array
    x = np.asarray(x, dtype=float)

    n = len(x)

    # Non-NA indices
    idx = np.where(~np.isnan(x))[0]

    # At least two non-NA values required
    if len(idx) < 2:
        raise ValueError(
            "At least two non-NA values are required for spline filling."
        )

    # Copy original data
    y = x.copy()

    # Python indices → spline x values
    x_idx = idx + 1

    # ------------------------------------------------------------------
    # Create interpolation function
    # ------------------------------------------------------------------

    if method == "natural":

        sf = CubicSpline(
            x_idx,
            x[idx],
            bc_type="natural"
        )

    elif method == "not-a-knot":

        sf = CubicSpline(
            x_idx,
            x[idx]
        )

    elif method == "periodic":

        # Periodic spline requires first and last values to be equal
        if not np.isclose(x[idx[0]], x[idx[-1]]):
            raise ValueError(
                "For 'periodic' interpolation, "
                "the first and last non-NA values must be equal."
            )

        sf = CubicSpline(
            x_idx,
            x[idx],
            bc_type="periodic"
        )

    elif method == "pchip":

        sf = PchipInterpolator(
            x_idx,
            x[idx]
        )

    elif method == "akima":

        sf = Akima1DInterpolator(
            x_idx,
            x[idx]
        )

    # ------------------------------------------------------------------
    # Fill inside missing values
    # ------------------------------------------------------------------

    if inside:

        left = idx[0]
        right = idx[-1]

        na_inside = np.where(
            np.isnan(x) &
            (np.arange(n) >= left) &
            (np.arange(n) <= right)
        )[0]

        if len(na_inside) > 0:
            y[na_inside] = sf(na_inside + 1)

    # ------------------------------------------------------------------
    # Fill outside missing values
    # ------------------------------------------------------------------

    if outside:

        # Fill values before first observed value
        if back and idx[0] > 0:

            left_idx = np.arange(0, idx[0])

            y[left_idx] = sf(left_idx + 1)

        # Fill values after last observed value
        if idx[-1] < n - 1:

            right_idx = np.arange(idx[-1] + 1, n)

            y[right_idx] = sf(right_idx + 1)

    return y

