class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # wrap value into Node to be inserted into tree
        new_node = BSTNode(value)

        """
        # should I check if this value is already in the tree?
        # if it's in the tree return none
        if self.contains(value):
            return None
        """
        # compare value to root for placement
        if value < self.value:
            # check self.left, if no value, place there
            if not self.left:
                self.left = new_node
            # else continue to find next empty spot.
            else:
                self.left.insert(value)
        else:
            # this will currently set equal values to the right property
            # for dupe_insert_test
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        BSTNode(target)
        value = self.value
        # start searching at root,
        if target is value:
            return True
        # compare target again self
        # choose a direction based
        # on compared value
        # reiterate until target matches self,
        # or we hit a leaf
        if target < value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # I already know that the max
        # value should be the most right value

        # check if self exists
        if not self:
            return None
        # hold the current value that is higher
        current_max = self
        # continues to get the right value, until self.value is none
        while current_max.right is not None:
            # set the max value to var to return value
            current_max = current_max.right
        return current_max.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # wrap function with current value
        fn(self.value)
        # helps find end of for each function
        if not self:
            return None
        if self.left or self.right:
            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)
