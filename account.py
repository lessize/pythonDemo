
class AccountExecption(Exception):
  def __init__(self, errmsg):
    self.errmsg = errmsg
  # 객체의 상태를 문자열로 표현하는 메소드 __str__
  # print(), str() 사용 시 객체의 상태를 문자열로 출력해준다
  def __str__(self):
    return self.errmsg

class Account:
  pass

  # 생성자
  def __init__(self):
    self.balance = 0

  # 입금
  def deposit(self, money):
    if money > 40000 :
      # print("1회 입금 한도는 4만원을 초과할 수 없습니다.")
      raise AccountExecption("1회 입금 한도는 4만원을 초과할 수 없습니다.")

    self.balance += money

  # 출금
  def withdraw(self, money):
    if money > 40000 :
      # print("1회 출금 한도는 4만원을 초과할 수 없습니다.")
      raise AccountExecption("1회 출금 한도는 4만원을 초과할 수 없습니다.")

    # 마이너스 잔고 체크
    if self.balance - money < 0:
      # print(f"잔액이 부족합니다. 현재 잔액  {self.balance}")
      raise AccountExecption(f"잔액이 부족합니다. 현재 잔액  {self.balance}")

    self.balance -= money

  # 잔액조회
  def getBalance(self):
    return self.balance

account = Account()

stop = False
while not stop :
  try:
    print("*" * 35)
    print(" 1.입금 2.출금 3.잔액조회 4.종료")
    print("*" * 35)
    menu = input("메뉴 선택 : ")
    match menu:
      case "4":
        stop = True
        break;

      case "1":
        money = int(input("입금액 : "))
        account.deposit(money)

      case "2":
        money = int(input("출금액 : "))
        account.withdraw(money)

      case "3":
        print("잔액조회")
        print(f'잔액 : {account.getBalance()}')

      case "5" | "6" | "7" :
        print("5, 6, 7")

      case _ :
        print("1~4 중에서 선택하세요.")

  except AccountExecption as e :
    print(e)
  else:
    continue