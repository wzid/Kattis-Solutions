import sys
for n in sys.stdin:
    n = int(n)
    p = w = 1
    while p < n:
        p *= 2 + 7*w;
        w = 1 - w
    print(['Stan', 'Ollie'][w], 'wins.')