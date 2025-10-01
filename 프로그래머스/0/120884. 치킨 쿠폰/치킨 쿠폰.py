def solution(chicken):
    answer = 0
    coupon = 0
    for i in range(chicken):
        coupon += 1
        if coupon == 10:
            coupon = 1
            answer += 1
    coupon += (coupon/10)
    print(coupon)
            
    return answer