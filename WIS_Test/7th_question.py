import random

def getDigits(num):
    return [int(i) for i in str(num)]
def generate_num():
    num = random.randint(1000,9999)
    return num
num = generate_num()
def Bull_n_Cow_count(num, player_guess):
    cow_bull = [0, 0]
    num_list = getDigits(num)
    guess_list = getDigits(player_guess)
    for i, j in zip(num_list, guess_list):
        if j in num_list:
            if j == i:
               cow_bull[0] += 1
            else:
                cow_bull[1] += 1
    return cow_bull

if __name__ == "__main__":
    playing = True
    print('''
        This is the Cow & Bull game.
        For every correct digit in the right place, you get a cow. For every correct digit in the wrong place, you get a bull.
    ''')
    while playing:
        player_guess = int(input("Enter your guess: "))
        if player_guess < 1000 or player_guess > 9999:
            print("Enter a 4 digits number only. Try again.")
            continue
        cow_bull = Bull_n_Cow_count(num, player_guess)
        print(f"{cow_bull[0]} cows, {cow_bull[1]} bulls")
        if cow_bull[0] ==4:
            print("Hurray your guess is right!!!")
            break
    else:
        print
