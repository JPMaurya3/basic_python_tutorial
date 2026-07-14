#creating a dictionary
student ={"name":"vishal","age":22,
          "gender":"male","mark":87,
          "fruits":["appple","banana","mango"],
          "address":{"city":"delhi","state":"delhi"}}
print(student)
print("the name of student is:", student["name"])
print("the age of student is:", student["age"])
print("the gender of student is:", student["gender"])
print("the mark of student is:", student["mark"])
print("the fruits of student is:", student["fruits"][0])
print("the city of student is:", student["address"]["city"])

#assign value
student["name"] = "kumar"
print("the new name of student is:", student["name"])

#type cast a dctionary to list
student_list = list(student)
print("the student list is:", student_list)