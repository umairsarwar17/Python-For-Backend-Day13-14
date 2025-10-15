'''
Check voting eligibility
Find the largest of 3 numbers
Simple Calculator
Even or Odd Checker
Price Discount Calculator
Time-based Greeting
Employee Bonus Calculator
'''
#...........
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#............
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the largest number")
elif b >= a and b >= c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")
#..........
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    print("Result:", num1 / num2)
else:
    print("Invalid operator")
#.........
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#............
'''
Ask for a product price and apply discounts:
Above 500 → 20% off
200–500 → 10% off
Below 200 → No discount
'''
price = float(input("Enter product price: "))

if price > 500:
    discount = 0.20
elif price >= 200:
    discount = 0.10
else:
    discount = 0

final_price = price - (price * discount)
print(f"Final price after discount: {final_price}")
#....................
hour = int(input("Enter hour (0–23): "))

if hour < 12:
    print("Good Morning!")
elif hour < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")
#........
'''
If salary > 50,000 → 10% bonus
If 30,000–50,000 → 5% bonus
Else → 2% bonus
'''
salary = float(input("Enter your salary: "))

if salary > 50000:
    bonus = 0.10
elif salary >= 30000:
    bonus = 0.05
else:
    bonus = 0.02

print("Bonus:", salary * bonus)
print("Total Salary:", salary + (salary * bonus))
