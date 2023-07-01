import pymysql

# 打开数据库连接，参数1：主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名
db = pymysql.connect(host='localhost', user='root', password='Tianxin_2015', database='usr_contact_info')

# 使用cursor()创建一个cursor对象
cursor = db.cursor()
# 创建数据库和数据表
cursor.execute("drop table if exists usr_contact_info")
sql = """create table usr_contact_info (
         `序号`  INT UNSIGNED AUTO_INCREMENT,
         `姓名`  CHAR(10),
         `联系方式` CHAR(11),  
         `住址` CHAR(30),
         `接待人` CHAR(10),
         PRIMARY KEY ( `序号` ) )"""
cursor.execute(sql)

# 外部导入的数据
data_test = [
            ['张三','15023481157','成都市武侯区蜀都大道富贵花园小区2栋1单元','王凯'],
            ['李四','15420135526','成都市武侯区蜀都大道富贵花园小区12栋2单元','王凯'],
            ['王五','18654265531','成都市武侯区蜀都大道富贵花园小区9栋1单元','王凯'],
            ['赵六','19454265623','成都市武侯区蜀都大道富贵花园小区8栋1单元','王凯']
        ]
cursor.executemany("insert into usr_contact_info(姓名,联系方式,住址,接待人) values (%s,%s,%s,%s)", data_test)
db.commit()

# 使用execute()方法执行SQL查询
rs = cursor.execute("select * from usr_contact_info;")
print(rs)
# 查询第一条数据
rs_data_one = cursor.fetchone()
print(rs_data_one)
# 查询所有数据
rs_data_all = cursor.fetchall()
print(rs_data_all)

# 关闭数据库
db.close()
