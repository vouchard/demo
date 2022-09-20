'''
Assume you have an array as follows: [2, 3, 5, 7, 9, 11]. Find the two numbers from the array
that will give you a total of 9.
Input: [2, 3, 5, 7, 9, 11]
Output: [2, 7]

'''

class ListOfNumbers():
    def __init__(self,target_number,array_of_numbers):
        self.target = target_number
        self.array_of_numbers = array_of_numbers

    @property
    def sum_of_two(self):
        pair_of_numbers = []
        for first_number in self.array_of_numbers:
            second_number = self.target - first_number

            if second_number in self.array_of_numbers:
                pair_of_numbers.append(first_number)
                pair_of_numbers.append(second_number)
                break
        return pair_of_numbers    


#Sample Run
print(ListOfNumbers(target_number=9,array_of_numbers=[2, 3, 5, 7, 9, 11]).sum_of_two)




