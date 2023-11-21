import copy
import itertools
from launchkit.utils import merge_recursive_dicts, dot_map_dict_to_nested_dict


class DeterministicHyperparameterSweeper:
    """
    Note: from https://github.com/rail-berkeley/rlkit/blob/c81509d982b4d52a6239e7bfe7d2540e3d3cd986/rlkit/util/hyperparameter.py#L151

    Do a grid search over hyperparameters based on a predefined set of
    hyperparameters.
    """
    def __init__(self, hyperparameters, default_parameters=None):
        """

        :param hyperparameters: A dictionary of the form
        ```
        {
            'hp_1': [value1, value2, value3],
            'hp_2': [value1, value2, value3],
            ...
        }
        ```
        This format is like the param_grid in SciKit-Learn:
        http://scikit-learn.org/stable/modules/grid_search.html#exhaustive-grid-search
        :param default_parameters: Default key-value pairs to add to the
        dictionary.
        """
        self._hyperparameters = hyperparameters
        self._default_kwargs = default_parameters or {}
        named_hyperparameters = []
        for name, values in self._hyperparameters.items():
            named_hyperparameters.append(
                [(name, v) for v in values]
            )
        self._hyperparameters_dicts = [
            dot_map_dict_to_nested_dict(dict(tuple_list))
            for tuple_list in itertools.product(*named_hyperparameters)
        ]

    def iterate_hyperparameters(self):
        """
        Iterate over the hyperparameters in a grid-manner.

        :return: List of dictionaries. Each dictionary is a map from name to
        hyperpameter.
        """
        return [
            merge_recursive_dicts(
                hyperparameters,
                copy.deepcopy(self._default_kwargs),
                ignore_duplicate_keys_in_second_dict=True,
            )
            for hyperparameters in self._hyperparameters_dicts
        ]