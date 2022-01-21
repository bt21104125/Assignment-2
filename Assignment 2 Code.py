#Question 1 Python Code for the input string 
print("Solution of Ques.No.1 Using Different string operations")
print(" ")
a=("Python is a case sensitive language")
print("Solution 1 (a) To find the length of the string")
print(len(a))
print(" ")
print("Solution 1 (b) To reverse the order of the string")
print(a[::-1])
print(" ")
print("Solution 1(c) To using slice function ")
b=print(a.split(a[0:11:1]))
print(" ") 
print("Solution 1(d) To replace a particular word ")
print(a.replace("a case sensitive","object oriented"))
print(" ")
print("Solution 1(e) To find the index of the substring a ")
print(a.index("a"))
print(" ") 
print("Solution 1(f) To remove the whitespaces from given input string")
print(a.replace(" ",""))
print(" ")
print("****************************************************************")
print(" ")


#Question 2 Storing different values in string by using string formatting
print("Solution of Ques.No.2 Storing different variables in the string after formatting")
a=str(input("Enter the NAME of student="))
b=int(input("Enter the SID of student="))
c=str(input("Enter the DEPARTMENT NAME of student="))
d=float(input("Enter the CGPA of student="))
print("Hey", a ,"Here !" )
print("My SID is", b )
print("I am from" ,c, "department and my CGPA is" ,d)
print(" ")
print("****************************************************************")
print(" ")


#Question 3 Using bitwise operators to calculating following  parts
print("Solution of Ques.No.3 Using bitwise operator to calculate the following: ")
a=56
b=10
print("Solution 1 (a) (a&b)  ")
print(a&b)
print(" ")
print("Solution 1 (b) (a|b)  ")
print(a|b)
print(" ")
print("Solution 1(c) (a^b)  ")
print(a^b)
print(" ")
print("Solution 1(d) Left side both  a and b with 4 bits ")
print(a>>2 and b>>2)
print(" ")
print("Solution 1(e) Right side a with 2 bits  and b with 4 bits ")
print(a<<2 and b<<4)
print(" ")
print("****************************************************************")
print(" ")



#Question 4 Python program to find the greatest number among the three Entered number by the user
print("Solution of Ques.No.4 Finding Greatest Number among he three entered number  ")
a=int(input("Enter the First number="))
b=int(input("Enter the Second number="))
c=int(input("Enter the Third number="))
if a>b and a>c:
    print("a is the greatest number among three number")
elif b>a and b>c:
      print("b is the greatest number among three number")
else :
      print("c is the greatest number among three number")
print(" ")
print("****************************************************************")
print(" ")


#Question 5 Checking the word "name" in the string entered by the user
print("Solution of Ques.No.5 Finding word(name) in the entered string by the user")
string=str(input("Enter any String="))
if "name" in string:
        print("Yes")
else:
    print("No")
print(" ")
print("****************************************************************")
print(" ")


#Question 6 Testing the crieteria to fulfill the forming a triangle by entering three sides by the user
print("Solution of Ques.No.6 Test to form a triangle by entered ")
a=float(input("Enter the First side of triangle="))
b=float(input("Enter the Second side of triangle="))
c=float(input("Enter the Third side of triangle="))
if a>b+c:
    print("Triangle can not be formed")
elif b>a+c:
    print("Triangle can not be formed")
elif c>a+b:
    print("Triangle can not be formed")
else:
    print("Triangles is formed")
print(" ")
print("****************************************************************")
print(" ")    
    









