import random

# Text-based Slot Machine

"""
-) Deposit certain amount of Money
-) Betting on 1-3 lines
-) Win or Lose?
-) Got lines ? -> Multiplying their bet by value of line
-) Add Win to balance
-) Allowance to keep playing till cash out or money is out


-) Collect user deposit
-) Allow to bet on one or multiple lines
-) Generate different items that are in the slot machine on the different reels
-) Spin the Slot Machine
-) See if they acutally got any of these lines
-) Add win to their Balance
"""

# Global Constants:
## Betting
max_lines = 3
max_bet = 100
min_bet = 1

## Slotmachine
rows = 3
cols = 3
# Number of As, Bs, ..
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# Multipl. for A, B, ...
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


"""
-) Check if user won -> 3 identical symbols on 1 line
-) loop over every row
-) check symbol in first col of current row -> A,B,...
-) loop over every colum in current row and check if symbol is identical
"""
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # +1 bc line is an index

    return winnings, winning_lines


"""
-) Generate Column for every col we have -> 3; for loop runs 3 times
-) Picking random Values for each row we have for current Col
-) Copy all_symbols for removing the current choosen Value
"""
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # iteration over Dic -> # symbol: Letter/Key; symbol_count: Value
    # get Key & value with .items()
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # Nested List -> represent Value in Column -> columns = [[], [], []]
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


"""
-) Print Funktion for testing slot machine spin
-) Transpose Matrix
-) Loop over rows we have
-) For every single row -> loop over every column
-) for every column -> print current row we are on 
"""
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):    # enumerate -> index
            if i != len(columns) - 1:
                print(column[row], end = " | ") # end default: \n
            else:
                print(column[row], end = "")

        print() # for loop above prints line -> print here equal to \n


# Collecting User Input -> Deposit from user
def deposit():
    while True:
        amount = input("What would you like to deposit? €")
        # Check if digit; isdigit() outcome will be False with negative Numbers
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


# Define Number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(max_lines) + ")? " )
        # Check if digit; isdigit() outcome will be False with negative Numbers
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


# Amount to bet on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? €")
        # Check if digit; isdigit() outcome will be False with negative Numbers
        if amount.isdigit():
            amount = int(amount)
            if min_bet <= amount <= max_bet:
                break
            else:
                print(f"Amount must be between €{min_bet} - €{max_bet}. ")
        else:
            print("Please enter a number.")

    return amount


# Looping for multiple games in a row
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough € to bet that amount. Your current balance is €{balance}.")
        else:
            break

    print(f"You are betting €{bet} on {lines} lines. Total bet is equal to: €{total_bet}")

    slots = get_slot_machine_spin(rows, cols, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won €{winnings}.")
    print(f"You won on lines:", *winning_lines)  # * -> Unpack operator
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: €{balance}.")
        answer = input("Press enter to play (q to quit).")

        if answer == "q":
            break
        elif balance == 0:
            balance = deposit()

        balance += spin(balance)

    print(f"You left with €{balance}")

main()

