# Problem: A - Your Hackathon Project - Chat Feature - https://codeforces.com/gym/534160/problem/A

for _ in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for i in range(len(s) - 1,-1,-1):
        if s[i]==')':
            count += 1
        else:
            break
    if count > (len(s) - count):
        print("Yes")
    else:
        print("No")