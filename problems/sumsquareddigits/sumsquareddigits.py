def solution(num, base) -> int:
    result = 0
    while num > 0:
        remainder = num % base
        result += remainder * remainder
        num //= base
    return result


cases = int(input())
for i in range(cases):
    case_num, base, num_as_dec = map(int, input().split())
    print(case_num, solution(num_as_dec, base))