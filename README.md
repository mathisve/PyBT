# PyBT
PyBT (or Python Binary Tree) is a package designed to make working with [binary trees](https://en.wikipedia.org/wiki/Binary_tree) a breeze! It sets up a whole framework that support nodes, children, roots, ect.

## How to use
First import the package as such (after you've placed the `pybt.py` file in the same directory (we're not on PyPI yet))
```python
from pybt import node
from pybt import tree

or

from pybt import node, tree
```

Then you need to make a `tree` object as such:
```python
bt = tree()
```
And thats it! Now you can start playing with the awesome functions it has!
### fill_with_random
`fill_with_random` is a function that fills the tree with random ints. `size` is the size of the desired tree, `min_range` and `max_range` set a limit to how big or small the integers can be.
```python
>>> bt.fill_with_random(size=20, min_range=0, max_range=1000)
```

### get_tree_array
`get_tree_array` is pretty self explanatory, it returns the tree in an array as if it were projected on an array under the tree.
```python
>>> result = bt.get_tree_array(bt.root)
>>> print(result)
[110, 136, 89, 574, 459, 803, 946, 929, 966, 748]
```

### get_tree_array_sorted
`get_tree_array_sorted` is even more self explanatory! It returns the tree array but sorted. Take note that is an independent function from `get_tree_array`! Because it reads trough the binary tree only once the time complexity is still O(n) !
```python
>>> result = bt.get_tree_array_sorted(bt.root)
>>> print(result)
[89, 110, 136, 459, 574, 748, 803, 929, 946, 966]
```

### get_max_height
`get_max_height` returns the maximum height of the tree.
```python
>>> result = bt.get_max_height(bt.root)
>>> print(result)
5
```

### get_root
`get_root` returns the root of the binary tree, aka the first value.
```python
>>> result = bt.get_root()
>>> print(result)
748
```