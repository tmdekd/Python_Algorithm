def solution(my_string):
    answer = []
    count = [0] * 52  # 알파벳 대문자 26개, 소문자 26개
    for char in my_string:
        if 'A' <= char <= 'Z':  # 대문자
            # ord() 함수를 이용해 문자에 해당하는 인덱스 계산
            # 대문자는 0~25 인덱스를 사용하기 위해 - ord('A')
            # 'A'를 0으로 맞추기 위해 ord('A')를 뺌
            index = ord(char) - ord('A')
        elif 'a' <= char <= 'z':  # 소문자
            # ord() 함수를 이용해 문자에 해당하는 인덱스 계산
            # 소문자는 대문자 인덱스 뒤에 위치시키기 위해 +26
            index = ord(char) - ord('a') + 26
        count[index] += 1
        
    answer = count
    return answer

if __name__ == "__main__":
    my_string = "Programmers"
    print(solution(my_string))  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]