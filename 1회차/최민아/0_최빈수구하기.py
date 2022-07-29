import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())                                        # 테스트케이스 개수

for test_case in range(1, T+1):
    n = int(input())                                    # 현재 테스트케이스
    
    grade = list(map(int, input().split()))             # 성적 리스트
    max_score = 0                                       # 최빈수 초기값
    
    for score in range(101):                            # 0점부터 100점까지
        if grade.count(score) > grade.count(max_score): # 해당 점수의 개수 비교
            max_score = score                           # 최빈수 갱신
    
    print(f'#{n} {max_score}')                          # 최빈수 출력
