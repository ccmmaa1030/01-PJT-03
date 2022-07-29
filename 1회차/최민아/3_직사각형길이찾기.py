import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())                                # 테스트케이스 개수

for test_case in range(1, T+1):
    length = list(map(int, input().split()))    # 3변의 길이 리스트
    length.sort()                               # 오름차순 정렬

    if length[0] == length[1]:                  # 0번과 1번 길이가 같으면
        answer = length[2]                      # 나머지 변은 2번과 같음
    else:
        answer = length[0]                      # 같지 않으면 0번과 같음
    
    print(f'#{test_case} {answer}')             # f-string으로 지정