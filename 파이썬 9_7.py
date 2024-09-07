# 모듈
'''
같은 폴더에 있는 다른 파일에서 함수를 불러올 때 사용
import calculator (모듈 사용 예시 / calculator는 파일 이름)
import calculator as calc (calc로 calculator 파일 사용 가능)
ex) print(calc.add(5, 9))

from calculator import add, multiply 
--> calculator 모듈(파일)에서 add함수와 multiply함수만 불러 올 때
이렇게 불러온 함수는 
add(2,5)와 같이 (모듈명.add) 붙이지 않고 사용 가능   
'''

# 스탠다드 라이브러리(내장 함수)
import math
print(math.log10(100))
print(math.cos(0))
print(math.pi) # pi처럼 변수도 불러올 수 있음

# 자주 사용되는 모듈의 함수 
import random
print(random.random())
print(random.randint(2,10)) # 2~10(둘다 포함)의 랜덤 정수
print(random.uniform(0,1)) #0~1(둘다 포함)의 랜덤 소수 

# os
import os
print(os.getlogin()) # os에 로그인 되어 있는 아이디


import datetime

pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))


pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15) #년/월/일/시/분/초
print(pi_day)
print(type(pi_day))

#오늘 날짜
today = datetime.datetime.now()
print(today)

# 두 datetime값 사이의 기간
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))

# 기간 더하기
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)

print(today)
print(today + my_timedelta)



# datetime값에서 연도/월 등을 추출 하는 방법
today = datetime.datetime.now()

print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초


# 출력 값을 다양하게 표현
today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))

'''
# 사용자 입력
rand_num = random.randint(1,20)
chance = 4
while True:
    guess_num = int(input("기화가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(chance)))
    if chance == 1:
        print(f"아쉽습니다. 정답은 {rand_num}입니다.")
        break
        
    if rand_num>guess_num:
        print("up")
        chance -= 1 
        
    elif rand_num<guess_num:
        print("down")
        chance -= 1 
        
    elif rand_num==guess_num:
        chance -= 1 
        print(f"축하합니다. {chance}번 만에 숫자를 맞히셨습니다")
        break
'''
    
# open(파일 열기) / '파일 경로(파일명)', 'read(읽기),write(쓰기)'
with open('chicken.txt', 'r', encoding='UTF-8') as f:
    total_revenue = 0
    total_days = 0
    for line in f:
        data = line.strip().split(': ')
        price = int(data[1])
        total_revenue += price
        total_days += 1
        print(price)
        
print(total_revenue/total_days)
        
# 콘솔에 한 줄씩 띄어쓰기 되는 현상: 메모장에 \n(엔터)키 한 번+print에서 자동 \n한 번 때문
# 화이트 스페이스: \t \n  '  '와 같은 공백
#-> strip로 해결(문자열 맨 앞뒤에 있는 모든 화이트 스페이스 제거)
string = "    \t  \n 안녕 하 세 요.\n      "
print(string.strip())

#split(문자열 나누기)
str1 = '1, 2, 3, 4, 5, 6'
str_data = str1.split(", ")
a = str_data[0]
b = str_data[1]
c = str_data[2]
print(c,b)

#화이트 스페이스를 기준으로 문자열 나누기
print("  \t \n 123 \t   456 \n  ghi".split()) # split()를 사용하면 123도 문자열로 인식


#파일 쓰기(만들어 놓지 않아도 됨/ 코드 실행시 자동 생성)
with open('wirte_file.txt', 'a', encoding='UTF-8') as f:
    f.write("Hi~~~\n")
    f.write("my name is JEON")
    
# 'w'는 덮어쓰기 'a'는 기존 파일에 추가
# -> 'w'사용 시 기존의 텍스트는 모두 지워지고 코드로 작성한 내용만 남음
# -> 'a'사용 시 기존의 텍스트에 코드 내용을 추가
# 기존에 파일이 없다면'a'도 'w'와 같이 자동 생성     


# 실습 (157줄의 방식 중요)
with open("vocabulary.txt", 'a', encoding='UTF-8') as f:
    while True:
        english = input("영어 단어를 입력하세요: ")
        if english == 'q':
            break

        korean = input("한국어 뜻을 입력하세요: ")
        if korean == 'q':
            break
        
        f.write('{}: {}\n'.format(english, korean))
        
        
        
with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        data = line.strip().split(": ")
        korean = data[1]
        english = input("{}: ".format(korean))
        if english == data [0]:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(data[0]))        
            
            


# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아 오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("틀렸습니다. 정답은 {}입니다.\n".format(english_word))
