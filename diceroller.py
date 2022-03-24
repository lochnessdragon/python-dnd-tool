from common import TreeNode
import random

# rolls a dice with a ceratain number of faces
# a certain number of times
# this is simulated by keeping a running total
# of random.randint results and returning that
def roll(num_dice, dice_faces):
	total = 0
	for i in range(0, num_dice):
		total += random.randint(0, dice_faces)
	return total

# resolves an abstract syntax tree by recursively
# cycling down its branches

def resolveAST(rootNode):
	result = 0
	
	# if the data type is an integer, return it
	if(isinstance(rootNode.data, int) or isinstance(rootNode.data, float)):
		result = rootNode.data
	else:
		# if its an operator, get the results of the right and the left and use
		if(rootNode.left != None):
			left = resolveAST(rootNode.left)
		else:
			print("Trying to parse incomplete AST!")
			return 0
		
		if(rootNode.right != None):
			right = resolveAST(rootNode.right)
		else:
			print("Trying to parse incomplete AST!")
			return 0

		if rootNode.data == 'd':
			# the d is a dice operator
			result = roll(left, right)
		elif rootNode.data == '+':
			# plus is addition
			result = left + right
		elif rootNode.data == '-':
			# minus is subtraction
			result = left - right
		elif rootNode.data == '*':
			# star is multiplication
			result = left * right
		elif rootNode.data == '/':
			# slash is division
			result = left / right
		elif rootNode.data == "^":
			# carat is exponential
			result = left**right
			# im not going to include sqrt bc IDK why
			# you would need that in a d&d game
			# just get a calculator at that point
		else:
			print("Could not resolve the operator: " + rootNode.data)
			result = 0
		
		# print the results
		print(left, rootNode.data, right, "=", result)

	# at the end, return the result
	return result

# the rolling command
def roll_cmd(cmd):
	if(len(cmd) < 2):
		print("Enter a dice literal (like 1d4 or 1d6 + 2):")
		dicestr = input("> ").strip()
	else:
		dicestr = cmd[1]
	print("Rolling:", dicestr)

	# make the abstract syntax tree

	# debug print for checking
	print(ast)

	# resolve the syntax tree and compute the result
	print("Roll Result: " + str(resolveAST(ast)))
	