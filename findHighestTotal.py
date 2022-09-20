'''
    Assume a 2D array = [[2], [3, 5], [6, 7, 8], [7, 3, 5, 9]] to be a pyramid
    2
    35
    678
    7359
    Assume each path as the following:
    1. 2 + 3 + 6 + 7
    2. 2 + 3 + 6 + 3
    3. 2 + 3 + 6 + 5
    4. 2 + 3 + 6 + 9
    5. 2 + 3 + 7 + 7
    Etc..
    Write a pseudo code to find the path that has the highest total and return an array of the
    numbers.
    Input: [[2], [3, 5], [6, 7, 8], [7, 3, 5, 9]]
    Output: [2, 5, 8, 9].
'''

class ArrayPyramid():
    def __init__(self,array_2d):
        self.array_2d = array_2d
        
    @property
    def highest_total(self):
        lst = []
        for element in self.array_2d:
            lst.append(max(element))
        return lst

##TEST CODE
print(ArrayPyramid(array_2d=[[2], [3, 5], [6, 7, 8], [7, 3, 5, 9]]).highest_total)
        