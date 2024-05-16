from replit import clear
from art import logo

#게임 로고
print(logo)

#경매 참가자 딕셔너리
bidders = {}
name = ()
bid = ()
stop = False


#경매 입찰자 추가 함수
def add_bidder(name, bid):
  bidders[name] = bid


#경매 입찰자 정보 확인 및 승리자 선정 함수
def winner():
  highest_bid = 0
  winner = ""
  for bidder in bidders:
    bid_amount = bidders[bidder]
    if int(bid_amount) > int(highest_bid):
      highest_bid = bid_amount
      winner = bidder
  print(f"입찰자는 최고가액 ${highest_bid}를 제시하신 {winner}님이십니다. 축하드립니다.")


#경매 입찰자 정보 입력 및 추가 함수 호출
while stop is False:
  name = input("What is your name? \nName: ")
  bid = input("how much do you want to bid?\n$")
  add_bidder(name, bid)
  answer = input("더 참가하실 입찰자 계십니까? Type 'yes' or 'no'.\n")
  if answer == 'no':
    stop = True
  else:
    clear()
    print(logo)

#경매 승리자 선정 및 출력
clear()
print(logo)
winner()
