def check(arr,n,key):
    arr.sort()

    for i in range(0,n-2):
        l=i+1
        r=n-1
        while(l<r):
            if(arr[i]+arr[l]+arr[r]==key):
                return 1
            if(arr[i]+arr[l]+arr[r]>key):
                r-=1
            else:
                l+=1

    return 0


arr=[6,4,45,8,8,1]
key=19
ans = check(arr,len(arr),key)
if (ans):
    print('YES')
else:
    print('NO')
    
