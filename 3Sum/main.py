from collections import defaultdict

def ThreeMumberSum(mums,target):
    twonum=[]
    dict={}

    for j in range(0,len(nums)):
        length=len(nums)
       
        target2 = target-nums[j]
        sublist = nums.copy()
        del sublist[j]

        if target2 in sublist:
            print('found')
            twonum.append(nums[j])
            twonum.append(target2)
    
    return twonum
        

        


if __name__=='__main__':
    print('inside main')
    nums=[12,3,1,2,-6,5,-8,6]
    
   
    target=0

    for i in range(0,len(nums)):
        arr = nums.copy()
        del arr[i]
        target1= target-nums[i]
        print(target1)
        arr = nums.copy()

        res=ThreeMumberSum(arr,target1)
        res.append(arr[i])

        print(res)
       

  
   
    
    
       



    