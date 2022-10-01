# simulating a coin flipping

def flipping():
    """This function is a simulation of a coin toss."""
    from random import choice as coin

    while True:
        decision = input('\nPress ENTER\nto flip a coin\nand "b" to exit: ')
        if not decision:
            print("\n", coin(["HEAD(орел)", "TAIL(решка)"]))
        elif decision == "b":
            return print("\nThe program is over.")
        else:
            print(f'\nI remind you of ENTER or "b".\nNot "{decision}".\nTry again.')


flipping()
