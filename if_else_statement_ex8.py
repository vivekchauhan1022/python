science = int(input("enter your science mark:"))
maths = int(input("enter your maths mark:"))
english = int(input("enter your english mark:"))

total = science+maths+english

percentage = total/3

print("--------------------Result------------------")
print("math:",maths)
print("science:",science)
print("english:",english)
print("total:",total)
print("percentage:",percentage,"%")

if percentage>=80:
    print("Very Good...")
    
if percentage>=60 and percentage<=80:
    print("Good")

else:
    print("Poor")