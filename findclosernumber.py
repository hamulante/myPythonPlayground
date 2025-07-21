def findclosernumber(nums_str,target):
    nums_list = []
    for i in nums_str.split(','): #以逗号为分割找出真正的数字元素
        #此时的i是字符
        #不这样写，12，33，45会变成[1,2,3,4,4,5]

        if i.isdigit() == True:
            nums_list.append(int(i))#把int形式的i传进去
            print(nums_list)
        
    nums_list.sort()#确保有序
    target = int(target)
        
    left = 0
    right = len(nums_list)-1
    pos = -1 #pos 始终记录“第一个大于等于 target 的元素下标”（即左边界 first ≥ target）。

     # 二分查找最左边 >= target 的索引
    while left<=right:
        mid = (left+right)//2
        if nums_list[mid]>=target: #说明答案在左边
            pos=mid 
            #pos放if还是else都行，主要是看pos记录什么来决定之后怎么比
            right=mid-1
        elif nums_list[mid]<target:#说明答案在右边
            left=mid+1
    
    if pos == -1:#target比所有数字大
        return nums_list[-1]
    elif pos == 0:#target比所有数字小
        return nums_list[0]
    else:#比较pos和pos-1哪个更近
        if abs(nums_list[pos]-target)<=abs(nums_list[pos-1]-target):
            return nums_list[pos]
        else:
            return nums_list[pos-1]
         

if __name__=='__main__':
    nums_str = input("请输入一组数字，用逗号分隔：")#1,2,3
    target = input("give me a target")
    pos = findclosernumber(nums_str,target)
    print(pos)

