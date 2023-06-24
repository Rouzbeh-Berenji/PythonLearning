MAX_LINES = 3  # Write in Capital because it is CONSTANT 
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
       amount = input("What would you like to deposit ? $") #grabing the amount from the user via input()
       if amount.isdigit(): # check to ensure the input value is a whole number
           amount = int( amount) # convert to integer 
           if amount > 0 : # cheeck to ensure taht the input is greater than 0
               break # if yes , we can continue with the amount and exit of the wile loop
           else: # for propably negetive input 
               print ("Amount must be greater than 0.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")  # a way to put variable between string 
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #to check the values in between two values
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") # another way to put variable between string 
        else:
            print("Please enter a number.")

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True: 
      bet = get_bet()
      total_bet = bet*lines

      if total_bet > balance:  #check to ensure that the requested bet amount is enough based on the current balance !
          print( f"You don't have enough to bet that amount, your current balance is ${balance}")
      else: 
          break
    print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")
 
main()