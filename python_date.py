import datetime, os


now = datetime.datetime.now()
current_age = int(input('How old are you, stranger? ')) # must be integer

if now.year <= 2035: # if it's not 2035 yet, just subtract
	years_to_go = 2035 - now.year
	future_age = int(years_to_go) + int(current_age)
	print('You\'ll be {} in 2035.'.format(str(future_age)))
elif now.year > 2035: # if it's past 2035, show error
	print('It\'s past 2035! I don\'t feel like calculating your age anymore. Bye!')

