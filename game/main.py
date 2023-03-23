import random

def taking_choice(choices):
    player = None
    cpu = random.choice(choices)

    '''
    You will be in a loop until you input your choice correctly.
    * Choices are 'rock', 'paper' and 'scissors' and they can be written
    in lowercase, uppercase or capitalized.
    '''
    while player not in choices:
        player = input( "\nWrite your choice: " )
        player = player.lower()

    return player, cpu

def choosing_winner(player, cpu):
    '''
    The function will return on of these results:
    None => Tie
    0    => CPU wins
    1    =>  Player wins
    '''
    if player == cpu:
        return None
    elif player == "rock":
        if cpu == "paper":
            return 0
        elif cpu == "scissors":
            return 1
    elif player == "paper":
        if cpu == "scissors":
            return 0
        elif cpu == "rock":
            return 1
    elif player == "scissors":
        if cpu == "rock":
            return 0
        elif cpu == "paper":
            return 1

def main():
    choices = [ "rock", "paper", "scissors" ]

    player, cpu = taking_choice(choices)

    print("\nYour option => ", player.upper())
    print("CPU's option => ", cpu.upper())
    print()
    
    result = choosing_winner(player, cpu)
    
    if result == None:
        print("Tie")
    elif result == 0:
        print("CPU wins")
    else:
        print("You win")

if __name__ == "__main__":
    # Run your code
    print("ROCK, PAPER, SCISSORS GAME")
    main()