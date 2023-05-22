import socket
from _thread import *
import os
import sys
sys.path.append(r'C:\Users\jongh\소공\SE-22Team')
sys.path.append(r'{}'.format(os.getcwd()))
import time

import pickle

join = False

def start_server(pw):
    server = "10.50.99.56"
    port = 5555
    password = pw

    #소켓 생성
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 소켓 바인딩
    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    # 소켓 리스닝
    s.listen(5)
    print("Waiting for a connection, Server Started")

    from Data.GAME_LOGIC.uno_Player import Player
    players = [Player("cli1", True), Player("cli2", True)]
    
    # 입출력 테스트를 위한 샘플 handlist 1번, 2 번
    players[0].handCardList = ["1번 플레이어 카드리스트"]
    players[1].handCardList = ["2번 플레이어 카드리스트"]
    print("players handlist init")

    # 이 부분과 player 부분이 관련있음
    currentPlayer = 0

    while True:
        print("true")
        # 클라이언트가 접속 요청시 accept 함수를 통해 연결 수락
        conn, addr = s.accept()
        print("연결됨 : ", addr)
        print("클라이언트 JOIN 버튼 클릭")
        global join
        join = True

        start_new_thread(threaded_client, (conn, ))
        
        currentPlayer += 1
        print("현재 플레이어 : ", currentPlayer)


def threaded_client(conn):
    #conn.send(pickle.dumps())
    reply = ""

    while True:
        print("while True")
        try:
            from Data.GAME_VIEW.SCREEN.multi_mode_set import server_pw
            reply = server_pw
            print(reply)
            conn.sendall(pickle.dumps(reply))
            print("try")
            time.sleep(1)
            data = pickle.loads(conn.recv(2048))
            print(conn.recv(2048))
            print(data)
            # players[player] = data

            # socket_queue.put(data)

            if not data:
                print("연결불가")
                break
            else:
                pass
            
            
            print("보냄")
    
        except:
            break
    
    print("연결 종료")
    conn.close()
    sys.exit()


