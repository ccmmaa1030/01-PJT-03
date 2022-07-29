import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())                        # 테스트케이스 개수

for test_case in range(1, T+1):
    answer = 1                          # 발급 가능이면 1
    
    num = input().replace('-', '')      # 입력받은 값에서 -을 공백으로 바꾸어 제거
    if len(num) != 16:                  # 입력받은 값이 - 제외 16자리가 아니면
        answer = 0                      # 발급 불가로 0
    
    if num[0] not in '34569':           # 입력받은 값 첫 자리수가 3,4,5,6,9가 아니면 
        answer = 0                      # 발급 불가로 0
    
    print(f'#{test_case} {answer}')     # 가능여부 출력