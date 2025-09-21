def solution(order):
    answer = 0
    for item in order:
        if 'americano' in item or item == 'anything':
            answer += 4500
        elif 'cafelatte' in item:
            answer += 5000
    return answer

if __name__ == "__main__":
    order = ["cafelatte", "americanoice", "hotcafelatte", "anything"]
    print(solution(order))  # 19000