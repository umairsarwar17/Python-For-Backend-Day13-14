age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
elif age > 0:
    print("You are not eligible to vote yet.")
else:
    print("Invalid age entered.")
#.............Nested Conditions
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Number is not positive")
#.........Short-Hand if/else (Ternary Operator)
age = int(input("Enter your age: "))
print("Adult") if age >= 18 else print("Minor")
'''Logical Operators in Conditions
and
or
not
'''
marks = int(input("Enter your marks: "))
if marks >= 80 and marks <= 100:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
