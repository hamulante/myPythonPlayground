#all files in C:\Users\beibeihu\Documents\PythonPlayground\playground
#先不递归，不考虑子文件夹的情况

import os
import re
from datetime import datetime

def finderrorsinlogs(path):
    n_file=0
    n_error=0
    error_result=[]#用来存放找到的error记录，不然在for循环内的变量外面读不到

    for file in os.listdir(path):
        n_file=n_file+1#扫描的文件数量+1

        full_path = os.path.join(path,file)#接下来找文件都得用完整路径

        with open(full_path,'r',encoding='utf-8') as opened_file:#read only
            for line_number,line in enumerate(opened_file,start=1):
                if "error" in line.lower():#防止文本里error是大写
                    n_error=n_error+1 #找到的error数量+1
                    error_result.append((file,line_number,line))#3个元素存成一个大元素
    
    print("本次扫描了",n_file,"个文件")
    print("共发现了",n_error,"个关键字")
    for result in error_result:#每一个大元素中的小元素
        print("在文件",result[0],"中第",result[1],"行发现",result[2])
    
    return

if __name__=='__main__':
    path = input("please give a folder path")
    finderrorsinlogs(path)