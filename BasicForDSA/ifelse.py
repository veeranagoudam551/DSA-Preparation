#Given marks of a student, print on the screen:
#Time Complexity:0(1)
#Space Complexity:0(1)
marks = int(input("enter the marks of student:"))
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")