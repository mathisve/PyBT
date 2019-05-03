class node:
	def __init__(self, value=None):
		self.value= value
		self.r_child=None
		self.l_child=None

		self.leaf=False

	def is_leaf(self):
		if(self.r_child == None and self.l_child == None):
			self.leaf=True
			return True
		else:
			self.leaf=False
			return False

class tree:
	def __init__(self):
		self.root=None

	def insert(self, value, cur_node):
		if(self.root==None):
			self.root=node(value)
		else:
			if(value<cur_node.value):
				if(cur_node.l_child==None):
					cur_node.l_child=node(value)
				else:
					self.insert(value, cur_node.l_child)    
			else:
				if(cur_node.r_child==None):
					cur_node.r_child=node(value)
				else:   
					self.insert(value, cur_node.r_child)

	def get_tree_array(self, cur_node, array=[]):
		if(self.root==None):
			return []
		if(cur_node!=None):
			self.get_tree_array(cur_node.l_child, array)
			self.get_tree_array(cur_node.r_child, array)
			array.append(cur_node.value)
			return array
		else:
			return array

	def get_tree_array_sorted(self, cur_node, array=[]):
		if(self.root==None):
			return []
		if(cur_node!=None):
			self.get_tree_array_sorted(cur_node.l_child, array)
			array.append(cur_node.value)
			self.get_tree_array_sorted(cur_node.r_child, array)
			return array

	def get_max_height(self, cur_node, cur_height=1, max_height=1):
		if(self.root==None):
			return 0

		def check_cur_max(cur_height, max_height):
			if(cur_height > max_height):
				max_height = cur_height
			return max_height

		if(cur_node!=None):
			max_height = self.get_max_height(cur_node.l_child, cur_height, max_height)
			max_height = check_cur_max(cur_height, max_height)
			max_height = self.get_max_height(cur_node.r_child, cur_height, max_height)
			max_height = check_cur_max(cur_height, max_height)
			return max_height + 1
		else:
			return max_height


	def get_root(self):
		return self.root.value 

	def fill_with_array(self, array=[]):
		for x in array:
			self.insert(x, self.root)

	def fill_with_random(self, size, min_range, max_range):
		from random import randint
		for _ in range(size):
			value = randint(min_range, max_range)
			if(self.insert(value, self.root)==False):
				size += 1
			else:
				pass
		return tree