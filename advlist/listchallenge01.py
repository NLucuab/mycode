#!/usr/bin/env python3
wordbank = ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

num = int(input("Please enter a number between 0 and 20: "))

student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent")


