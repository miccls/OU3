"""
Student:
Mail:
Reviewed by:
Date reviewed:
"""

from unittest.loader import defaultTestLoader


class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

        def length(self):
            '''Method returning number of
            nodes after this one'''
            if self.succ is None:
                return 1
            else:
                return 1 + self.succ.length()

        def insert(self, x):
            '''Inserts element x in list of
            nodes
            '''  
            if self.succ is None or x <= self.succ.data:
                # Creating instance of Node.
                self.succ = self.__class__(x, self.succ)
            else:
                self.succ.insert(x)
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def _count(self, x ,f):
        if f.succ is None:
            return (f.data == x)
        else:
            return (f.data == x) + self._count(x, f.succ)

    def count(self, x):
        return self._count(x, self.first)

    def insert(self, x):
        
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            self.first.insert(x)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    
    # To be implemented
    
    def length(self):
        '''Method returning list length'''             # Optional
        if self.first is None:
            return 0
        else:
            return self.first.length()

  
  
    def mean(self):               # Optional
        '''Method calculating mean of list elements'''
        f = self.first
        numOfElements = 0
        totSum = 0
        while f:
            totSum += f.data
            numOfElements += 1
            f = f.succ

        return totSum/numOfElements

    
    
    def remove_last(self):        # Optional
        '''Method removing last element of list'''
        f = self.first
        if not f or not f.succ:
            if f:
                data = f.data
                self.first = None
                return data
            return None
        else:
            prev = None
            while f.succ:
            #    print(f.data)
                prev = f
                f = f.succ
            prev.succ = None
            return f.data  
    
    '''
    def remove(self, x, f):
        if f.succ:
            if f.succ.data == x:
                f.succ = f.succ.succ
                return True
            else: return self.remove(x, f.succ)
        return False
        
    '''
    
    def remove(self, x):          # Compulsory
        f = self.first
        # First check if first is x
        if f and f.data == x:
            self.first = f.succ
            return True

        while f:
            if f.succ and f.succ.data == x:
                       f.succ = f.succ.succ
                       return True
            f = f.succ
        return False
    


    def _to_list(self, f):
        if not f:
            return []
        else:
            return list((f.data, *self._to_list(f.succ),))
    
    def to_list(self):            # Compulsory
        return self._to_list(self.first)

    
    def _remove_all(self, x, f):
        if not self.remove(x):
            return
        else:
            self._remove_all(x, f)

        
    def remove_all(self, x):      # Compulsory
        self._remove_all(x, self.first)
    
    
    def __str__(self):            # Compulsory

        # Dont know which of these is optimal. 
        # I just went with the shortest one. 
        #return str(tuple([e for e in self]))
        
        # Maybe this one is the fastest actually
        # s = ""
        # for e in self:
        #     s + str(e) 
        # # Compensate for last ', '.
        # return '(' + e[:-2] + ')'

        return "(" + ", ".join((str(e) for e in self)) + ")"
    
    
    def merge(self, lst):         # Compulsory
        '''Recursive method merging two
        objects of the LinkedList class
        '''
        e = lst.remove_last()
        if e:
            self.insert(e)
            self.merge(lst)
        else:
            return
    
    
    def __getitem__(self, ind):   # Compulsory
        i = 0
        for e in self:
            if i == ind:
                return e
            i += 1

    def __setitem__(self, key, value):
        raise TypeError('LinkedList does not support index assignment')



class Person:                     # Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __lt__(self, prsn):
        return True if self.pnr > prsn.pnr else False

    def __le__(self, prsn):
        return True if self.pnr >= prsn.pnr else False

    def __eq__(self, prsn):
        return True if self.pnr == prsn.pnr else False

def main():
    lst = LinkedList()
    for x in [6,6,6,6, 6]:
        lst.insert(x)
    
    # Test code:
    # print(lst.insert(120))
    # print(lst.length())
    # print(lst.count(120))
    print(lst.remove_all(6))

    print(lst.to_list())

    # lst2 = LinkedList()
    # for x in [1, 12, 3 ,545, 4, 90]:
    #     lst2.insert(x)
    # lst.merge(lst2)
    # print(lst[4], lst[9])
    # lst[3] = 1

    for x in [Person('Martin', 19990821), Person('Izza', 19980917), Person('Claes', 19600305)]:
        lst.insert(x)
    print(lst)


if __name__ == '__main__':
    main()
    


    

