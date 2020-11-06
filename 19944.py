N, M = input().split()
if int(M) < 3:
    print("NEWBIE!")
elif int(M) <= int(N):
    print("OLDBIE!")
else:
    print("TLE!")