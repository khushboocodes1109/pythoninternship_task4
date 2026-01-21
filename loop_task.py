code
"""
TASK 4: Loops & Iterations
Python Developer Internship
"""

# 1. Print numbers from 1 to 100 using for loop
print("1. Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n" + "-" * 40)


# 2. Countdown timer using while loop
print("2. Countdown Timer:")
count = 10
while count > 0:
    print(count)
    count -= 1
print("Countdown finished!")
print("-" * 40)


# 3. Demonstration of break and continue
print("3. Break and Continue Example:")
for num in range(1, 11):
    if num == 5:
        continue   # skips 5
    if num == 8:
        break      # stops loop at 8
    print(num)
print("-" * 40)


# 4. Iterating over string characters
print("4. Iterating over a string:")
name = "Python"
for char in name:
    print(char)
print("-" * 40)


# 5. Multiplication table
print("5. Multiplication Table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print("-" * 40)


# 6. Using range with steps
print("6. Numbers from 0 to 20 with step 2:")
for i in range(0, 21, 2):
    print(i, end=" ")
print("\n" + "-" * 40)


# 7. Loop with conditions
print("7. Even numbers between 1 and 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print("\n" + "-" * 40)


# 8. Real-world example: Checking pass/fail
print("8. Student Result Check:")
marks = [45, 67, 89, 32, 76]
for mark in marks:
    if mark >= 40:
        print(mark, "- Pass")
    else:
        print(mark, "- Fail")

print("\nTask 4 completed successfully!")
