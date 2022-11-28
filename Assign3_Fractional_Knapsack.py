class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

# Main greedy function to solve problem
def fractionalKnapsack(W, arr):

	# sorting Item on basis of ratio
	arr.sort(key = lambda x: (x.value/x.weight), reverse = True)

	finalvalue = 0.0

	# Looping through all Items
	for item in arr:
		if item.weight <= W:
			W -= item.weight
			finalvalue += item.value
		else:
			finalvalue += item.value * W / item.weight
			break
	return finalvalue

# Driver's Code
# Weigth = 50
# arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

Weigth = int(input("\nEnter Weight : "))
items = int(input("\nEnter No of Items : "))
arr = []

for i in range(items):
	key,val = map(int, input(f"Enter Items {i+1} : ").split())
	arr.append(Item(key, val))

max_val = fractionalKnapsack(Weigth, arr)
print (f'\nBags filled with objects worth : {int(max_val)}')