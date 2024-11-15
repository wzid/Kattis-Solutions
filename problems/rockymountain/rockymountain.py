

ii = lambda:int(input())
mii = lambda:list(map(int, input().split()))

n = ii()

peaks = []

def get_slope(mid, this):
    y = abs(this[1]-mid[1])
    x = abs(this[0]-mid[0])
    return (y,x)

def get_cross(first, second):
    return (first[0]*second[1], first[1]*second[0])

middle = -1
m = 0
for i in range(n):
    a,b = map(int, input().split())

    if b > m:
        m = b
        middle = i
    peaks.append((a,b))
# print(peaks[middle])

bestLeft = middle
slope = (10**10,1)
for i in range(middle-1, -1, -1):
    thisS = get_slope(peaks[middle], peaks[i])
    # print(peaks[i], thisS)
    a,b = get_cross(slope, thisS)

    if a >= b:
        slope = thisS
        if peaks[i][1] <= peaks[bestLeft][1]:
            bestLeft = i

bestRight = middle
slope = (10**10,1)
for i in range(middle+1, n):
    thisS = get_slope(peaks[middle], peaks[i])
    # print(peaks[i], thisS)
    a,b = get_cross(slope, thisS)

    if a >= b:
        slope = thisS
        if peaks[i][1] <= peaks[bestRight][1]:
            bestRight = i

print(*peaks[bestLeft])
print(*peaks[bestRight])