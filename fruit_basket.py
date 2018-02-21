import sys

fruit_basket = ['apple', 'mango', 'persimmon', 'blackberry', 'rambutan']

# invoke the program with main()

def main():
    guess_count = 0
    while guess_count < 5:
        guess = guess_fruit(fruit_basket)
        
        if guess:
            print("Good job!")
            return
        else:
            print("I don't have that fruit.")
            guess_count += 1

# create a function called guess_fruit()

def guess_fruit(basket):
    guess = input("Guess a fruit in my basket: ")
    return (guess in basket)

main()