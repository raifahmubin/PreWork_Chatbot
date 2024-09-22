print("Hello! I am your math chatbot.")
name = input("What is your name? ")
age = input("What is your age? ")
print(
    "What math can I help you with? Type one of the options below or 'quit' to exit."
)
how_help = input(
    "Type 'addition', 'subtraction', 'multiplication', or 'division'. ")
if how_help == "addition":
  print("What is the first number you want to add?")
  first_number = input()
  print("What is the second number you want to add?")
  second_number = input()
  result = int(first_number) + int(second_number)
  print("The result is " + str(result))
elif how_help == "subtraction":
  print("What is the first number you want to subtract?")
  first_number = input()
  print("What is the second number you want to subtract?")
  second_number = input()
  result = int(first_number) - int(second_number)
  print("The result is " + str(result))
elif how_help == "multiplication":
  print("What is the first number you want to multiply?")
  first_number = input()
  print("What is the second number you want to multiply?")
  second_number = input()
  result = int(first_number) * int(second_number)
  print("The result is " + str(result))
elif how_help == "division":
  print("What is the first number you want to divide?")
  first_number = input()
  print("What is the second number you want to divide?")
  second_number = input()
  result = int(first_number) / int(second_number)
  print("The result is " + str(result))
else:
  print("Goodbye! Have a nice day.")
