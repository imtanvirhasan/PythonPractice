marks = int(input("Enter your marks:"))
if marks > 100:
    print ("Invalid marks!")
elif marks > 80:
    print ("You have got A+")
elif marks > 70:
    print ("You have got A")
elif marks > 60:
    print ("You have got A-")
elif marks > 50:
    print ("You have got B")
elif marks > 40:
    print ("You have got C")
elif marks < 0:
    print ("Invalid marks")
else:
    print ("You have got F")
