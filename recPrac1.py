# made to take user input to predict which is best
import random

num = 999 # hidden from the program, known to the user
already_guessed = []
low, high = 0, 1000   # the range the number must be in this just makes the range 

def find_num(a, c, low, high, tries=0):
    b = random.randint(low, high)
    if b not in c:
        c.append(b)

        return b
    if tries < 30:
        return find_num(a, c, low, high, tries + 1)

a = random.randint(0, 1000)
already_guessed.append(a)
guessing = True
print("The program will try to guess your number. Respond with higher, lower, or correct. 0 is the lowest, 1000 the highest.")

while guessing and a != num:
    print(f"Is your number {a}?   (range: {low}-{high})")
    user_input = input(">>>> ").strip().lower()
    if user_input == "higher":
        low = a + 1          # number is above this guess why does this not become 1 if user inputs 20, 
    elif user_input == "lower":
        high = a - 1         # number is below this guess
    elif user_input == "correct":
        break
    else:
        print("invalid, type higher, lower, or correct")
        continue
    if low > high:
        print("Your answers contradict each other!")
        guessing = False
        break

    a = find_num(a, already_guessed, low, high)

if guessing:
    print(f"Your number is {a}! Found it in {len(already_guessed)} guesses.")