from random import randint

# 0~9 사이 무작위 추출
def rand_num():
    num_list = []
    while len(num_list)!=3:
        num = randint(0,9)
        if num not in num_list:
            num_list.append(num)
            
    return num_list


def num_check(n1, guess, ord):
    if n1<0 or n1>9:
        print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        return ord
    elif n1 in guess:
        print("중복되는 숫자 입니다. 다시 입력하세요.")
        return ord
    guess.append(n1)
    ord += 1
    return ord
    

def strike_ball(c_list, g_list, s, b):
    for i in g_list:
        if i in c_list:
            if c_list.index(i) == g_list.index(i):
                s += 1
            b += 1
    print("{}S {}B". format(s, b))




correct = rand_num()
strike = 0; ball = 0
print("숫자 3개를 하나씩 차례대로 입력하세요.")

while strike !=3 :

    order = 1
    guess_list = []
    while order <= 3:
        num = int(input("{}번째 숫자를 입력하세요: ".format(order)))
        order = num_check(num, guess_list, order)
    strike_ball(correct, guess_list, strike, ball)
    

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다". format())