"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        #Verify number can not less than 0
        if number < 0:
            return "number can not less than 0"
        
        #Number List
        num = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4, 1]
        
        #Roman List
        roman = ["M", "CM", "D", "CD",
                 "C", "XC", "L", "XL",
                 "X", "IX", "V", "IV", "I"]
        
        number_roman = ""

        i = 0

        #Convert Value
        while number > 0:
            for _ in range(number // num[i]):
                number_roman += roman[i]
                print("number_roman : ", number_roman)

                number -= num[i]
                print("number : ", number)

            i += 1

        return number_roman

        pass

solution = Solution()

#Input 
number = int(input("Enter a number : "))

#Call Function
print("Roman number is :", solution.number_to_roman(number))
