import sys
from tkinter import N

sys.stdin = open("_암호문1.txt")

T = 10                                      # 10개의 테스트케이스
for test_case in range(1, T+1):
    code_len = int(input())                 # 원본 암호문 길이
    code = list(input().split())            # 원본 암호문 리스트
    cmd_cnt = int(input())                  # 명령어 개수
    cmd = list(input().split())             # 명령어 리스트

    x = 0
    y = 0
    s = 0
    for i in range(len(cmd)):               # 명령어 처음부터 끝까지
        if cmd[i] == "I":                   # 명령어가 I이면
            x = int(cmd[i+1])               # 삽입 위치
            y = int(cmd[i+2])               # 삽입 개수
            s = i+3                         # 삽입할 암호 인덱스
            while True:
                code.insert(x, cmd[s])      # 원본 암호문 x 위치에 암호 삽입
                if s == i+2+y:              # i+2+y : 마지막 암호 인덱스
                    break                   # y개 삽입하면 반복문 탈출
                x += 1                      # 다음 위치
                s += 1                      # 다음 암호 인덱스
    
    print(f'#{test_case}', end=' ')
    for i in range(10):                     # 처음부터 10개
        print(code[i], end=' ')             # 수정된 암호문에서 출력
    print()                                 # 10개 출력하면 줄바꿈