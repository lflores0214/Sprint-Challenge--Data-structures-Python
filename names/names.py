import time
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # * base case
        # check if empty
        if self.value == None:
            # if it is put node here
            self.value == value
            print(f"value {self.value}")
        else:
            # if it's not empty and smaller than node put new node to the left
            if value < self.value:
                # check if there is anything on left
                if self.left != None:
                    # if there is then go left again
                    self.left.insert(value)
                else:
                    # if there isn't, insert node here
                    self.left = BinarySearchTree(value)
            # if it's not empty and larger than node put new node to the right
            if value >= self.value:
                # check if there's anything to the right:
                if self.right != None:
                    # if there is go right again
                    self.right.insert(value)
                else:
                    # if there isn't, insert node here
                    self.right = BinarySearchTree(value)

    def contains(self, target):
        # base case
        # if there is no value return false
        if self.value == None:
            return False
        # if self.value is equal to the target return true
        if self.value == target:
            return True
        else:
            # if the target is less than self.value and there is a self.left check the left
            if target < self.value and self.left:
                return self.left.contains(target)
            # if the target is larger than self.value and there is a self.right check the right
            elif target > self.value and self.right:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # max number will always be to the right
        # if there is a right. get max on right
        if self.right != None:
            return self.right.get_max()
        # if there isn't a right, that is the max value
        else:
            # return max value
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # base case
        # if there is no value there is nothing you can do
        # * ended up not needing the below check
        # if self.value == None:
        #     pass
        # else:

        # if there is a value
        if self.value:
            # perform the cb fn on that value
            cb(self.value)
        # if there is a right value
        if self.right != None:
            # recurse to use the cb fn on that value and keep going right until you cant
            self.right.for_each(cb)
        # if there is a left value
        if self.left != None:
            # recurse to use the cb fn on that value and keep going left until you cant
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # left is always the lowest value
    # traverse all the way and start printing from there
    # How can I print all numbers in sequential order?
    # use recursion
    # need a base case
    def in_order_print(self, node):
        # base case
        # if there is no value return nothing
        # * Below check turned out to not be necessary
        # if self.value == None:
        #     return
        # if there is a left value
        if self.left:
            # use recursion to run the fn on the left node till you cant go any more left
            self.left.in_order_print(self.left)
        # once you go as left as you can you should be at the smallest number so print it
        print(node.value)
        # after printing the number you can check the number to the right if there is one since that will be the next biggest number
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    # Breadth first traversal- width, broad , layer by layer
    # iterative BFT
    # - create queue
    # - add root to queue
    # - while queue is not empty
    #     - node = pop head of queue
    #     - DO THE THING!!! (print)
    #     - add children of root to queue

    def bft_print(self, node):
        # create queue
        q = Queue()
        # add root to queue
        q.enqueue(node)
        # while queue is not empty
        while q.size > 0:
            # node = pop head of queue (node is the argument choose different var name to avoid confusion)
            popped = q.dequeue()
            # DO THE THING! (print)
            print(popped.value)
            # add children of root to queue
            if popped.left:
                q.enqueue(popped.left)
            if popped.right:
                q.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Depth first traversal -  keep going one direction until you no longer can
    # iterative DFT
    # - create stack
    # - add root to stack
    # - while stack is not empty
    #     - node = pop top of stack
    #     - DO THE THING!!! (print)
    #     - add children of node to stack
    def dft_print(self, node):
        # create stack
        stack = Stack()
        # add root to stack
        stack.push(node)
        # while stack is not empty
        while stack.size > 0:
            # node = pop top of stack
            popped = stack.pop()
            # DO THE THING! (print)
            print(popped.value)
            # add children of node to stack
            if popped.left:
                stack.push(popped.left)
            if popped.right:
                stack.push(popped.right)
        return
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#* first attempt. runs faster, but reading the readme suggest I should use a binary search tree to search. worst case runtime for below fn is O(n^2)
# duplicates = [x for x in names_1 if x in names_2] 
 # Return the list of duplicates in this data structure
duplicates = []
#* the runtime for the below fn is (n^2)
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#Instantiate BinarySearchTree with first name in list
bst = BinarySearchTree(names_1[0])
#Add the rest of the names with insert
for name in names_1[1:]:
    bst.insert(name)
# if a name in names_2 is the same append it to the list
for same in names_2:
    if bst.contains(same):
        duplicates.append(same)
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
