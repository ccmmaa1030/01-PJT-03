import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())                        # 테스트케이스 개수

for test_case in range(1, T+1):
    bdpq = input()                      # b,d,p,q로 이루어진 문자열
    reverse = bdpq[::-1]                # 문자열 뒤집기
    mirror = ''

    for i in reverse:                   # 뒤집은 문자열
        if i == 'b':
            mirror += 'd'               # b이면 거울상은 d 추가
        elif i == 'd':
            mirror += 'b'               # d이면 거울상은 b 추가
        elif i == 'p':
            mirror += 'q'               # p이면 거울상은 q 추가
        else:
            mirror += 'p'               # q이면 거울상은 p 추가
    
    print(f'#{test_case} {mirror}')     # 거울상 출력
