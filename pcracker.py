import timeit
import os
import getpass

os.system('clear')

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

print(bcolors.GREEN + "Welcome to Mediocre Password Cracker.\n")
password = getpass.getpass("Please enter a password to crack.\nIt may have up to 8 characters and use any numbers, characters, or symbols.\t")

if len(password) > 8:
  print("Try again dipshit")
  quit()

curr_check = [' ']
cracked = False

print(bcolors.BLUE + "\n\nThank you. Loading and checking base modules...")
start_time = timeit.default_timer()

words = open("words.txt", "r")
passwords = open("passwords.txt", "r")
dictionary_words = words.read().splitlines()
common_passwords = passwords.read().splitlines()

for i in dictionary_words:
  if i == password:
    curr_check = i
    cracked = True
    break

if cracked != True:
  for i in common_passwords:
    if i == password:
      curr_check = i
      cracked = True
      break

load_time = timeit.default_timer() - start_time
print(f"\nModules checked in {load_time} seconds.")

count = 0

while ord(curr_check[0]) <= 126 and cracked == False:
  if ''.join(curr_check) == password:
    cracked = True
    break

  count += 1
  if count % 10000000 == 0:
    print(f"{int(count / 1000000)} million passwords checked...")

  spot = len(curr_check) - 1 # Would it save time to hard code this instead of forcing a length check each time? Or perhaps have some other variable outside the loop set to len(curr_check) - 1?
  move_up = True

  while move_up: # This block increments up the character line as overflow occurs
    curr_check[spot] = chr(ord(curr_check[spot]) + 1)
    if ord(curr_check[spot]) > 126:
      curr_check[spot] = ' '
      if spot == 0:
        curr_check.insert(0, ' ')
      else:
        spot -= 1
    else:
      move_up = False

elapsed = timeit.default_timer() - start_time

if cracked:
  print(bcolors.YELLOW + bcolors.BOLD + f"\n\nPassword {curr_check} successfully cracked after {elapsed} seconds.")
else:
  print("\n\nPassword crack failed.")
