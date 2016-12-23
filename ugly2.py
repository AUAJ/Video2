#!/usr/bin/python

# Fix me!

def StudentInfo():
    name = raw_input("Enter name: ")
    age = input("Enter age: ")
    grade1 = int(input("Enter marks for subject 1: "))
    grade2 = int(input("Enter marks for subject 2: "))
    grade3 = int(input("Enter marks for subject 3: "))
    sum_ = grade1 + grade2 + grade3
    avg = sum_ / 3

    print("Hello " + name + " you are " + str(age) + " years old")
    print("Your total marks are: " + str(sum_))
    print("Your average marks are: " + str(avg))

if __name__ == '__main__':
    for x in range(0,3): 
        StudentInfo()
        
