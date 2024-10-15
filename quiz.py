print('Welcome t the Quiz World')
score = 0

index=input('do you want to start th game : ')

if index.lower() != 'yes':
    quit()

print('Get Ready to start')

q1=input('Which one of the following is the correct extension of the Python file?')
if q1.lower() == ".py":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  .py')

q1=input('In which language is Python written?')
if q1.upper() == "C":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  C')

q1=input('What is the method inside the class in python language??')
if q1.lower() == "function":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  Function')


q1=input('Is Python case sensitive when dealing with identifiers?')
if q1.lower() == "yes":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  Yes')

q1=input('Which of the data types does Python not natively support?')
if q1.lower() == "array":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  Array')

q1=input('Python supports the creation of anonymous functions at runtime, using a construct called __________')
if q1.lower() == "lambda":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  Lambda')

q1=input('What arithmetic operators cannot be used with strings in Python?')
if q1.lower() == "-":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  -')

q1=input('Which function is used to read input from the console in Python?')
if q1.lower() == "input()":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  input()')

q1=input('What is the default type of data returned by the input() function in Python 3.x?')
if q1.lower() == "string":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  String')

q1=input('Which of the following is an immutable data type?')
if q1.lower() == "tuples":
    print('Correct')
    score +=1
else:
    print('Incorrect Answer')
    print('Correct Answer is :  Tuples')

print('score :',score,'out of 10')
if score==10:
    print('You are good')
elif score==9:
    print('You are almost there')
elif score==8:
    print('Work hard')
elif score=={7,6}:
    print('Prepare well')
elif score >=5:
    print('Better luck next time')

print('Thank you for your time')
