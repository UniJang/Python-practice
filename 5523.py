import sys

N = int(sys.stdin.readline())
Awin, Bwin = 0, 0
for _ in range(N):
    A, B = sys.stdin.readline().split()
    if A < B: Bwin += 1
    elif A > B: Awin += 1
print(Awin, Bwin)