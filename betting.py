# 배팅게임 첫 시작
import random

print()
print("랜덤 배팅게임에 오신 것을 환영합니다.")
print("한 레벨을 통과하실 떄마다 배팅한 금액의 2배를 지급합니다.")
print("레벨 통과에 실패하더라도 재도전이 가능합니다.")
print("목표 금액에 빠르게 도달하여 당신의 운을 확인해보세요!")
print()
basic_payment = 5000
print(f"당신은 5000원을 지급 받았습니다.")

print()
print("=" * 50)
print("<< 1라운드 >>")
print("=" * 50)
print()

import random

while True:
    try:
        bet_1 = int(input("배팅 금액을 입력하세요. 단위: 원 >>>  "))
        if bet_1 <= basic_payment:
            payment_1 = basic_payment - bet_1
            print(f"{bet_1}원이 차감되었습니다.")
            print(f"남은 잔액: {payment_1}원")
            break
        if bet_1 > basic_payment:
            print("잔액이 부족합니다. 다시 시도해주세요.")
    except ValueError:
        print("잔액이 부족합니다. 다시 시도해주세요.")
        
money = """
1. [̲̅₩̲̅(̲̅5̲̅0̲̅0̲̅0̲̅)̲̅₩̲̅]
2. [̲̅₩̲̅(̲̅1̲̅0̲̅0̲̅0̲̅0̲̅)̲̅₩̲̅]
3. [̲̅₩̲̅(̲̅50̲̅0̲̅0̲̅0̲̅)̲̅₩̲̅]
"""

print(money)

while True:
    try:
        user_choice_1 = int(input("바닥에 돈이 떨어져 있습니다. 어느 것을 선택하시겠습니까? 1,2,3 >>>  "))

        winning_num_1 = random.randint(1,3)

        win_amount_1 = payment_1 + bet_1 *2

        if user_choice_1 == winning_num_1:
            win_amount_1 = payment_1 + bet_1 *2
            print("축하합니다! 금액 2배! 총 금액은 ",format(win_amount_1),"원 입니다.")
            break
        else:
            print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
            continue
    except ValueError:
        print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
        continue


print()
print("=" * 50)
print("<< 2라운드 >>")
print("=" * 50)
print()


while True:
    try:
        bet_2 = int(input("배팅 금액을 입력하세요. 단위: 원 >>>  "))
        if bet_2 <= win_amount_1:
            payment_2 = win_amount_1 - bet_2
            print(f"{bet_2}원이 차감되었습니다.")
            print(f"남은 잔액: {payment_2}원")
            break
        if bet_2 > win_amount_1:
            print("잔액이 부족합니다. 다시 시도해주세요.")
    except ValueError:
        print("잔액이 부족합니다. 다시 시도해주세요.")
        
mail = """
11111.
○　　 ○┤口├　　 L┤
┬ Z│　口　　 ┐├
　 　　　　ㅁ
　 　　　　┴ ㅅH ㄱㅕㄷ├┤
　　　　　 ㅅ　ㅇ  ㅅ
○　　 ○┤口├　   L┤已├
┬ Z│　口　　 ┐├　　○
　 　　　　ㄴ
　 　　　　┴ ス│ 口├ 已├┤
　　　　　 已

22222.

⎛° ͜ʖ°⎞⎠ પ ભય નુૂપ

33333.
으이구 인간아 ᕙ( ︡’︡益’︠)ง 으이구 인간아 ᕙ( ︡’︡益’︠)ง 
"""

print(mail)

while True:
    try:
        user_choice_2 = int(input("하나뿐인 동생에게 문자를 보내고 싶습니다. 어느 것을 선택하시겠습니까? 1,2,3 >>>  "))

        winning_num_2 = random.randint(1,3)

        win_amount_2 = payment_2 + bet_2 *2

        if user_choice_2 == winning_num_2:
            win_amount_2 = payment_2 + bet_2 *2
            print("축하합니다! 금액 2배! 총 금액은 ",format(win_amount_2),"원 입니다.")
            break
        else:
            print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
            continue
    except ValueError:
        print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
        continue


print()
print("=" * 50)
print("<< 3라운드 >>")
print("=" * 50)
print()


while True:
    try:
        bet_3 = int(input("배팅 금액을 입력하세요. 단위: 원 >>>  "))
        if bet_3 <= win_amount_2:
            payment_3 = win_amount_2 - bet_3
            print(f"{bet_3}원이 차감되었습니다.")
            print(f"남은 잔액: {payment_3}원")
            break
        if bet_3 > win_amount_2:
            print("잔액이 부족합니다. 다시 시도해주세요.")
    except ValueError:
        print("잔액이 부족합니다. 다시 시도해주세요.")
        
fight = """
1.
(> ” ” <)
( =’o'= )
-(,,)-(,,)-

2.
╭ ⁀ ⁀ ╮
(　 ͡° ̲̮ ͡° )
╰ ‿ ‿ ╯

3.
（;´Д｀）
（　 八)
　〉 〉

"""

print(fight)

