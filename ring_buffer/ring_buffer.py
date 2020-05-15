# a queue with a size limit
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = 0

    '''
    Adds an item to the ring buffer in order,
    if max capacity is reached,
    the item replaces the oldest object
    '''
    # O(n) ?

    def append(self, item):
        # check current item list
        # if it is lower
        if len(self.storage) < self.capacity:
            # add the item to our queue/list
            self.storage.append(item)
        # else if it is greater
        else:
            # reseting where to place next index counter
            if self.count == self.capacity:
                self.count = 0
            # swap out item in the index that matches count
            # with new item
            self.storage[self.count] = item
            self.count += 1

        # stretch:
        # update this into a linked list

    def get(self):
        return self.storage
