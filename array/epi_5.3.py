# my initial attempt

def product_array(arr1, arr2):
    offset = 0
    answer = [0] * (len(arr1) + len(arr2))
    for i in range(1, len(arr1) + 1):
        carry = 0
        for j in range(1, len(arr2) + 1):
            curr = abs(arr1[-i]) * abs(arr2[-j]) + carry
            if curr < 10:
                answer[-j - offset] += curr
            else:
                answer[-j - offset] += curr % 10
                carry = curr // 10
        answer[-len(arr2) - 1 - offset] += carry
        offset += 1
    for index in range(len(answer)):
        curr = answer[-index]
        if curr > 9:
            answer[-index] = curr % 10
            answer[-index - 1] += curr // 10
    if answer[0] == 0:
        answer = answer[1:]
    if arr1[0] <= 0 or arr2[0] <= 0:
        answer[0] = -answer[0]
    return answer

print(product_array([1,1], [2,0]))
print(product_array([9,8,7], [9,8,7]))
print(product_array([1,9,3,7,0,7,7,2,1], [-7,6,1,8,3,8,2,5,7,2,8,7]))
print(product_array([-2, 3, 5], [2]))
print(product_array([8,8,8,8,8,8,8], [-1,1,1,1,1,1]))
print(product_array([7,7,2,1], [7,2,8,7]))
