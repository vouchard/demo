from findHighestTotal import ArrayPyramid
from longestNonRepeating import String_Of_Chars
from totalOfNine import ListOfNumbers

#TEST QUESTION 1
def test_q1_a():
    input_list = [[2], [3, 5], [6, 7, 8], [7, 3, 5, 9]]
    expected_res = [2, 5, 8, 9]
    ans = ArrayPyramid(array_2d=input_list).highest_total
    assert ans == expected_res

def test_q1_b():
    input_list = [[2], [3, 9], [6, 7, 9], [7, 3, 5, 9]]
    expected_res = [2, 9, 9, 9]
    ans = ArrayPyramid(array_2d=input_list).highest_total
    assert ans == expected_res

def test_q1_c():
    input_list = [[2], [3, 6], [6, 7, 2], [7, 3, 5, 6]]
    expected_res = [2, 6, 7, 7]
    ans = ArrayPyramid(array_2d=input_list).highest_total
    assert ans == expected_res    



#TEST QUESTION 2
def test_q2_a():
    input_list = [5,2,4,6,1]
    target = 9
    expected_res = [5,4]
    ans = ListOfNumbers(target_number=target,array_of_numbers=input_list).sum_of_two
    assert ans == expected_res

def test_q2_b():
    input_list = [5,3,2,6,8]
    target = 9
    expected_res = [3,6]
    ans = ListOfNumbers(target_number=target,array_of_numbers=input_list).sum_of_two
    assert ans == expected_res

def test_q2_c():
    input_list = [5,2,6,1,7,8]
    target = 9
    expected_res = [2,7]
    ans = ListOfNumbers(target_number=target,array_of_numbers=input_list).sum_of_two
    assert ans == expected_res 


#TEST QUESTION 3
def test_q3_a():
    input_str = 'abcabcdbb'
    expected_res = 'abcd'
    ans = String_Of_Chars( string_to_eval=input_str).longestSubstring
    assert ans == expected_res

def test_q3_b():
    input_str = 'abcabcdbbasdfghj'
    expected_res = 'basdfghj'
    ans = String_Of_Chars( string_to_eval=input_str).longestSubstring
    assert ans == expected_res

def test_q3_c():
    input_str = 'abcghjrabcdbb'
    expected_res = 'ghjrabcd'
    ans = String_Of_Chars( string_to_eval=input_str).longestSubstring
    assert ans == expected_res

def test_q3_d():
    input_str = 'abcaabbccddbb'
    expected_res = 'abc'
    ans = String_Of_Chars( string_to_eval=input_str).longestSubstring
    assert ans == expected_res        