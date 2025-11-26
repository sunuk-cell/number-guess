import random

print("=== 숫자 맞추기 게임 ===")
print("1~100 사이의 숫자를 맞춰보세요!")

# 컴퓨터가 1~100 사이의 숫자 선택
target = random.randint(1, 100)
attempts = 0  # 시도 횟수 저장

while True:
    try:
        guess = int(input("숫자 입력: "))
        attempts += 1

        if guess < target:
            print("👉 더 큰 숫자!")
        elif guess > target:
            print("👉 더 작은 숫자!")
        else:
            print(f"🎉 정답! {attempts}번 만에 맞췄습니다!")
            break
    
    except ValueError:
        print("숫자를 입력해야 해요!")
