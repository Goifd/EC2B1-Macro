import numpy as np

def get_regression_coefs(Y, x1, x2, x3=None):
    """
    Compute coefficients for trend regressions.

    Given a vector `Y` and a collection of regressors `*args`, return vector of coefficients `coefs`.

    Parameters
    ----------
    Y : (T,) array that will be the dependent variable. In our example, either GDP per capita in
    level or in logs.
    
    x1: (T,) array of the first regressor. By convention, this should be a vector of ones.

    x2: (T,) array of the second regressor.

    x3: If provided, a (T,) array of the third regressor. If not provided, this will be ignored,
    i.e. set to None.

    Returns
    -------
    coefs: This returns the array of coefficients. If we input two regressors (i.e. `x1` and `x2`),
    then coefs = `(a, b)`. If we input three
    regressors (i.e. `x1`, `x2`, and `x3`), then coefs = `(a, b1, b2)`. Ordering `x1` as the vector
    of ones ensures that `a` is the intercept and `b`s the slope coefficients.
    """
    
    T = XXX # number of time periods in regression sample is the length of Y

    if x3 is None:
        # If we do not provide x3 we only combine vectors x1 and x2
        X = np.concatenate((XXX), axis=1)
    else:
        # Otherwise, if we provide x3 we combine vectors x1, x2, and x3 into the X data
        X = np.concatenate((XXX), axis=1)

    coefs = np.linalg.inv(XXX) @ XXX # solve for formula (X'X)^(-1) X'Y

    # Congratulations we just ran a regression.
    return coefs

"""
Additional task (if you're keen and up for the challenge): The above code works perfectly fine in
the case with two or three regressors (x variables), but fails for four or more regressors. To write
better code we would want to allow an arbitrary number of regressors.

Hint: Python has a function option `*args` to do this exactly.

Example:

 >>> def sum(*args):
        s = 0
        for num in args:
            s = s + num
        return(s)
 >>> sum(1, 1)
     2
 >>> sum(1, 2, 3)
     6
"""