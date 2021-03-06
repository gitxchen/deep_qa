from itertools import zip_longest
from typing import Any, Dict, List
import random


def group_by_count(iterable: List[Any], count: int, default_value: Any) -> List[List[Any]]:
    """
    Takes a list and groups it into sublists of size ``count``, using ``default_value`` to pad the
    list at the end if the list is not divisable by ``count``.

    For example:
    >>> group_by_count([1, 2, 3, 4, 5, 6, 7], 3, 0)
    [[1, 2, 3], [4, 5, 6], [7, 0, 0]]

    This is a short method, but it's complicated and hard to remember as a one-liner, so we just
    make a function out of it.
    """
    return [list(l) for l in zip_longest(*[iter(iterable)] * count, fillvalue=default_value)]


def add_noise_to_dict_values(dictionary: Dict[Any, float], noise_param: float) -> Dict[Any, float]:
    """
    Returns a new dictionary with noise added to every key in ``dictionary``.  The noise is
    uniformly distributed within ``noise_param`` percent of the value for every value in the
    dictionary.
    """
    new_dict = {}
    for key, value in dictionary.items():
        noise_value = value * noise_param
        noise = random.uniform(-noise_value, noise_value)
        new_dict[key] = value + noise
    return new_dict


def clean_layer_name(input_name: str,
                     strip_right_of_last_backslash: bool=True,
                     strip_numerics_after_underscores: bool=True):
    """
    There exist cases when layer names need to be concatenated in order to create new, unique
    layer names. However, the indices added to layer names designating the ith output of calling
    the layer cannot occur within a layer name apart from at the end, so this utility function
    removes these.

    Parameters
    ----------

    input_name: str, required
        A Keras layer name.
    strip_right_of_last_backslash: bool, optional, (default = True)
        Should we strip anything past the last backslash in the name?
        This can be useful for controlling scopes.
    strip_numerics_after_underscores: bool, optional, (default = True)
        If there are numerical values after an underscore at the end of the layer name,
        this flag specifies whether or not to remove them.
    """
    # Always strip anything after :, as these will be numerical
    # counts of the number of times the layer has been called,
    # which cannot be included in a layer name.
    if ':' in input_name:
        input_name = input_name.split(':')[0]
    if '/' in input_name and strip_right_of_last_backslash:
        input_name = input_name.rsplit('/', 1)[0]
    if input_name.split('_')[-1].isdigit() and strip_numerics_after_underscores:
        input_name = '_'.join(input_name.split('_')[:-1])

    return input_name
