def write_file(name, contents):
	file = open(name, "w")
	file.write(contents)
	file.close()

def read_file(name):
	file = open(name, "r")
	contents = file.read()
	file.close()
	return contents

class TreeNode:
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None
	
	def __init__(self, left, right, data):
		self.left = left
		self.right = right
		self.data = data
	
	@staticmethod
	def create_branchless(data):
		return TreeNode(None, None, data)

	def __str__(self):
		result = "TreeNode: data=" + str(self.data)
		if(self.left != None):
			result += "\nleft={\n" + "  " + str(self.left).replace("\n", "\n  ") + "\n}"
		if(self.right != None):
			result += "\nright={\n" + "  " + str(self.right).replace("\n", "\n  ") + "\n}"
		
		return result