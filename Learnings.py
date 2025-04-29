print("hello")  #sample print
"""
# sample tax calculation
income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43

print('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or',
      income * ripoffland_rate, 'income tax in Ripoffland. You would save',
      income * ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowtaxland!')

# sample string operation
login = input('Enter your login: ')
language = input('Enter your native language: ')

print('Your login is', login, 'and you speak', language)

#sample salary calculation
hours = float(input('How many hours did you work last month? '))
rate = float(input('What is your hourly rate? '))

print('Last month, you earned', hours * rate, 'dollars')

# Refund policy helper
purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')

if (is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
    print('You can get a refund.')
else:
    print('You cannot get a refund.')
 

# guessing game
while True:
    answer = int(input('When was Python 1.0 released? '))
    if answer > 1994:
        print('It was earlier than that!')
    elif answer < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break
 
#Sample budget calculation
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low = 0
normal = 0
high = 0

for month in spendings:
    if month < 1000.0:
        low += 1
    elif month <= 2500.0:
        normal += 1
    else:
        high += 1

print('Numbers of months with low spendings: ' + str(low) + ', normal spendings: ' + str(
    normal) + ', high spendings: ' + str(high) + '.')

#Sample list operation
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170)
]

counter = 0
sum = 0.0

for con in connections:
    if con[1] == 'Rome':
        counter += 1
        sum += con[2]

print(counter, 'connections lead to Rome with an average flight time of', sum / counter, 'minutes')

#Get rid of duplicates
def unique(input_list=[]):
  to_return = []
  for el in input_list:
    if el not in to_return:
      to_return.append(el)
  return to_return

unique_values=unique(['a','c','f','o','d','o','o'])
print('Now the list after removing duplicates is', unique_values)
"""
# finding longest word
def get_longest_word(input_string):
  words = input_string.replace('.', ' ').replace(',', ' ').split()
  temp_max_word = ''

  for word in words:
    if len(word) > len(temp_max_word):
      temp_max_word = word

  return temp_max_word

temp_max_word=get_longest_word("Nothing is impossible,the word itself says i m possible.")
print("The longest word from given sentence is", temp_max_word)