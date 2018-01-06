class Vector(object):
    def __init__(self, elements):
        self.elements = elements
    def __add__(self, other):
        if isinstance(other, Vector):
            