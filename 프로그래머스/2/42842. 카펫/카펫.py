def solution(brown, yellow):
    total_area = brown + yellow
    
    for height in range(3, int(total_area**0.5) + 1):
        if total_area % height == 0:
            width = total_area // height
            
            if (width - 2) * (height - 2) == yellow:
                return [width, height]