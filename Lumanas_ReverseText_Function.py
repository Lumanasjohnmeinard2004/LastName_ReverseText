#python program that asks the user to enter a text and print it in reverse/backward.

def reverse_string():
  while True:
    try:
      text = input("Enter a string: ")
      reversed_text = ""
      for char in text:
        reversed_text = char + reversed_text
      print("Output:", reversed_text)
      break
    except ValueError:
      print("Error Reported! Enter text only.")

reverse_string()
