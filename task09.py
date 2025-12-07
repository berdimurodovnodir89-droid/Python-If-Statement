num1=int(input('1-sonni kiriting :'))
num2=int(input('2-sonni kiriting :'))
num3=int(input('3-sonni kiriting :'))

if num1 == num2 == num3 :
    print('Teng tomonli')
elif num1 == num2 < num3 :
    print('teng yonli')
elif num1 > num2 == num3 :
    print('teng yonli')
elif num1 < num2 == num3 :
    print('trng tomonli')
elif num1 > num2 > num3 :
    print('turli tomonli')
elif num1 < num2 < num3 :
    print('turli tomonli')