import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())                                # 테스트케이스 개수

for test_case in range(1, T+1):
    N = int(input())                            # N명
    income = list(map(int, input().split()))    # N명의 소득 리스트
    
    income_avg = sum(income) / N                # 평균 소득
    avg_down = 0                                # 평균 이하인 사람 수 초기값

    for i in range(N):
        if income[i] <= income_avg:             # 현재 사람의 수입이 평균 이하이면
            avg_down += 1                       # 평균 이하인 사람 수 1증가

    print(f'#{test_case} {avg_down}')           # 평균 이하인 사람 수 출력
