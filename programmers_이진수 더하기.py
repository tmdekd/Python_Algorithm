def solution(bin1, bin2):
    # 이진수 문자열을 정수로 변환하여 더함
    answer = int(bin1, 2) + int(bin2, 2)
    # print(answer)
    # print(bin(answer))
    
    # 이진수 변환을 위해 bin() 함수 사용하면 0b 접두사가 붙으므로 [2:]로 제거
    answer = bin(answer)[2:]
    return answer

def solution2(bin1, bin2):
    # 1. 이진수 문자열을 정수로 변환하여 더함
    answer = int(bin1, 2) + int(bin2, 2)
    
    # 2. 이진수 변환을 위해 format() 함수 사용
    answer = format(answer, 'b')
    return answer

if __name__ == "__main__":
    bin1 = "10"
    bin2 = "11"
    print(solution(bin1, bin2))  # Expected output: "101"
    print(solution2(bin1, bin2))  # Expected output: "101"