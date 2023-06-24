import random  # we need some random number fot slot machine
MAX_LINES = 3  # Write in Capital because it is CONSTANT 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


# we need some symbols for slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
# look trough only rows that user bets on
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #could be 1 to MAX_LINES
        symbol = columns[0][line] #get the first symbols and check others to be the same
        for column in columns: # we got symbol, and we want to go trough the column 
            symbol_to_check = column[line]
            if symbol != symbol_to_check: # if we found one of the symbols are different with the selected symbol, the line dose not win !
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):  # how to generate the items that going to be in our slot machine
    #randomly pick the number of rows inside of each columns
    all_symbols =[] 
    for symbol, symbol_count in symbols.items():  # to iteration trough a dictionary : .item() gives you both the key and a value associated with a dictionary
        for _ in range(symbol_count) : # "_" is an anonymous variable that you can look trough something 
            all_symbols.append(symbol)

    columns = [] #defining our columns list
    #we want to generate a column for every single column that we have
    for _ in range(cols): 
        column= []
        current_symbols = all_symbols[:] # make a copy of all_symbols to current
        for _ in range (rows):
             value = random.choice(current_symbols) #picking random valus for each rows / this picks a random value from the list of symbols that we have
             current_symbols.remove(value)
             column.append(value) # add this value to our coulmn
        columns.append(column)
    return columns
    
def print_slot_machines (columns): # our columns in a list (horizontal) we need to rotate them to correctly shown them as a coulmn (verticaly)
# this operation reffered to as "transposing" (flip our coulmns from horizontal to vertical):
    for row in range(len(columns[0])):  # we look trough every single row that we have
        for i, column in enumerate(columns) : # for every single row, we look r=trough every column, and print only the first value
            if i != len(columns) - 1:# the max index we have
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
  



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
 
def spin(balance): # refer to one game/spin
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main(): #make the spin continuously untill balance is enough 
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
    
main()