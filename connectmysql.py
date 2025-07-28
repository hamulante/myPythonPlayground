# pip install pymysql done

import pymysql
import time

host = "mysql-flexible-server-test1.mysql.database.azure.com"
user = "beibeihu"
password = 'Ms199642-'
ca_path = r'C:\Users\beibeihu\Documents\PythonPlayground\DigiCertGlobalRootCA.crt.pem'

def connectmysql():
    print("connecting")
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            ssl={'ca':ca_path}
        )
        print("connected")
        conn.close()
    except pymysql.MySQLError as e:
        print(e)
    return

if __name__=="__main__":
    start_time = time.time()#设定开始时间，打算让脚本跑10分钟就停
    while True: #不写这个while直接判断时间的话，根本不会开始
        if time.time()-start_time>600: #600s
            break
        connectmysql()
        time.sleep(10)#check every 10s
    






