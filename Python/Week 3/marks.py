score = int(input('Enter your mark: '))
def gradingsystem(score):
    if score >= 90:
        print(f'Your score of {score} is A') 
    elif score >= 80:
        print (f'Your score of {score} is B')
    elif score >= 70:
        print (f'Your score of {score} is C')
    elif score >= 60:
        print (f'Your score of {score} is D') 
    else:
        print (f'Your score of {score} is F')

gradingsystem(score)