
class Priority_Queue:
    def __init__(self):
        self.pqueue = []
        self.length = 0
    
    def insert(self, node):
        for i in self.pqueue:
            get_bound(i)
        i = 0
        while i < len(self.pqueue):
            if self.pqueue[i].bound > node.bound:
                break
            i+=1
        self.pqueue.insert(i,node)
        self.length += 1

    def print_pqueue(self):
        for i in list(range(len(self.pqueue))):
            print ("pqueue",i, "=", self.pqueue[i].bound)
                    
    def remove(self):
        try:
            result = self.pqueue.pop()
            self.length -= 1
        except: 
            print("Priority queue is empty.")
        else:
            return result
        
class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.items = []
        
            
def get_bound(node):
    if node.weight >= capacity:
        return 0
    else:
        result = node.profit
        j = node.level + 1
        totweight = node.weight
        while j <= items-1 and totweight + weightOfItem[j] <= capacity:
            totweight = totweight + weightOfItem[j]
            result = result + profitOfItem[j]
            j+=1
        k = j
        if k<=items-1:
            result = result + (capacity - totweight) * pricePerWeight[k]
        return result


# Driver Code :
items = int(input("\nEnter No of items : "))
capacity = int(input("Enter Capacity : "))
profitOfItem = list(map(int, input("Enter Profit of Each Item : ").split()))
weightOfItem = list(map(int, input("Enter Weight of each Item : ").split()))
pricePerWeight = list(map(int, input("Enter Price per Weight : ").split()))

# n = 4
# W = 16
# p = [40, 30, 50, 10]
# w = [2, 5, 10, 5]
# p_per_weight = [20, 6, 5, 2]

nodes_generated = 0
pq = Priority_Queue()

v = Node(-1, 0, 0) 
nodes_generated+=1
maxprofit = 0 
v.bound = get_bound(v)

pq.insert(v)

while pq.length != 0:
    
    v = pq.remove()

    if v.bound > maxprofit: 
        u = Node(0, 0, 0)
        nodes_generated+=1
        u.level = v.level + 1
        u.profit = v.profit + profitOfItem[u.level]
        u.weight = v.weight + weightOfItem[u.level]
       
        u.items = v.items.copy()
        u.items.append(u.level) 
        if u.weight <= capacity and u.profit > maxprofit: 
            maxprofit = u.profit
            bestitems = u.items
        u.bound = get_bound(u)
        if u.bound > maxprofit:
            pq.insert(u)
        u2 = Node(u.level, v.profit, v.weight)
        nodes_generated+=1
        u2.bound = get_bound(u2)
        u2.items = v.items.copy()

        if u2.bound > maxprofit:
            pq.insert(u2)


print("\nMaxprofit = ", maxprofit)
