""" bst.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""


from linked_list import LinkedList
import time
import random

class BST:
    
    class Node:     
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
        
        def __iter__(self):     # Discussed in the text on generators
            if self.left:            
                yield from self.left
            yield self.key             
            if self.right:        
                yield from self.right

        def smallest(self):
            if self.left:
                return self.left.bottom('right')
            else:
                return self.key
        
        def largest(self):
            if self.right:
                return self.right.bottom('right')
            else:
                return self
        
        def bottom(self, side):
            if side == 'right':
                return self if not self.right else self.right.bottom('right')
            else:
                return self if not self.left else self.left.bottom('left')
            
        def contains(self, a):
            return self._contains(self, a)
    
        def _contains(self, r, a):
            if r:
                if r.key == a:
                    return True
                else:
                    return self._contains(r.left, a) if r.key > a else self._contains(r.right, a)
            else:
                return False


    def __init__(self, root=None):
        self.root = root
        
        
    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root
    

   
    # def insert(self, key):
    #     self.root = self._insert(self.root, key)
  
  
    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass # Already there
        return r


    def insert(self, key):
        '''Iterative insert method for
        the BST.
        '''
        r = self.root
        if not r:
            self.root = self.Node(key)
        rol = ''
        while r:
            if key < r.key:
                rol = 'left'
            elif key > r.key: 
                rol = 'right'
            else:
                return
            if getattr(r, rol):
                r = getattr(r, rol)
            else:
                setattr(r, rol, self.Node(key))
                return
                # Already there.
        # If None is encountered, fill the node
        


    def print(self):
        self._print(self.root)
    
    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)


    # def contains(self, k):
    #     n = self.root
    #     v = 1
    #     while n and n.key != k:
    #         if k < n.key:
    #             n = n.left
    #         else:
    #             n = n.right
    #         v += 1
    #     return n is not None, v if n else None

    

    # def _contains(self, r, k):
    #     if r and r.key != k:
    #         return self._contains(r.left, k) or self._contains(r.right, k)
        
    #     return r is not None


    # def contains(self, k):
    #     return self._contains(self.root, k)

    
    def size(self):
        return self._size(self.root)
    
    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#
    def _height(self, r):
        if not r:
            return 0
        else:
            return 1 + max(self._height(r.left), self._height(r.right))


    def height(self):                             # Compulsory
        return self._height(self.root)
        
    

    
    def remove(self, key):                           
        self.root = self._remove(self.root, key)
    
    def _remove(self, r, k):                            # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
        elif k > r.key:
            r.right = self._remove(r.right, k)
        else: # This is the key to be removed       
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case  
                return r.left
            else: # This is the tricky case.
                # Smallest in right tree replaces.
                r.key = r.right.smallest().key
                r.right = self._remove(r.right, r.key)
                     # Find the smallest key in the right subtree
                     # Put that key in this node
                     # Remove that key from the right subtree
        return r # Remember this! It applies to some of the cases above
    

    
    def __str__(self):                           # Compulsory
        '''String method to be able to print
        representation of string.
        '''
        nums = ', '.join(str(num) for num in self)
        return f'<{nums}>'
    
    
    def to_list(self):                            # Compulsory
        '''Vad är komplexiteten av denna metod?
        Jag vill mena att komplexiteten är O(n).
        Detta då man itererar över trädet där man
        med den metod vi använder 'hittar rätt' vid 
        varje iteration, man behöver inte leta upp något från början
        igen.
        '''

        return [num for num in self]

    
    
    def to_LinkedList(self):                      # Compulsory
        '''Vad är komplexiteten av denna metod?
        Här är komplexiteten för iterationen fortfarande
        O(n) Men i värsta fall så är insert operationen också O(n)
        Detta ger då O(n^2)
        '''
        lst = LinkedList()
        for num in self:
            lst.insert(num)
        return lst
    
    def _ipl(self, r, level = 1):
        if not r:
            # Base case of the recursion
            return 0
        else:
            return level + self._ipl(r.left, level + 1)\
            + self._ipl(r.right, level + 1)


    def ipl(self):                                # Compulsory
        '''Method returning the internal path lenght
        using recursion.
        '''
        return self._ipl(self.root)
    
    def LCA(self, a, b):
    
        return self._LCA(self.root, a, b)

    def _LCA(self, r, a, b):
        if r:
            if r.left:
                a_in_left = r.left.contains(a)
                b_in_left = r.left.contains(b)
            if r.right:
                a_in_right = r.right.contains(a)
                b_in_right = r.right.contains(b)
            if a_in_left and b_in_left:
                return self._LCA(r.left, a, b)
            elif a_in_right and b_in_right:
                return self._LCA(r.right, a, b)
            elif (a_in_left and b_in_right) or (b_in_left and a_in_right):
                return r.key
            else:
                return None

    
    
def random_tree(n):                               # Useful
    t = BST()
    while t.size() < int(n):
        t.insert(round(random.random(), 6))
    return t





def main():
    t = BST()
    for x in [5,8,6,3,7,2,8,1,9]:
        t.insert(x)
    print(t.LCA(9,7))
    


    # print('size  : ', t.size())
    # for k in [0, 1, 2, 5, 9]:
    #     print(f"contains({k}): {t.contains(k)}")

    # Test code below:
    # print(t.height())
    # t.remove(6)
    # t.print()
    # print()
    # print(t.height())
    # #print(t)
    # start = time.perf_counter()
    # lst = t.to_LinkedList()
    # print(time.perf_counter() - start)
    # start = time.perf_counter()
    # lst2 = t.to_list()
    # print(time.perf_counter() - start)
    #print(t.ipl())1000

    # Code to time search in tree of size n.

    # n1 = input("Ge storlek: ")
    # bst = random_tree(n1)
    #Now we want to verify that the number of node visits depends
    #on the following formula --> N = 1.39*log2(n) + O(1). So in our case N = 1.39*log2(1000) approximatley = 14

    # node_visits = 0
    # n = 50000
    # n_succ = 0
    # avg_v = 0
    # for _ in range(30):
    #     bst = random_tree(n1)
    #     n_succ = 0
    #     node_visits = 0
    #     for n2 in range(n):
    #         i = round(random.random(), 6)
    #         success, search_result = bst.contains(i)
    #         if success:
    #             node_visits += search_result
    #             n_succ += 1
    #     avg_v += node_visits/n_succ
    # # Prints the average number of visits after 50000 searches in 30 different trees of the same size 
    # # Does not yield exactly what the formula says, a bit lower.
    # print((avg_v + 30)/30)
    



if __name__ == "__main__":
    main()
    
    
    
    
    
"""
What is the genertor good for?
==============================

1. computing size? Yes, one could do it like this, return len[n for n in tree]
2. computing height? Difficult as the generator does not keep track of level
3. contains? Sure -> return any([n == k for n in tree]) if k is the value to be searched
4. insert? Also difficult as you are only given the key and not the reference to the Node itself
5. remove? -||-




Results for ipl of random trees
===============================



13.05 for tree of 1000 elements.


"""