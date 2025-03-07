# dind3

`dind3` is a lightweight Python library that automatically imports NumPy,Pandas and Matplotlib as `np`,`pd`and `plt`.

## Installation
```sh
pip install dind
```
## Usage
```sh
from dind import np, pd

print(np.array([1, 2, 3]))
print(pd.DataFrame({"A": [1, 2, 3]}))

```