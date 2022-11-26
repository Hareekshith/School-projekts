#Add Dictionary and take inputs for the names and marks of a particular person
namelist = list()
marklist = list()
namemark = dict()
numnames = int(input("How many names with marks do you want to enter? "))
name = 0
mark = 0

for i in range(numnames):
    name = input("ENter name: ")
    namelist.append(name)
    marks = int(input("Enter marks: "))
    marklist.append(marks)
    namemark[name] = marks 

print(namemark)