import pymysql

db = pymysql.connect("localhost", "root", "root", "test")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

sql = "SELECT * FROM user_tab"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)

    for row in results:
        sid = row[0]
        gender = row[1]
        class_id=row[2]
        sname=row[3]
        addrs = row[4]
        # 打印结果
        print("职业是:%s,帐号是:%s,年龄是:%s,电话是:%s,地址是:%s" %(sid, gender,class_id,sname,addrs ))
except:
    print("Error: unable to fetch data")


# data = cursor.fetchone()
# print("Database version : %s " % data)

# 关闭数据库连接
# db.close()