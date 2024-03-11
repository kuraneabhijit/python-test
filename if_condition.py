while True:
    when_python_released=int(input('When was Python 1.0 released? '))
    if when_python_released==1994:
        print('Correct! ')
        break
    elif when_python_released>1994:
        print('It was earlier than that! ')
    else:
        print('It was later than that! ')
