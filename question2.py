#================================================================
#================================================================
#이름 잘못 줬습니다. 저는 후슬렝_20241773입니다.
# 물건 정보
items = [
    ("", 0, 0),                 
    ("노트북", 3, 12),
    ("카메라", 1, 10),
    ("책", 2, 6),
    ("옷", 2, 7),
    ("휴대용 충전기", 1, 4)
]
# 물건 개수
n = 5  

# 배낭 용량 입력
W = int(input("배낭 용량을 입력 하세요 : "))

# DP 테이블 생성
# A[i][w] ==> i번째 물건까지 고려했을 때 용량 w에서의 최대 만족도
A = [[0] * (W + 1) for _ in range(n + 1)]

# Bottom-up 방식으로 DP 테이블 채우기
for i in range(1, n + 1):
    name, weight, value = items[i]
    for w in range(W + 1):
        if weight <= w:
            A[i][w] = max(
                A[i - 1][w],                 
                A[i - 1][w - weight] + value 
            )
        else:
            A[i][w] = A[i - 1][w]

# 최대 만족도
max_value = A[n][W]
print(f"\n최대 만족도: {max_value}")

# 선택한 물건 역추적
selected_items = []
w = W

for i in range(n, 0, -1):
    if A[i][w] != A[i - 1][w]:
        selected_items.append(items[i][0])
        w -= items[i][1]

selected_items.reverse()

print("선택된 물건:", selected_items)

# 물건 목록 출력
print("\n물건 목록")
print("번호\t물건 이름\t무게\t만족도")
for i in range(1, n + 1):

    print(f"{i}\t{items[i][0]}\t{items[i][1]}\t{items[i][2]}")
