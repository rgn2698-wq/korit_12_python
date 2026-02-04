from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자를 통한객체생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

ADMIN_PASSWORD = '1234'

def admin_mode (coffee_maker: CoffeeMaker, money_machine: MoneyMachine) -> bool:
    pw = input('관리자 모드\n비밀번호 입력:')
    if pw != ADMIN_PASSWORD:
        print('비밀번호가 틀렸습니다.')
        return False
    else:
        print('로그인 성공')

    print('관리자 모드 \n( 커피재료 / 수입 / 보고 / 보충 / 종료 / 메뉴 )')
    while True:
        cmd = input('>>> ').lower().strip()
        if cmd == '커피재료':
            coffee_maker.report()

        elif cmd == '수입':
            money_machine.report()

        elif cmd == '보고':
            coffee_maker.report()
            money_machine.report()

        elif cmd == '종료':
            print('자판기를 종료합니다.')
            break

        elif cmd == '메뉴':
            print('관리자 모드를 종료합니다.')
            return False

        else:
            print('지원하지않는 명령어 입니다.')


is_on = True
while is_on:
    opt = menu.get_items()
    choice = input(f'어떤 음료를 드시겠습니까? {opt} >>>')

    if choice.lower() == 'admin':
        shutdown = admin_mode(coffee_maker, money_machine)
        if shutdown:
            print('자판기가 종료됩니다.')
            break
        continue

    if choice.lower() in 'resource,profit,report,off':
        print('해당 메뉴는 관리자만 이용 가능합니다.')
        continue

    if choice.lower() == 'report':
        coffee_maker.report()
        money_machine.report()
        continue

    drink = menu.find_drink(choice)
    if drink is None:
        continue

    if not coffee_maker.is_resource_sufficient(drink):
        continue

    if not money_machine.make_payment(cost=drink.cost):
        continue

    coffee_maker.make_coffee(drink)

    break