# Simple game in python

print('Hi, welcome to the Lara quiz!')
print('If you can, try to get as many questions correct as possible')

totalQuestions = 4
score = 0

ans = input('1. What is the username of my Github account?')

if ans.lower() == 'Laurel-leaf1703':
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('2. What is my age? ')

if ans == "25":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('3. What is my favourite sport? ')

if ans.lower() == "basketball":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('4. What is my favourite food? ')

if ans.lower() == "pasta":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


print("Thank you for playing, you got " + str(score) + ' questions correct!' )
percent = (score/totalQuestions) * 100
print("Mark: " + str(int(percent)) + '%')

if percent >= 50:
    print('Nice! You did a great job. You passed!')
else:
    print('Better luck next time')