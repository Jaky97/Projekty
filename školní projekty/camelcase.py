def sumOfNums(x, y):
    return x + y
print(sumOfNums(3, 5))
print(sumOfNums(3.11, 5))
print(sumOfNums("Čau", "Vole!"))
print(sumOfNums(3, sumOfNums(5,7)))

print( "\n \n \n \n" )
print("Je tu mezera?")

#5 -14 9 -6
s = sumOfNums
p = print

p(s(s(5, -14,), s(9, -6)))

def sumOfNuns2(*nums):
    return sum(nums)