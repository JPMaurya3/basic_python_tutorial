# print the conditional statements traffic light
light = input("enter the traffic light color:").strip()
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("ready")
elif(light == "green"):
    print("go")
else:
    print("invalid color")