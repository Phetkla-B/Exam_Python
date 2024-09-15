"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        #Verify non-negative data
        if number < 0:
            return "number can not be negative"
        
        #Find zeroes factorial
        count = 0
        divisor = 5
        while number >= divisor:
            count += number // divisor
            divisor *= 5

        return count
        
        pass

solution = Solution()

#Input 
number = int(input("Enter a number : "))

#Call Function
print("count of tailing zero as an integer :", solution.find_tailing_zeroes(number))