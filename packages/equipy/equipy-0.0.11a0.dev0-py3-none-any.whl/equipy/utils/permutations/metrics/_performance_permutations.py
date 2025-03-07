"""Calculation of performance sequentially with respect to all orders of sensitive variables"""

import numpy as np
from typing import Callable, Optional, Union
from sklearn.metrics import mean_squared_error

from ....metrics._performance_metrics import performance_dict
from ....utils.checkers import _check_type, _check_positive_class


def performance_permutations(y_true: np.ndarray, permut_y_fair_dict: dict[tuple, dict[str, np.ndarray]], metric: Callable = mean_squared_error, threshold: Optional[float] = None, positive_class: Union[int, str] = 1) -> list[dict[str, float]]:
    """
    Compute the performance values for multiple fair output datasets compared to the true labels, considering permutations.

    Parameters
    ----------
    y_true : np.ndarray
        Actual values.
    permut_y_fair_dict : dict
        A dictionary containing permutations of fair output datasets.
    metric : Callable, default = sklearn.metrics.mean_squared_error
        The metric used to compute the performance, default=sklearn.metrics.mean_square_error.
    threshold : float, default = None
        The threshold used to transform scores from binary classification into labels for evaluation of performance.
    positive_class : int or str, optional, default=1
        The positive class label used for applying threshold in the case of binary classification. Can be either an integer or a string.

    Returns
    -------
    list
        A list of dictionaries containing performance values for each permutation of fair output datasets.

    Example
    -------
    >>> y_true = np.array([15, 38, 68])
    >>> permut_y_fair_dict = {(1,2): {'Base model':np.array([19,39,65]), 'sens_var_1':np.array([22,40,50]), 'sens_var_2':np.array([28,39,42])},
    ...                        (2,1): {'Base model':np.array([19,39,65]), 'sens_var_2':np.array([34,39,60]), 'sens_var_1':np.array([28,39,42])}}
    >>> performance_values = compute_performance_permutations(y_true, permut_y_fair_dict)
    >>> print(performance_values)
    [{'Base model': 8.666666666666666, 'sens_var_1': 125.66666666666667, 'sens_var_2': 282.0}, 
     {'Base model': 8.666666666666666, 'sens_var_2': 142.0, 'sens_var_1': 282.0}]
    """
    performance_list = []
    
    for value in permut_y_fair_dict.values():
        performance_list.append(performance_dict(
            y_true, value, metric, threshold, positive_class))
    return performance_list