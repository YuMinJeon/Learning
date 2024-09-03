# 주석
# Ctrl + shift + L (선택 단어 모두 변경)

#한 줄에 여러 변수 정의
a = 1; b = 2; c = 3

#함수 정의
def hello():
    print("Hello!")
    print("Welcome")
    
hello()

def hello_2(name):
    return("Hello! "+ name)

print(hello_2("Yumin"))


#round(반올림 함수)
print(round(3.141592))
print(round(3.141592, 2)) #3.14

#문자열 안에 따옴표
print("He said \"i love you\"")

#오늘은 2024년 9월 3일 입니다.
year = 2024; month = 9; day = 3
print("오늘은 {}년 {}월 {}일 입니다.".format(year, month, day))
date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day+1))

#{:.4f} -> 소수점 넷째 자리까지 반올림

#c,java에서는 이와같이 포맷 스트링 사용
name = "최지웅"
age = 32
print("제 이름은 %s이고 %d살입니다." % (name, age))

#f-string 최근에 많이 사용
name = "최지웅"
age = 32
print(f"제 이름은 {name}이고 {age}살입니다.")

# return 사용시 즉시 함수 종료

#옵셔널 파라미터는 무조건 마지막에!
def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터에 값을 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터에 값을 제공하지 않는 경우

PI = 3.14 #pi와 같이 절대적인 값(변하지 않는)은 constant(상수)로 모든 알파벳을 대문자료 표기(규칙)



# 최소 지폐수로 거스름돈 계산기
def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐
    ten_count = (change % 50000) // 10000  # 10,000원 지폐
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐

    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))


# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
