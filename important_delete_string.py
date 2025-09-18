# 문자열 a와 b 입력
a = input("문자열 a 입력: ")
b = input("문자열 b 입력: ")

# 문자열 b에서 a 확인 및 삭제
if a in b:  # a가 b에 포함되어 있는지 확인
    # replace() 메서드 사용법:
    # b.replace(old, new, count)
    # - old: 바꾸고자 하는 기존 문자열 (여기서는 a)
    # - new: 바꿀 새로운 문자열 (여기서는 빈 문자열 "")
    # - count (선택): 바꿀 횟수 (1이면 한 번만 바꿈)
    b = b.replace(a, "", 1)  # a를 b에서 한 번만 삭제
    print(f"문자열 a를 삭제한 결과: {b}")
else:
    print(f"문자열 a({a})는 문자열 b({b})에 포함되어 있지 않습니다.")
