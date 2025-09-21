def solution(price, money, count):
    answer = -1
    total_cost = 0
    for i in range(count + 1):
        total_cost += price * i
    
    if money >= total_cost:
        answer = 0
    else:
        answer = total_cost - money
    return answer

if __name__ == "__main__":
    price = 3
    money = 20
    count = 4
    print(solution(price, money, count))  # 10