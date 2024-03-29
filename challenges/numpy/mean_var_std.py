""" Mean, Var, and Std Challenge """
from dataclasses import dataclass
from typing import Union

import numpy as np

from challenges.numpy.utils import get_entries

CustomNdArray = Union[float, np.ndarray, int]


@dataclass
class NumpyData:
    """Dataclass for mean, var, and std"""

    mean: CustomNdArray
    var: CustomNdArray
    std: CustomNdArray

    def __str__(self) -> str:
        return f"{self.mean}\n{self.var}\n{self.std}"


def mean_var_std(data: list[list[int]]) -> NumpyData:
    """Appliyng min and max operations on data"""
    arr = np.array(data)
    return NumpyData(
        arr.mean(axis=1),
        arr.var(axis=0),
        np.round(arr.std(), 11),
    )


def main() -> None:
    """Main function"""
    # np.set_printoptions(legacy=False)

    result = mean_var_std(get_entries())
    print(result)


if __name__ == "__main__":
    main()
