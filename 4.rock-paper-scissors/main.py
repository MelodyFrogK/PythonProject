rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

charactor = ["바다", "쿠로", "산미", "마에스트로", "장기에프", "헤이아치"]

user_choise = int(input('죽음의 가위 바위 보 게임에 참가하신 것을 환영합니다. \n당신에게 3가지 선택권을 드릴 것입니다. \n제가 준비한 것은 바로 [가위], [바위], [보] 입니다. 놀라실 것 없습니다. 선택하세요!\n 가위는 0, 바위는 1, 보는 2를 입력하세요.\n 당신의 선택은: '
    ))

print('당신의 선택\n')
if user_choise == 0:
    print(scissors)
elif user_choise == 1:
    print(rock)
else:
    print(paper)

#캐릭터 네임 선택
charactor_num = random.randint(0, 5)
rd_charactor_name = charactor[charactor_num]
#캐릭터 공격 타입 선택
charactor_att_type = random.randint(0, 2)

print(f'{rd_charactor_name}의 선택')
if charactor_att_type == 0:
    print(scissors)
elif charactor_att_type == 1:
    print(rock)
else:
    print(paper)

#승패 결정
if (user_choise == 0 and charactor_att_type
        == 0) or (user_choise == 1 and charactor_att_type
                  == 1) or (user_choise == 2 and charactor_att_type == 2):
    print('비겼습니다.\nRetry')

elif (user_choise == 0
      and charactor_att_type == 1) or (user_choise == 1 and charactor_att_type
                                       == 2) or (user_choise == 2
                                                 and charactor_att_type == 0):
    print('당신이 졌습니다.\nGameOver')

else:
    print('당신이 이겼습니다.\nend')
