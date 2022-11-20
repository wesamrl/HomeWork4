print(" You can Choose the process : ", "\n",
      "1- +"
      , "\n",
      "2- -"
      , "\n",
      "3- *"
      , "\n",
      "4- /"
      , "\n",
      "5- ^"
      "\n",
      "6- %"
      )
def checkValueIsNumber(inputStr: str):
    if inputStr != None and not inputStr.isspace() and inputStr.count(".") <= 1:
        inputStr = inputStr.replace(".", "1")
        if inputStr.isdigit():
            return True

    return False
num=input("Enter first number")
if checkValueIsNumber(num)==True:
   number1=float(num)
   operat = input("Enter operat")
   num2 = input("Enter Second number")
   if checkValueIsNumber(num2)==True:
       number2 = float(num2)
       if operat == "+" or operat == "1":
           total = number1 + number2
           print("real total :", total)
           print("nearly :", round(total))
           print("integer value: ", int(total))

       elif operat == "2" or operat == "-":
           total = number1 - number2
           print("real total :", total)
           print("nearly :", round(total))
           print("integer value: ", int(total))

       elif operat == "3" or operat == "*":
           total = number1 * number2
           print("real total :", total)
           print("nearly :", round(total))
           print("integer value: ", int(total))

       elif operat == "4" or operat == "/":
           total = number1 / number2
           print("real total :", total)
           print("nearly :", round(total))
           print("integer value: ", int(total))

       elif operat == "5" or operat == "^":
           total = number1 ^ number2
           print("real total :", total)
           print("nearly :", round(total))
           print("integer value: ", int(total))

       elif operat == "6" or operat == "%":
           total = number1 % number2
           print("real total :", total)
           print("nearly :", round(total))
           print("integer value: ", int(total))
       else:print("Error in your input operator")

   else: print("invalid value")
else:print("invalid value , Not number")
