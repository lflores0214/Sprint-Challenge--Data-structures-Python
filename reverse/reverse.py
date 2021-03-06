class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # to reverse a list you have to move pointers
        # cant use loops
        # base case
        # if there is no head return None
        if node == None:
            return
        # check if the node has a next
        if node.next_node == None:
            # if it doesn't then we reached the end of the list and we want to set the head to that node
            self.head = node
            # we also want to set the next to the previous node
            node.next_node = prev
            return
        # create pointers
        # next becomes next_node so we can pass that into the fn 
        temp = node.next_node
        # set the next node of current node to prev
        node.next_node = prev
        # do the same for each node in the list
        self.reverse_list(temp, node)
