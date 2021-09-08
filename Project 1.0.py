#!/usr/bin/env python
# coding: utf-8

# # student portfolio

# In[ ]:


print("Enter the details")
name = str(input("Enter student's name: "))
std = str(input("Enter student's standard: "))
rollNumber=int(input("Enter Roll Number: "))
print("Enter marks gained in each subject OUT OF 100 ")
sub1 = int(input(">>MATHS: "))
sub2 = int(input(">>SCIENCE: "))
sub3 = int(input(">>SOCIAL STUDIES: "))
totalMarks = int(sub1 + sub2 + sub3)
##print("TOTAL MARKS:"+totalMarks)
percentage = float((totalMarks/300)*100)
print("Here are your details")
print(">> NAME:"+ name)
print("\n")
print(">> STANDARD: "+ std)
print("\n")
print(">> ROLL NUMBER: "+ str(rollNumber))
print("\n")
print(">> TOTAL MARKS GAINED OUT OF 300: "+str(totalMarks))
print("\n")
print(">> PERCENTAGE: "+ str(percentage))
print("\n")
print("keep Learning and do more better in your next exams")

