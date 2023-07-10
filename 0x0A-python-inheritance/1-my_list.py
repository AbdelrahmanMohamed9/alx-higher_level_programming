#!/usr/bin/python3
''' that create a class MyList derived from list '''


class MyList(list):
    ''' that inherit the attributes references of class list
    Args:
        list: that class list
    '''
    def print_sorted(self):
        ''' taht print the sorted list '''
        print(sorted(self))
