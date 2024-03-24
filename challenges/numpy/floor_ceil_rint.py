import numpy as np

if __name__ == "__main__":
    arr = np.array(list(map(float, input().strip().split())))
    np.set_printoptions(legacy="1.13")
    for operation in ("floor", "ceil", "rint"):
        print((getattr(np, operation)(arr)))
