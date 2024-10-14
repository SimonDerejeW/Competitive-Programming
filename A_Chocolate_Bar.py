for _ in range(int(input())):
    n , l , r , k = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    nums.sort()

    count = 0
    started = False
    for num in nums:
        if num >= l and num <= r and num <= k:
            count += 1
            k -= num
            started = True
        elif started is True:
            break
        
    print(count)