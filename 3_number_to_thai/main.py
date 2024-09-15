"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        #Verify number can not less than 0
        if int(number) < 0:
            return "number can not less than 0"
        
        #Thai number list
        thai_number_list = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

        #Thai digit list
        Thai_digit_list = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

        #Check value
        str_number = str(number)[::-1]
        result = ""

        #Convert Value
        for index, value in enumerate(map(int, str_number)):
            if value:
                if index:
                    result = Thai_digit_list[index] + result

                if len(str_number) > 1 and value == 1 and index == 0:
                    result += 'เอ็ด'
                elif index == 1 and value == 2:
                    result = 'ยี่' + result
                elif index != 1 or value != 1:
                    result = thai_number_list[value] + result

        #print("result : ", result)
        return result


        pass

solution = Solution()

#Input 
number = int(input("Enter a number : "))

#Call Function
print("string of thai number call :", solution.number_to_thai(number))