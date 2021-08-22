import calc_func


while (True):
    operation = calc_func.calculate()
    match operation:
        case 1:
            print(calc_func.sum_fun())
        case 2: 
            print(calc_func.sub_fun())
        case 3:
            print(calc_func.multi_fun())
        case 4:
            print(calc_func.div_fun())
        case 5:
            calc_func.min_fun()
        case 6:
            print(calc_func.squ_fun())
        case 7:
            print(calc_func.pow_fun())  
        case 8:
            print('See you later')
            break
        case _:
            break
    
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

    if calc_again == 'Y':
      print("OK")

    elif calc_again == 'N':
        print('See you later')
        break

    else:
       break
         



