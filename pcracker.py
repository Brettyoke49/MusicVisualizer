password = input("Please enter a password to crack.\nIt may have up to 8 characters and use any numbers, characters, or symbols.\n")

curr_check = [' ']
cracked = False

while ord(curr_check[0]) <= 126:
  print(curr_check)
  if ''.join(curr_check) == password:
    cracked = True
    break

  spot = len(curr_check) - 1 # Would it save time to hard code this instead of forcing a length check each time? Or perhaps have some other variable outside the loop set to len(curr_check) - 1?
  move_up = True

  while move_up: # This block increments up the character line as overflow occurs
    curr_check[spot] = chr(ord(curr_check[spot]) + 1)
    if ord(curr_check[spot]) > 126:
      curr_check[spot] = ' '
      if spot == 0:
        curr_check.insert(0, ' ')
        print(f"Now checking for passwords of length {len(curr_check)}.")
      else:
        spot -= 1
    else:
      move_up = False

if cracked:
  print(f"Password {curr_check} successfully cracked.")
else:
  print("Password crack failed.")
