name=input(" Enter your name")
if name.isdigit():
       name = int(name)
       print("invalid  name value")
elif name.isspace():
    print("Please Enter your name")
else:
    age = input("Enter your age")
    if age.isdigit():
       age=int(age)
       address = input("Enter your address")
       if address.isspace():
           print("Please Enter your address")
       else:
           print("Hello Mr/Ms", name, "age", age, "located in", address, ".", "\n",
                 "thanks for beening one of our commmunity", ',', "   ", "Enjoy")
    elif age.isspace():
        print("Please Enter Your age ")
    else:
      print("Enter correct age")


