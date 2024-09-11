# 로또 시뮬레이션 실습

from random import randint

def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers

# 테스트 코드
print(generate_numbers(6))



def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


# 테스트 코드
print(draw_winning_numbers())


# 내 코드: i=0; j=0 -> 반복문 2번 사용 -> 비효율적
def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count = count + 1

    return count


# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))


# 해당 코드는 내 코드(모범과 일치)
def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    count = count_matching_numbers(numbers, winning_numbers[:6])
    count_b = count_matching_numbers(numbers, winning_numbers[6:])
    if count==6:
        return 1000000000
    elif count==5 and count_b==1:
        return 50000000
    elif count==5:
        return 1000000 
    elif count==4:
        return 50000
    elif count==3:
        return 5000
    else:
        return 0
# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))




#########################################################


#숫자 야구
from random import randint


def generate_numbers():
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    numbers = []

    # 여기에 코드를 작성하세요
    while len(numbers)!=3:
        num = randint(0,9)
        if num not in numbers:
            numbers.append(num)
            
    return numbers

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_num)

    return new_guess


def get_score(guesses, solution):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    strike_count = 0
    ball_count = 0

    # 여기에 코드를 작성하세요
    for i in guesses:
        if i in solution:
            if solution.index(i) == guesses.index(i):
                strike_count += 1
            else:
                ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 여기에 코드를 작성하세요
while True:
    GUESS = take_guess()
    strike, ball = get_score(GUESS, ANSWER)
    tries += 1
    if strike==3:
        break
    print("{}S {}B".format(strike, ball))

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))