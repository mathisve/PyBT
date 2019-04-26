from pybt import node
from pybt import tree


bt = tree()
bt.fill_with_random(size=15, min_range=0, max_range=999)
print("root: " ,bt.get_root())
print("tree array: 	   " ,bt.get_tree_array(cur_node=bt.root))
print("sorted tree array: " ,bt.get_tree_array_sorted(cur_node=bt.root))