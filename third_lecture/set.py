#set is the collection of unordered and unindexed items. In python sets are written with curly brackets.
student = {"jhon", 87, "male", 5.9, "bachelor","bachelor","bachelor", "jhon"}
print(student)

# add new item to set
student.add("vishal")
print("the new student set is:", student)

#remove item from set
student.remove("bachelor")  
print("the new student set after removing bachelor is:", student)