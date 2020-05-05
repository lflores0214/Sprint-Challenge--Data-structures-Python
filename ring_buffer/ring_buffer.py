from doubly_linked_list import DoublyLinkedList
# Reading through the problem and looking at the example. this is similar to an LRU cache


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # append adds elements to buffer
        # like and lru cache the nodes cannot exceed the capacity
        # in this case the oldest element should be overwritten by the new element

        # check if buffer is at capacity
        if self.storage.length < self.capacity:
            # check if theres anything at the head
            if self.storage.head == None:
                # if there isn't you can add the item there
                self.storage.add_to_head(item)
                # self.current becomes the head
                self.current = self.storage.head
            else:  # if there is something at the head but still has room add it to the tail
                self.storage.add_to_tail(item)
        else:  # if the buffer is at capacity
            # check if current has a next
            if self.current.next:
                # if there is a next replace the value of the current item with the new one
                self.current.value = item
                # move current to the next item
                self.current = self.current.next
            else:  # if there is no next
                # replace current value with item
                self.current.value = item
                # the current item becomes the head
                self.current = self.storage.head

    def get(self):
        # returns all elements in the buffer in their given order
        # it should not return any None values in the list even if they are present in the ring buffer
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        # start at the beginning of the list
        item = self.storage.head
        # while item is not None
        while item:
            # add the value of item to the list
            list_buffer_contents.append(item.value)
            # increment to next to add the next item
            item = item.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
