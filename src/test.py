from pybt import node
from pybt import tree


bt = tree()
bt.fill_with_random(50, 0, 1000)
#bt.fill_with_array([7,4,3,5,9,8,11,12])
#print("tree array: 	   " ,bt.get_tree_array(cur_node=bt.root, array=[]))
print("sorted tree array: " ,bt.get_tree_array_sorted(cur_node=bt.root, array=[]))
print("Max height: ", bt.get_max_height(cur_node=bt.root))