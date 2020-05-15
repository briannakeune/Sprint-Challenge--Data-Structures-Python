import time
# from bst import BSTNode

# a bug I came across, was in my BSTNode when checking the target vs the value
# it was *is* which worked within it's self,
# but after changing it to == to check if the values were equal
# it was successful


class BSTNode:

    def __init__(self, value=None):
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
        if target == value:
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

    def in_order_print(self, node):
        # the lowest value will be the most left
        # while the highest value will be the most right
        # so using a stack approach LIFO...
        # we travel down all the left options, then right right options

        if self.left:
            # when the recursion start it creates a new instance
            # of all these lines of code on the newly passed in node
            # when the new node's set of function lines ends,
            # we revert back to the parent node's function where it left off
            self.left.in_order_print(self.left)
        # and that's how it can print the parent nodes
        print(self.value)
        # then travel to the right
        if self.right:
            self.right.in_order_print(self.right)


# original runtime is O(n²)
# new runtime is O(n)
# also I still need practice with naming runtimes

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
duplicates = [i for i in (set(names_1).intersection(names_2))]

# # creating a binary tree with M as the root node
# # i chose m because it's the middle of the alphabet
# bst = BSTNode('M')
# # inserting all names for name_1 list into my binary tree
# for name in names_1:
#     bst.insert(name)
# # then for each name in name_2 we
# # search the bst for a value that is equal
# for name_2 in names_2:
#     if bst.contains(name_2):
#         # if value is equal append
#         duplicates.append(name_2)
# # this helps runtime because I do not have to search
# # both lists with a variable amount of indexes through each index
# # also because I chose a binary tree, it will only have to search
# # half of the alpabet names, rather than every single name in the original list

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