while True:
    try:
        user_choice_3 = int(input("결투 게임 기본 캐릭터로 어떤 것을 선택하시겠습니까? 1,2,3 >>>  "))

        winning_num_3 = random.randint(1,3)

        win_amount_3 = payment_3 + bet_3 *2

        if user_choice_3 == winning_num_3:
            win_amount_3 = payment_3 + bet_3 *2
            print("축하합니다! 금액 2배! 총 금액은 ",format(win_amount_3),"원 입니다.")
            break
        else:
            print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
            continue
    except ValueError:
        print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
        continue


print()
print("=" * 50)
print("<< 4라운드 >>")
print("=" * 50)
print()


while True:
    try:
        bet_4 = int(input("배팅 금액을 입력하세요. 단위: 원 >>>  "))
        if bet_4 <= win_amount_3:
            payment_4 = win_amount_3 - bet_4
            print(f"{bet_4}원이 차감되었습니다.")
            print(f"남은 잔액: {payment_4}원")
            break
        if bet_4 > win_amount_3:
            print("잔액이 부족합니다. 다시 시도해주세요.")
    except ValueError:
        print("잔액이 부족합니다. 다시 시도해주세요.")
        
you = """
1.
두다다다다다다다
두다다다다다다다
　(∩`・ω・)
＿/_ミつ/￣￣￣/
　　＼/＿＿＿/


2.
.　　／ ⌒ヽ
　く/・*　⌒ヽ
　 |　  3  (∪￣] ⌒
　く､・　(∩￣]
￣￣￣￣￣￣￣￣￣￣


3.
.　　／＼
　く 　　ゝ
　  |　　 |
 ヽ( ´･ω･)ノ 오징오징
　 ﾉﾉ从从


"""

print(you)

while True:
    try:
        user_choice_4 = int(input("현재 당신은 어떤 모습일까요? 1,2,3 >>>  "))

        winning_num_4 = random.randint(1,3)

        win_amount_4 = payment_4 + bet_4 *2

        if user_choice_4 == winning_num_4:
            win_amount_4 = payment_4 + bet_4 *2
            print("축하합니다! 금액 2배! 총 금액은 ",format(win_amount_4),"원 입니다.")
            break
        else:
            print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
            continue
    except ValueError:
        print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
        continue


print()
print("=" * 50)
print("<< 5라운드 >>")
print("=" * 50)
print()


while True:
    try:
        bet_5 = int(input("배팅 금액을 입력하세요. 단위: 원 >>>  "))
        if bet_5 <= win_amount_4:
            payment_5 = win_amount_4 - bet_5
            print(f"{bet_5}원이 차감되었습니다.")
            print(f"남은 잔액: {payment_5}원")
            break
        if bet_5 > win_amount_4:
            print("잔액이 부족합니다. 다시 시도해주세요.")
    except ValueError:
        print("잔액이 부족합니다. 다시 시도해주세요.")
        
pet = """
1. 강아지
．．．．．/)─―ヘ
　　　━／　　　　＼
　 ／　　    　　●　　●丶
　｜　　　　　　　▼　| 
　｜　　　　    　　　亠ノ 　
　 U￣U￣￣￣U￣￣U


2. 알파카
　　 　　　　　　|＼＿/|  
　　  　　　　　 |・x・|  
　　＼＿＿＿＿＿／　　　| 
　 　|　　　 　　　　　|  
 　　＼　　　　    　ノ　  
（（（　(/￣￣￣￣(/ヽ)


3. 말
　/)/) 　 ∧,,∧
.／・　 ﾐ(＾ο＾)
(＿ノ＼　ﾐ⊂　)
　　　(　 .しﾉ⌒)～
　　　 .ＵJ~ＵJ


"""

print(pet)

while True:
    try:
        user_choice_5 = int(input("집에서 동물을 키우게 됐습니다. 어떤 동물과 지낼까요? 1,2,3 >>>  "))

        winning_num_5 = random.randint(1,3)

        win_amount_5 = payment_5 + bet_5 *2

        if user_choice_5 == winning_num_5:
            win_amount_5 = payment_5 + bet_5 *2
            print("축하합니다! 금액 2배! 총 금액은 ",format(win_amount_5),"원 입니다.")
            break
        else:
            print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
            continue
    except ValueError:
        print("아쉽네요. 배팅에 실패했습니다. 당신은 오늘 운이 없군요. 다시 선택하세요.")
        continue

print()
print("=" * 50)
print("당신이 보유한 총 금액은 ",format(win_amount_5),"원 입니다.")
print("당신은 ",format(win_amount_5),"원으로 ",win_amount_5//5000,"장의 복권을 살 수 있습니다.")
print("=" * 50)

print()
print("고생한 당신에게 랜덤 로또 번호를 추첨해 드립니다.")
print()


import random

def generate_lotto_numbers():
    numbers = list(range(1, 45))
    lotto_numbers = random.sample(numbers, 6)
    return sorted(lotto_numbers)

def main():
    print("로또 번호 추첨을 시작합니다.")
    num_of_tickets = int(input("몇 세트의 로또 번호를 추천해드릴까요? "))

    for _ in range(num_of_tickets):
        lotto_numbers = generate_lotto_numbers()
        print("추첨된 로또 번호: ", lotto_numbers)

if __name__ == '__main__':
    main()


print()
print("당신의 즐거운 삶을 응원합니다!")