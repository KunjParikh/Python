##P1 : Implementation of reversing a string using concepts of class. And internal functioning of for .. in .. .
#Defination:
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
##Usage:
rev = Reverse('spam')
for char in rev:
  print char

##End of piece P1


