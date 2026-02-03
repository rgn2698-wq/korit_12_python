class Student:
    # 생성자 정의
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        # 설적을 저장힉 위한 빈 딕셔너리 -> 과목명을 ket / 정수를 value로 예정
        self._grades = {}

    # python 버전의 getter에 해당하는 메서드 정의방식
    @property
    def name(self):
        return self._name

    # python 버전의 setter의 예시
    @name.setter
    def name(self, value):
        self._name = value

# 객체생성
student1 = Student('김일',2026001)
# getter의 호출    - 주의사항 : 객체명.속성명도 아니도 객체명.메서드명() - 소괄호도 아님.
print(f'학생 이름 : {student1.name}')
# setter의 호출 예시
student1.name = '김영'
# getter 재호출
print(f'변경된 학생 이름 : {student1.name}')
print(student1._name)   # 속성으로도 여전히 불러낼수있음.

'''
이상의 코드에서 확인 가능한 점은 JAva기준으로 파이썬 코드를 해석할때 의문 스러운 점이 많다는 점임.

1. _name이라는 속성이 있는데 객체명.name을 통해서 '김일'/'김영' 이라는 속성값이 출력된다는 점 : 그런데 객체명._name도 작동함.

2. 객체명._name = '김영' 이 아니라 객체명.name = '김영'으로 재대입 한것 처럼 보이지 setter의 호출로 보이지 않는다는 저ㅓㅁ. 당연히 갹체명 .set_name("김영")이어야 ㅎ자ㅣ않냐는 의문점임.

그런데 이건 Java기준으로 본거고, 파이썬으로 풀었을때는 _name / name이 서로 다른 개념으로 보이지만 '_'가 붙으면 파이썬 언어 내부적으로 동일한 속성으로 처리해즘

객체명.속성명 뒤에 ()가 없음에도 불구하고 ㅍ아ㅣ썬은 이걸그냥 메서드처럼 처리해준다는 점임. 그래서 그냥 객체명.속성명이면 getter로 처리해주고 '객체명.속성명 = 데이터' 알아서 setter로 처리해줌

그런데 그 '알아서' 처리하기 위한 필수적인 작업이 @property와 속성명.setter라는 데코라이터 때문

원래는 자동생성되기때문에 일일히 @달고 _속성명인지 / 그냥 속성명인지 따질 필요가 없는데 백엔드를 파이썬으로 짜지않기 때문에 현재 쓸모가 좀 없는 상황임. 현재 수준으론 파이썬으로 백엔드를 작성할때 필요할 때가 있고 이렇게 getter/setter를 쓴다는것으로 알아두면 됨.
'''