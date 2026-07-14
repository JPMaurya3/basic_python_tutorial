# print the conditional statements traffic light
light = input("enter the traffic light color:").strip() #strip() is used to remove any leading or trailing whitespace from the input string
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("ready")
elif(light == "green"):
    print("go")
else:
    print("invalid color")