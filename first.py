print("first")
print("Age Checker Program")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 0:
    print("Wrong age!")

elif age < 13:
    print("You are a child")

elif age < 18:
    print("You are a teenager")

else:
    print("You are an adult")

print("Hello", name)

print("second")
print("Rectangle Animation")
print("-------------------")
width = int(input("Enter rectangle width: "))
height = int(input("Enter rectangle height: "))
if width < 2 or height < 2:
    print("Invalid dimensions!")
else:
    for i in range(height):
        for j in range(width):
            print("*", end=" ")
        print()

print("third")
import time
import msvcrt

print("Project 03 - While Loop")
print("------------------------")

count = 0

while True:
    count = count + 1

    print("\nProject Report")
    print("----------------")
    print("Project: Python")
    print("Loop: While")
    print("Report Number:", count)
    print("Status: Running")
    print("----------------")

    print("Press any key to stop the program...")

    for i in range(10):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            break

        time.sleep(0.1)
    else:
        continue

    break

print("\nProgram Stopped!")
print("Total Reports:", count)

