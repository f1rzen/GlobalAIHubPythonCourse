def primenumberfinder():
    for i in range(0, 100):
        isprime = True
        if i == 2:
            print(i)
        elif i == 0:
            isprime = False
        elif i== 1:
            isprime= False
        else:
            for j in range(2, i):
                if i % j == 0:
                    isprime = False

            if isprime:
                print(i)

primenumberfinder()
