import sys

fruit_basket = ['apple', 'mango', 'persimmon', 'blackberry', 'rambutan']

guess = input('Guess a fruit in my basket. Singular form, please! ')

for fruit in fruit_basket:
	if guess == fruit: 
		print('You guessed right! I have that fruit. Good job!')
		break
	else:
		continue

print('Sorry, try again.')
	