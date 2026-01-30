leap_year = int(input('년도를 입력하세요 >>> '))

if int(leap_year)%4==0:
    print('윤년입니다.')
elif int(leap_year)%4==1:
    print('윤년이 아닙니다.')
else:
    print('잘못된 년도입니다.')

print(f'해당 {leap_year}년도는' )

# ch02_loops -> main_while / main_for