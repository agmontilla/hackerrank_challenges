""" Mean, Var, and Std Challenge """
import numpy as np

from challenges.numpy.utils import get_entries


def mean_var_std(data: list[list[int]]) -> tuple:
    """Appliyng min and max operations on data"""
    arr = np.array(data)
    return (
        arr.mean(axis=1),
        arr.var(axis=0),
        np.round(arr.std(), 11),
    )


def main() -> None:
    """Main function"""
    np.set_printoptions(legacy="1.13")
    print(*mean_var_std(get_entries()), sep="\n")


if __name__ == "__main__":
    main()
