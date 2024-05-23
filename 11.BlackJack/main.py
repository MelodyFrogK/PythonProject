from art import logo
from replit import clear
import random


#1.카드 뽑기
def first_draw_card(deck, player_deck, dealer_deck):
  for draw in range(2):
    player_deck.append(deck.pop())
    dealer_deck.append(deck.pop())
  print("Player's deck: ", end="")
  for position in range(len(player_deck)):
    print(f"[{player_deck[position]}] ", end="")
  print(f"\ndealer's deck: [{dealer_deck[1]}]")


#2.추가 플레이어 카드 뽑기
def draw_card(deck, player_deck):
  card_state = True
  while card_state is True:
    add_card = input("카드를 한장 더 받으시겠습니까? (y/n) 선택: \n")
    if add_card == "y":
      player_deck.append(deck.pop())
      #카드 핪이 21이 넘으면 게임오버
      player_result = 0
      #플레이어 합계 연산
      for position in range(len(player_deck)):
        if player_deck[position] in alpabet_dic:
          player_deck[position] = alpabet_dic[player_deck[position]]
        player_result += player_deck[position]
      #"A"카드 숫자 바꾸기
      if player_result > 21 and 11 in player_deck:
        player_deck.remove(11)
        player_deck.append(1)
        print(f"Player's deck: {player_deck}", end="\n")
      elif player_result > 21:
        print("💣💣Player Bust💣💣")
        card_state = False
      else:
        print(f"Player's deck: {player_deck}", end="\n")

    else:
      card_state = False
      print("게임을 결과를 확인합니다❤😍🃏")


#3.카드 점수 확인
def score_card(deck):
  result = 0
  #합계 연산
  for position in range(len(deck)):
    if deck[position] in alpabet_dic:
      deck[position] = alpabet_dic[deck[position]]
    result += deck[position]
  return result


#4. 카드 점수 비교
def compare_result(player_result, dealer_result):
  #결과 출력
  print(f"플레이어 카드합계: {player_result}")
  print(f"딜러 카드합계: {dealer_result}")
  if player_result == 21 and len(player_deck) == 2:
    print("🃏🃏Black Jack!! 플레이어 승리!🃏🃏")
  elif 21 >= player_result > dealer_result:
    print("🎇🎇플레이어 승리🎇🎇")
  elif player_result == dealer_result:
    print("⚖⚖무승부⚖⚖")
  else:
    print("😭😭플레이어 패배😭😭")


#Start: 게임 시작
play_state = True
start = input("♠♣블랙잭의 세계에 오신 것을 환영합니다.♥♦ 게임을 시작하시기 원하십니까?🎰 (y/n) 답:")
if start == "y":
  while play_state is True:
    print(logo)
    print("블랙잭 게임을 시작합니다.\n")
    #덱 수 13 * 4(스페어, 하트, 클로버, 다이아몬드)
    deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4
    alpabet_dic = {"A": 11, "J": 10, "Q": 10, "K": 10}
    player_deck = []
    dealer_deck = []
    #카드 섞기
    random.shuffle(deck)
    #카드 뽑기 실행
    first_draw_card(deck, player_deck, dealer_deck)
    #카드 추가 뽑기 실행
    draw_card(deck, player_deck)
    
    #카드 점수 확인
    player_result = score_card(player_deck)
    dealer_result = score_card(dealer_deck)
    
    #딜러 추가 뽑기 실행
    while dealer_result != 0 and dealer_result < 17:
      dealer_deck.append(deck.pop())
      dealer_result = score_card(dealer_deck)

    #플레이어와 딜러 카드 값 비교
    compare_result(player_result, dealer_result)

    #재시작
    re = input("게임을 다시 시작하시겠습니까? (y/n) 선택: \n")
    if re == "y":
      clear()
    else:
      play_state = False
      print("💣💣Game Over💣💣")
else:
  clear()
  print("게임을 종료합니다.")
