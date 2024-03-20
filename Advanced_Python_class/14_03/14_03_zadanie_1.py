# Zadanie 1
for i in range(1,101):
    if(i==50):
        print('83837')
    elif(i%5 == 0 & i%3 == 0):
        print('LoveUEP')
    elif(i%5 == 0):
        print('UEP')
    elif(i%3 == 0):
        print('Love')
    else:
        print(i)