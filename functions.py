# 1. Write a Python function called max_num()to find the maximum of three numbers.
def max_num(n1,n2,n3):
    return max(n1,n2,n3) # max() is a build in function 
   
print(max_num(10,52,36))

# 2. Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(nums):
    if len(nums) == 0:
        return 0
    mult = nums[0]
    if len(nums)>1:
        for n in nums[1:]:
            mult = mult * n
    return mult

print(mult_list([5,2,3]))


# 3. Write a Python function called rev_string() to reverse a string.
def rev_string(txt):
    return txt[::-1]
print(rev_string("Hello World"))

# 4. Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(num, r1, r2):
    if num in range(r1,r2+1):
        print ("in range")
    else:
        print("not in range")
num_within(7,1,4)   


# 5. Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    triangle = [[1],[1,1]]
    if n < 1:
        print("Invalid")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(row)

pascal(5)