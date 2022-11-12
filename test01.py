

from py2neo import Graph, Node, Relationship
import pymysql

if __name__ == '__main__':
    con = pymysql.connect(host='localhost', password='root', port=3306, user='root', charset='utf8',
                          database='knowledge')  # 链接mysql数据库
    cur = con.cursor()
    query = "SELECT * FROM entity"  # 查询语句
    cur.execute(query)
    rows = cur.fetchall()

    # 依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示

    for row in rows:
        print(row)
