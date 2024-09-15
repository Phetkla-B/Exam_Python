"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        #Check null
        if not numbers:
            return "list can not blank"
        
        #Find Max value
        max_value = max(numbers)
        return numbers.index(max_value)
        pass


solution = Solution()

#input test
numbers = [1,2,1,3,5,6,4]
output = solution.find_max_index(numbers)
print(f"index of maximum number in list = {output}")

#input test null
numbers = []
output = solution.find_max_index(numbers)
print(f"index of maximum number in list = {output}")