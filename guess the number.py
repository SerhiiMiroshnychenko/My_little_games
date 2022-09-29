"""
This is the simplest interactive Python game :-)
"""
import random
the_number = random.randint(0, 9)
print("""
HELLO!                                          (ДОБРОГО ДНЯ!)
You have to guess the number from 0 to 9        (Вам треба вгадати цифру від 0 до 9)
and do it in the minimum number of attempts     (і зробити це за мінімальну кількість спроб)

STARTED:""")
attempt_counter = 0
while True:
    your_number = input("\nEnter a number from 0 to 9 (Введіть цифру від 0 до 9): ")
    if your_number.isdigit():
        attempt_counter += 1
        if int(your_number) < the_number:
            print("\nYour number is less than guessed,\t\t\t\t(Ваше число ,менше ніж загадане)")
            print("try again:\t\t\t\t\t\t\t\t\t\t(спробуйте ще раз)")
        elif int(your_number) > the_number:
            print("\nYour number is more than guessed,\t\t\t\t(Ваше число ,більше ніж загадане)")
            print("try again:\t\t\t\t\t\t\t\t\t\t(спробуйте ще раз)")
        else:
            print("\n\nCONGRATULATIONS!!!\t\t\t\t\t\t\t\t(ВІТАЮ!!!)")
            print(f"You guessed with {attempt_counter} attempt(s)!\t\t\t\t\t(Ви вгадали з {attempt_counter} спроб(и)!)")
            break
    elif not your_number:
        print("\nPlease enter something.\t\t\t\t\t\t\t(Будь ласка введіть щось.)")
    else:
        print("\n\nPlease enter numbers from 0 to 9.\t\t\t\t(Будь ласка вводить цифри від 0 до 9.)")
        print(f'The entered symbol "{your_number}" is not a number.\t\t\t(Введений символ "{your_number}" це не цифра.)')


