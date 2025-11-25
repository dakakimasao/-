import sqlite3

def checkuser(username,userdb):
    conn = sqlite3.connect(userdb)
    cur = conn.cursor()
    username=username
    cur.execute("SELECT bal FROM wallets WHERE username=?",(username,))
    result = cur.fetchone()

    if result:
        bal = result[0]
        print(f'{username}님 환영합니다. 현재 잔액은{bal}원 입니다.')
        return bal
    else:
        stbal=10000
        cur.execute("INSERT INTO wallets (username,bal) VALUES (?,?)",(username,stbal))
        conn.commit()
        print(f'{username}님 신규 가입을 환영합니다. 도박은 적당히 하세요 초기 금액 10000원 입금되었습니다.')
        return stbal
def setup(userdb):
    conn = sqlite3.connect(userdb)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS wallets(username TEXT PRIMARY KEY NOT NULL,bal REAL NOT NULL)''')
    conn.commit()
    conn.close()

def updatebal(username,changemoney,userdb):
    conn = sqlite3.connect(userdb)
    cur = conn.cursor()

    cur.execute(
        "UPDATE wallets SET bal = bal + ? WHERE username = ?"
        ,(changemoney, username))
    conn.commit()  # 변경사항 저장 필수
    conn.close()