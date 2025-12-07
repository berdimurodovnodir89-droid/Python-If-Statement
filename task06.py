number=input('Raqam kiriting :')
code=number[:2]

if code == "90" or code == '91' :
    print('Beeline')
elif code == "93" or code == '94' :
    print('ucell')
elif code == '95' or code == '99' :
    print('uzmobile')
elif code == '88' or code == '97' :
    print('mobiuz')

else :
    print('nomalum operator')