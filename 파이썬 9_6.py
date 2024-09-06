country = ['한국', '중국', '일본', '미국']
del country[1]
print(country)

country.append('프랑스')   #### 아무것도 없는 리스트에 값을 추가할때 -> list[i] = '영국'이런식으로 X / 무조건 append로 추가
print(country)            #### list[i] = '영국' -> 원래 i자리에 있던 값을 변경할때만 사용

country.insert(2, '독일')
print(country)

country.remove('일본')
print(country)

new_country = sorted(country, reverse=True)  #오름차순 정렬은 reverse없이
print(new_country)    #sorted함수는 기존의 country리스트는 건들지 못함

country.sort()
print(country)   # 변수추가 없이 리스트 정렬시에는 sort()함수
country.reverse()  # sort(reverse=True) 동일 

tem = 3.455
#round(tem) -> print(tem) 하면 3.455출력 / round함수는 sorted처럼 원래 값은 변경x
print(round(tem))


# in 함수(리스트 안에 해당 value값이 있으면 True)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 not in primes) # value값이 있으면 True 

print(primes.index(13))  #13값의 인덱스 반환 -> 5


# 리스트 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산
    right = len(numbers) - left - 1

    # 위치 바꾸기
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

print("뒤집어진 리스트: " + str(numbers))



#닥셔너리
dict = {
    '한국': '서울',
    '일본': '도쿄',
    '미국': '워싱턴',
    '프랑스': '파리'
}
dict['중국'] ='베이징'

print(dict ['미국'])
print(dict.keys())
print(dict.values())
print('도쿄' in dict.values())

#key, value모두 받아오는 방법
for key, value in dict.items():
    print(key, value)
    

#문자열 인덱싱
string = 'apple'
print(string[3])

#string[2] = b -> 오류


# 각 자리의 수 합 구하기
def sum_digit(num):
    total = 0
    str_num = str(num)
    
    for digit in str_num:
        total += int(digit)

    return total


#문자열을 리스트로 변환
#num_list = []
#num_list = list(security_number)

# 리스트를 문자열로 복구
# total_str = ""
# for i in range(len(num_list)):
#    total_str += num_list[i]


#주민번호 마지막4자리를 *로 바꾸기 (모범 답안)
def mask_security_number(security_number):
    return security_number[:-4] + '****'

print(mask_security_number("880720-1234567"))

