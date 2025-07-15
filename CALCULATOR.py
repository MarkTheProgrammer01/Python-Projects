import sys

print("\nWELCOME TO YOUR PERSONAL CALCULATOR")
print("\nTHIS CALCULATOR SUPPORTS THE 4 BASIC OPERATIONS")

operations = ["+ ADDITION", "- SUBTRACTION", "* MULTIPLICATION", "/ DIVISION",]
for operation in operations:
    print(operation)
print("\nPRESS 1,2,3 OR 4 TO CHOOSE AN OPERATION")




def addition():
      first = input("\nFirst number: ")
      second = input("Second number: ")
      result = int(first) + int(second)
      print("\nThe result is: " + str(result))


def subtraction():
    first_2 = input("\nFirst number: ")
    second_2 = input("Second number: ")
    result = int(first_2) - int(second_2)
    print("\nThe result is: " + str(result))


def multiplication():
    first_3 = input("\nFirst number: ")
    second_3 = input("Second number: ")
    result = int(first_3) * int(second_3)
    print("\nThe result is: " + str(result))

def division():
    first_4 = input("\nFirst number: ")
    second_4 = input("Second number: ")
    result = int(first_4) / int(second_4)
    print("\nThe result is: " + str(result))

def quit():
    print("\nThank you for using calculator!")
    sys.exit()





while True:
  user_input = int(input("\nChoose your operation: "))
  if user_input == 1:
      addition()
  elif user_input == 2:
      subtraction()
  elif user_input == 3:
      multiplication()
  elif user_input == 4:
      division()
  print("\nDo you want to continue?")
  response = input()
  if response == "yes":
      continue
  elif response == "no":
      quit()