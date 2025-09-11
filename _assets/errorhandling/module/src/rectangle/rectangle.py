class Rectangle:
    """A class to represent a rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def set_width(self, width):
        """Set the width of the rectangle"""
        self.width = width

    def set_height(self, height):
        """Set the height of the rectangle"""
        self.height = height


# Standalone function in the module
def is_square(rectangle: Rectangle):
    """
    Check if a given rectangle is a square.
    
    This function is not part of the Rectangle class, 
    but it operates on a Rectangle object.
    """
    return rectangle.width == rectangle.height
