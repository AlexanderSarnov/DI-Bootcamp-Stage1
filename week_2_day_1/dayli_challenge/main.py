def check_and_process_string():
  """
  This function prompts the user for a string, validates its length,
  and prints the first and last characters if it's 10 characters long.
  """
  while True:
    user_input = input("Enter a string (10 characters): ")
    if len(user_input) < 10:
      print("String not long enough.")
    elif len(user_input) > 10:
      print("String too long.")
    else:
      print("Perfect string")
      # Access and print first and last characters
      first_char = user_input[0]
      last_char = user_input[-1]
      print(f"First character: {first_char}")
      print(f"Last character: {last_char}")
      break  # Exit the loop if the string is valid (10 characters)

check_and_process_string()