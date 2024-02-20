class MyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def display(self):
        print(self.items)

my_list = MyList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()

class MyList:
    def __init__(self):
        self.items = []

    def extend(self, iterable):
        self.items += iterable

    def display(self):
        print(self.items)

my_list = MyList()
my_list.extend([1, 2, 3])
my_list.extend(["a", "b", "c"])
my_list.display() 

class MyList:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def __add__(self, other):
        if isinstance(other, MyList):
            return MyList(self.items + other.items)
        elif isinstance(other, list):
            return MyList(self.items + other)
        else:
            raise TypeError("Unsupported operand type")

    def display(self):
        print(self.items)

list1 = MyList([1, 2, 3])
list2 = MyList(["a", "b", "c"])
result_list = list1 + list2
result_list.display() 

class MyList:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def pop(self, index=None):
        if index is None:
            if not self.items:
                raise IndexError("pop from empty list")
            return self.items.pop()
        else:

            try:
                return self.items.pop(index)
            except IndexError:
                raise IndexError("pop index out of range")

    def display(self):
        print(self.items)

my_list = MyList([1, 2, 3, 4, 5])

popped_item = my_list.pop()
print("Popped item:", popped_item)  
my_list.display()  

popped_item_at_index = my_list.pop(1)  
print("Popped item at index 1:", popped_item_at_index)  
my_list.display()

class MyList:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def clear(self):
        self.items = []

    def display(self):
        print(self.items)

my_list = MyList([1, 2, 3, 4, 5])
my_list.clear()
my_list.display()

class MyList:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def insert(self, index, item):
        self.items.insert(index, item)

    def display(self):
        print(self.items)
my_list = MyList([1, 2, 3, 5])
my_list.insert(3, 4)
my_list.display()  
my_list.insert(0, 0) 

class MyList:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def remove(self, item):
        try:
            self.items.remove(item)
        except ValueError:
            raise ValueError(f"{item} not in list")

    def display(self):
        print(self.items)

my_list = MyList([1, 2, 3, 4, 5])

my_list.remove(3)  
my_list.display()  

try:
    my_list.remove(7)
except ValueError as e:
    print(e)  
 


