#!/usr/bin/python3
'''Rectangle - defines and instance of a Rectangle requiring
2 parameters of type int (height, and width).

This module will raise TypeError if paramaters are not
of type int, and will raise ValueError if less than 0.

__str__() - Returns visual representation of a Rectangle()
based on height and width dimensions.
__repr__() - Returns string representation of the rectangle
to be able to recreate a new instance by using eval().
__del__() - Print confirmation upon successful deletion of an object.
area() - Returns the rectangle area.
perimeter() - Returns the rectangle perimeter.
'''


class Rectangle():
    '''class Rectangle - Parameters(width(int), height(int))'''

    def __init__(self, width=0, height=0):
        ''' Constructor '''
        self.width = width
        self.height = height

    def __str__(self):
        ''' Overload __str__ to print rectangle. '''
        if self.__width == 0 or self.__height == 0:
            return ''
        # Build a visual representation of the rectangle
        b = ('#' * self.__width + '\n') * self.__height
        # Return the rectangle after stripping the trailing newline.
        return (b.strip('\n'))

    def __repr__(self):
        ''' Overload __repr__ to return string. '''
        return("Rectangle(%d, %d)" % (self.__width, self.__height))

    def __del__(self):
        ''' On delete print confirmation. '''
        print("Bye rectangle...")

    @property
    def width(self):
        ''' Getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Setter '''
        if isinstance(value, int):
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        ''' Getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Setter '''
        if isinstance(value, int):
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
        else:
            raise TypeError('height must be an integer')

    def area(self):
        ''' Returns the rectangle area '''
        return self.__width * self.__height

    def perimeter(self):
        ''' Returns the rectangle perimeter. '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
