MENU = {
    '에스프레소' :  {
        '재료'  :    {
        '물' : 50,
        '커피' : 10,
        },
        '가격' : 18,
    },
    '라떼' : {
        '재료': {
            '물' : 200,
            '우유' : 150,
            '커피' : 24,
        },
        '가격': 2.5
    },
    '카푸치노' : {
        '재료' : {
            '물' : 250,
            '우유' : 100,
            '커피' : 24,
        },
        '가격' : 3.0
    },
}
resources = {
    '물' : 300,
    '우유' : 200,
    '커피' : 100,
}

profit = 0

# 자판기 보유량에서 에스프레소 두 잔을 추출 했을때 resources의 남은 물, 우유, 커피 량을 딕셔너리 형태로 보여주시오
# 로직

# drink = '에스프레소'
# cnt = 2
#
# need = MENU[drink]['재료']
#
# for coffee,amount in need.items():
#     resources[coffee] -= amount * cnt
#
# print(resources)

# 라뗴 한잔을 뽑았을때 남는 resources를 출력하고, 라떼 금액만큼 profit 더한 결과를 콘솔에 출력하시오.

# 로직

#
# drink2 = '라떼'
#
# use = MENU[drink2]['재료']
#
# for latte,amount in use.items():
#     resources[latte] += amount
#
# profit += MENU[drink2]['가격']
#
# print(resources)
# print(f'profit: {profit}')

def report():
    print(f'물{resources['물']}mL')
    print(f'우유{resources['우유']}mL')
    print(f'커피{resources['커피']}g')
    print(f'${profit}')

def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'{item}이(가) 부족합니다.')
            return False
    return True

def process_coins():
    '''
    동전을 입력받아 전체 금액을 반환하는 함수 call3() 유형
    :return: total
    '''
    total = 0.0
    # quarters / dimes / nickels / pennies
    total += int(input('quarters 갯수 >>> ')) * 0.25
    total += int(input('dimes 갯수 >>> ')) * 0.1
    total += int(input('nickels 갯수 >>> ')) * 0.05
    total += int(input('pennies 갯수 >>> ')) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    global profit

    change = round(money_received - drink_cost, 2)
    if change >= 0:
        profit += drink_cost
        if change > 0:
            print(f'여기 ${change}의 잔돈을 반환합니다.')
        return True
    else:
        print(f'금액이 부족합니다. ${money_received}을 반환합니다.')
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'{drink_name}가 나왔습니다.')

is_on = True
while is_on:
    choice = input('어떤 음료를 드시겠습니까? 에스프레소 / 라떼 / 카푸치노 >>>> ')

    if choice == 'off':
        print('자판기를 종료합니다.')
        break

    elif choice == 'report':
        report()
        continue

    elif choice in ['에스프레소', '라떼', '카푸치노']:
        drink = MENU[choice]

        if is_resource_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink['가격']):
                make_coffee(choice, drink['재료'])

    else:
        print('잘못 입력하셨습니다.')