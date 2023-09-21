a = input('How many points did you get?')
a = int (a)
if (15 <= a):
    print ("Congrats on Gold!")
else:
    if (12 <= a <= 14):
        print ("Congrats on Silver!")
    else:
        if (9 <= a <= 11):
            print ("Congrats on Bronze!")
        else:
            print ("Better luck next time")