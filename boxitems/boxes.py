# Write an “abstract” class, Box, and use it to define some methods which any box object should have: add,
# for adding any number of items to the box, empty, for taking all the items out of the box and returning
# them as a list, and count, for counting the items which are currently in the box. Write a simple Item
# class which has a name attribute and a value attribute – you can assume that all the items you will use
# will be Item objects. Now write two subclasses of Box which use different underlying collections to store
#  items: ListBox should use a list, and DictBox should use a dict. Write a function, repack_boxes, which
#  takes any number of boxes as parameters, gathers up all the items they contain, and redistributes them as
#  evenly as possible over all the boxes. Order is unimportant. There are multiple ways of doing this. Test
#  your code with a ListBox with 20 items, a ListBox with 9 items and a DictBox with 5 items. You should end
#   up with two boxes with 11 items each, and one box with 12 items. Use proper Exception Handling where it is required.

from abc import ABC, abstractmethod


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Box(ABC):

    @abstractmethod
    def add(self):
        raise NotImplementedError

    @abstractmethod
    def empty(self):
        raise NotImplementedError

    @abstractmethod
    def view_and_count(self):
        raise NotImplementedError


class ListBox(Box):
    def __init__(self):
        self.count = 0
        self.listitem = []

    # Add the item object to ListBoxclass
    def add(self, *item):

        self.listitem.extend(item[0])

    # Returns the list of items contained in the ListBox
    def empty(self):
        list = self.listitem
        self.listitem = []
        return list

    # Fuction to view the items build for my own conveneince
    def view_and_count(self):
        print(f"There are total {len(self.listitem)} items "
              f"in {self.__class__} : {[(i.name,i.value) for i in self.listitem]}")


class DictBox(Box):

    def __init__(self):
        self.dictitem = {}

    #Add the item object to dictclass
    def add(self, *item):

        self.dictitem.update(dict((i.name,i) for i in item[0]))

    #Returns the list of items contained in the dictbox
    def empty(self):
        list = [i for i in self.dictitem.values()]
        self.dictitem = {}
        return list

    #Fuction to view the items build for my own conveneince
    def view_and_count(self):
        print(f"There are total {len(self.dictitem.items())} items in {self.__class__} : { dict([(i.name,i.value) for i in self.dictitem.values()]).items() }")


def repack(*box):
    box_items = []
    for b in box :
        box_items.extend(b.empty())

    print(box_items)


    #Loop will execute till the box_items is not getting empty

    while box_items:

        #if it contains the item then we will insert the item in the different boxes by popping one by one and adding it
        for boxes in box:

            try:
                item = box_items.pop()  #This can throw exception if we are popping element from the empty list so we can take care by keeping it inside try catch block
                boxes.add([item])

            except IndexError:
                print("We are popping from empty list")
                break










# itemlist = [Item('box1', 10), Item('box2', 20),Item('box3', 30),Item('box4', 40),Item('box5', 50),Item('box6', 60),\
#             Item('box7', 70), Item('box8', 80),Item('box9', 90),Item('box10', 100), Item('box11', 110),Item('box12', 120),\
#             Item('box13', 130),Item('box14', 140),Item('box15', 150),Item('box16', 160)]


item1 = [Item(str(i), i) for i in range(20)]


item2 = [Item(str(i), i) for i in range(9)]


item3 = [Item(str(i), i) for i in range(5)]



l1 = ListBox()
l1.add(item1)
l2 = ListBox()
l2.add(item2)
d1 = DictBox()
d1.add(item3)


l1.view_and_count()
l2.view_and_count()
d1.view_and_count()

repack(l1,l2,d1)

l1.view_and_count()
l2.view_and_count()
d1.view_and_count()
