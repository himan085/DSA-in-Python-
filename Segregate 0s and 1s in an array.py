def function(arr,n):
    left=0;  right=n-1;

    while(left<right):
        while(arr[left]==0 and (left<right)):
            left+=1

        while(arr[right]==1 and (left<right)):
            right-=1

        if(left<right):
            arr[left]=0
            arr[right]=1
            left+=1
            right-=1
            

    for i in range(0,n):
        print(arr[i])


arr = [0,1,0,1,1,1,0,1,0]
n=len(arr)

function(arr,n)
