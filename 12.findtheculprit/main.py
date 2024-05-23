# 도둑 잡기 게임_층수 맞추기

import random
from art import logo
print(logo)

def story(difficulty):
  if difficulty == "상":
    print("당신은 살인을 저지른 범인을 찾는 경찰입니다. 범인은 지금 [150층]짜리 높은 빌딩으로 도주하여 또 다시 살인을 계획하고 있습니다. 당신은 범인이 몇층으로 도주하였는지 찾아야 합니다.\n")
  elif difficulty == "중":
    print("당신은 뺑소니를 저지르고 도주한 범인을 찾는 경찰입니다. 범인은 지금 [100층]짜리 높은 빌딩으로 도주하여 세상이 조용해지기만을 기다리고 있습니다. 당신은 범인이 몇층으로 도주하였는지 찾아서 엄벌을 내려야합니다.\n")
  else:
    print("당신은 지금 좀도둑을 쫓고 있는 경찰입니다. 범인은 지금 [50층]짜리 빌딩으로 도주하여 숨어있습니다. 당신은 범인이 몇층으로 도주하였는지 찾아야 합니다.\n")

#난이도별 최상층 선택
def floor_list(difficulty):
  floor = []
  if difficulty == "상":
    for i in range(1, 151):
      floor.append(i)
    return floor
  elif difficulty == "중":
    for i in range(1, 101):
      floor.append(i)
    return floor
  else:
    for i in range(1, 51):
      floor.append(i)
    return floor

#난이도별 게임 진행 횟수
def coin_count(difficulty):
  if difficulty == "상":
    return 5
  elif difficulty == "중":
    return 10
  else:
    return 10

#층수 랜덤 선정
def pick_number(floor):
  return random.choice(floor)

#답변 체크
def check_answer(answer, floor_number, coin):
  if answer != floor_number:
    coin -= 1
    if answer < floor_number:
      print(f"범인이 {answer}층보다 높은 층으로 도망갔다는 제보가 있었습니다. {coin}의 기회가 남았습니다.\n")
      if coin == 0:
        print("범인은 도주하였습니다. 세상은 죄로 물듭니다.")
    elif answer > floor_number:
      print(f"범인이 {answer}층보다 아래 층으로 도망갔다는 제보가 있었습니다. {coin}의 기회가 남았습니다.\n")
      if coin == 0:
        print("범인은 도주하였습니다. 세상은 죄로 물듭니다.")
    return coin
  else:
    print("범인을 검거했습니다.")
    print(f"범인은 {floor_number}층에 숨어있었습니다.")
    print("축하드립니다")
    return 0

#게임 시작
state = True

while state is True:
  #게임 난이도 선택
  difficulty = input("게임을 시작하겠습니다. 난이도를 골라주세요. [상] [중] [하] 난이도 입력: ")

  #게임 스토리 진행
  story(difficulty)
  #도망간 층 정하기
  floor = floor_list(difficulty)
  #게임 횟수
  coin = coin_count(difficulty)
  print(f"당신은 {coin}번의 기회가 주어집니다. 더 큰 범죄가 발생하지 않도록 범인을 꼭 잡아주세요!\n")
  #도망간 층수 결정
  floor_number = pick_number(floor)

  while coin is not 0:
    #정답 체크
    answer = int(input("범인은 몇 층으로 도망갔을까요?"))
    coin = check_answer(answer, floor_number, coin)
    if coin == 0:
      state = False
      restart = input("게임을 다시 하시겠습니까? [Y] [N] : ").lower()
      if restart == "y":
        state = True
      else:
        print("게임을 종료합니다.")
