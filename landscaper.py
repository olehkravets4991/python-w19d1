# Define initial variables
money = 0
tools = []
winning_amount = 1000

# Function to check if the user has won
def check_win():
    global money
    if money >= winning_amount and "team" in tools:
        return True
    return False

# Main game loop
while True:
    # Display current status
    print(f"Money: ${money}, Tools: {', '.join(tools)}")

    # Check for win
    if check_win():
        print("Congratulations! You've won the game!")
        break

    # Ask the user for their action
    action = input("What would you like to do? (cut / buy / hire / quit): ").strip().lower()

    # Perform the chosen action
    if action == "cut":
        if "team" in tools:
            money += 250
        elif "battery-powered lawnmower" in tools:
            money += 100
        elif "push lawnmower" in tools:
            money += 50
        elif "scissors" in tools:
            money += 5
        else:
            money += 1
    elif action == "buy":
        if money >= 500 and "team" not in tools:
            tools.append("team")
            money -= 500
        elif money >= 250 and "battery-powered lawnmower" not in tools:
            tools.append("battery-powered lawnmower")
            money -= 250
        elif money >= 25 and "push lawnmower" not in tools:
            tools.append("push lawnmower")
            money -= 25
        elif money >= 5 and "scissors" not in tools:
            tools.append("scissors")
            money -= 5
        else:
            print("You don't have enough money to buy any tools.")
    elif action == "hire":
        if "team" not in tools:
            print("You need to buy a team of starving students before hiring.")
        elif money >= 500:
            money -= 500
            print("You've hired a team of starving students!")
        else:
            print("You don't have enough money to hire a team.")
    elif action == "quit":
        print("Thanks for playing. Goodbye!")
        break
    else:
        print("Invalid action. Please choose 'cut', 'buy', 'hire', or 'quit'.")
