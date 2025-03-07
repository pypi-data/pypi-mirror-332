"""
Computation of the performance (i.e. measurement of the similarity between prediction and actual value).
"""

# Authors: Agathe F, Suzie G, Francois H, Philipp R, Arthur C
# License: BSD 3 clause
import numpy as np
from typing import Callable, Optional, Union
from sklearn.metrics import mean_squared_error
from ..utils.checkers import _check_metric, _check_type, _check_positive_class


def performance(y_true: np.ndarray, y_pred: np.ndarray, metric: Callable = mean_squared_error) -> float:
    """
    Compute the performance value for predicted fair output compared to the true labels.

    Parameters
    ----------
    y_true : np.ndarray
        Actual values.
    y_pred : np.ndarray
        Predicted (fair or not) output values. 
    metric : Callable, (default=mean_squared_error)
        The metric used to compute the performance, which expects y_true then y_pred,
        default=sklearn.metrics.mean_square_error.

    Returns
    -------
    float
        The calculated performance value.

    Example
    -------
    >>> from sklearn.metrics import f1_score
    >>> y_true = np.array([1, 0, 1, 1, 0])
    >>> y_pred = np.array([0, 1, 1, 1, 0])
    >>> classification_performance = compute_performance(y_true, y_pred, f1_score)
    >>> print(classification_performance)
    0.6

    >>> y_true = [1.2, 2.5, 3.8, 4.0, 5.2]
    >>> y_pred = [1.0, 2.7, 3.5, 4.2, 5.0]
    >>> regression_performance = compute_performance(y_true, y_pred)
    >>> print(regression_performance)
    0.05
    """

    _check_metric(y_true, metric)

    return metric(y_true, y_pred)


def performance_dict(y_true: np.ndarray,
                     y_fair_dict: dict[str, np.ndarray],
                     metric: Callable = mean_squared_error,
                     threshold: Optional[float] = None,
                     positive_class: Union[int, str] = 1) -> dict[str, float]:
    """
    Compute the performance values for multiple fair output datasets compared to the true events.

    Parameters
    ----------
    y_true : np.ndarray
        Actual values.
    y_fair_dict : dict
        A dictionary containing sequentially fair output datasets.
    metric : Callable, optional
        The metric used to compute the performance, default=sklearn.metrics.mean_square_error.
    threshold : float, default = None
        In the case of classification, the threshold used to transform scores from binary
        classification into labels for evaluation of performance.
    positive_class : int or str, optional, default=1
        In the case of classification, the positive class label used for applying threshold of
        binary classification. Can be either an integer or a string.

    Returns
    -------
    dict
        A dictionary containing performance values for sequentially fair output datasets.

    Example
    -------
    >>> y_true = np.array([15, 38, 68])
    >>> y_fair_dict = {'Base model':np.array([19,39,65]), 'color':np.array([22,40,50]),
                        'nb_child':np.array([28,39,42])}
    >>> performance_values = performance_dict(y_true, y_fair_dict)
    >>> print(performance_values)
    {'Base model': 8.666666666666666, 'color': 125.66666666666667, 'nb_child': 282.0}

    >>> from sklearn.metrics import f1_score
    >>> y_true = np.array(['yes', 'no', 'yes'])
    >>> y_fair_dict = {'Base model':np.array([0.19,0.39,0.65]), 'color':np.array([0.22,0.40,0.50]),
                                            'nb_child':np.array([0.28,0.39,0.42])}
    >>> performance_values = performance_dict(y_true, y_fair_dict, f1_score, threshold=0.5,
                                              positive_class='yes')
    >>> print(performance_values)
    {'Base model': 8.666666666666666, 'color': 125.66666666666667, 'nb_child': 282.0}
    """
    _check_type(y_true, y_fair_dict, threshold=threshold)
    if threshold is not None:
        _check_positive_class(y_true, positive_class)
        negative_class = list(set(y_true) - {positive_class})[0]
       
    performance_dict = {}
    for key in y_fair_dict.keys():
        if threshold is not None:
            scores_fair = list(y_fair_dict[key])
            labels_fair = [positive_class if score >= threshold else negative_class for score in scores_fair]
            performance_dict[key] = metric(y_true, labels_fair)
        else:
            performance_dict[key] = metric(y_true, list(y_fair_dict[key]))
    return performance_dict