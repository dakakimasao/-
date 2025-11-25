import pandas as pd

from calml import predict
from makespider import msg
import userdb
from makeml import makeml

data1=pd.read_excel('epl22.xlsx')
data2=pd.read_excel('epl23.xlsx')
game=pd.read_excel('epl24.xlsx')

alldata=pd.concat([data1,data2],ignore_index=True)
makeml(alldata)

gamecol=['HomeTeam','AwayTeam','B365H','B365D','B365A']

databasefile='toto.db'
makedbb=userdb.setup(databasefile)

while True:
    username = input('성함을 입력하세요')
    bal = userdb.checkuser(username, databasefile)
    bal=bal
    if bal==0:
        print('도박 그만 하세요잉')
        break
    betbetmoney=int(input('배팅금을 입력해주세요'))
    if bal<betbetmoney:
        print('잔금보다 더 큰 금액을 배팅 하셧습니다 종료합니다.')
        break
    elif bal>=betbetmoney:
        print('사장님 도박은 재미로 하셔야 합니다.')

        randomgame = game.sample(1)
        rdnum=randomgame.index

        print(randomgame[gamecol])

        home=randomgame['HomeTeam'].item()
        away=randomgame['AwayTeam'].item()


        msg(alldata,home,away)
        mlresult=predict(randomgame)

        totoresult=randomgame['HTR'].item()
        print(f'그래프를 보셧나요 {mlresult}가 머신러닝 분석 결과 입니다.')

        betmoney=0
        totosel=int(input(f'''
{home} VS {away}의 승 무 패를 예측 하세요 
홈승 = 2 무 = 1 원정승 = 0 
게임을 그만 하시려면 
2,1,0 제외 아무거나 입력하세요
숫자 입력: '''))

        if totosel==2:
            totosel='H'
        elif totosel==1:
            totosel='D'
        elif totosel==0:
            totosel='A'
        else:
            print('게임을 그만 합니다.')
            break
        if totoresult=='H':
            betmoney=randomgame['B365H'].item()
        elif totoresult=='D':
            betmoney=randomgame['B365D'].item()
        else:
            betmoney=randomgame['B365A'].item()

        if totosel==totoresult:
            print('축하합니다. 맞추셧습니다.')
            betchangemoney=betbetmoney*betmoney
            bal=userdb.updatebal(username,betchangemoney,databasefile)
        else:
            print('저런.... 도박엔 재능이 없으시네요.')
            betchangemoney = -betbetmoney
            bal=userdb.updatebal(username,betchangemoney,databasefile)
