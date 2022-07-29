import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())                            # 테스트케이스 개수

for test_case in range(1, T+1):
    num = list(map(int, input().split()))   # 16번째 자리수 제외 신용카드 숫자 리스트

    LUHN = 0
    for i in range(15):                     # 15자리 순서대로
        if i % 2 == 1:                      # 짝수자리
            LUHN += num[i]                  # 그대로 더하기
        else:                               # 홀수자리
            LUHN += num[i] * 2              # 2배해서 더하기

    answer = 0                              # 16번째 자리수
    for N in range(10):                     # 0부터 9까지
        if (LUHN + N) % 10 == 0:            # LUHN + N 값이 10으로 나누어 떨어지면
            answer = N                      # 답은 N

    print(f'#{test_case} {answer}')         # 16번째 자리수 출력