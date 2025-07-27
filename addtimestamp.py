#all files in C:\Users\beibeihu\Documents\PythonPlayground\playground
#先不递归，不考虑子文件夹的情况

import os
import re
from datetime import datetime

def addtimestamp(path):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S') # 20250722_154301
    #str(datetime.now())是2025-07-22 15:43:01.5584，有冒号，windows不接受

    existing_timestamp = re.compile(r'^\d{8}_\d{6}_')  # 匹配开头的时间戳格式

    for file in os.listdir(path):
        print(file)

        #现在的名字，可能带着时间戳
        old_path = os.path.join(path,file)
        print(old_path)
        
        #一律先去掉事件戳
        file = existing_timestamp.sub('', file) 
        print(file)
        new_path = os.path.join(path,timestamp+'_'+file)
        print(new_path)

        os.rename(old_path,new_path) #os.renamey必须用完整路径
    return

if __name__=='__main__':
    path = input("please give a folder path")
    addtimestamp(path)