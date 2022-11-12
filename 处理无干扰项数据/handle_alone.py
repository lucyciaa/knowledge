# 处理无干扰项数据

import pymysql

if __name__ == '__main__':
    con = pymysql.connect(host='localhost', password='root', port=3306, user='root', charset='utf8',
                          database='knowledge')  # 链接数据库
    cur = con.cursor()
    query = "INSERT INTO entity(name,性别,民族,职位,flag,奖项,奖项年份) VALUES(%s,%s,%s,%s,%s,%s,%s)"  # 插入语句

    f = open("无干扰项数据.txt", "r", encoding='utf-8')
    lines = f.readlines()  # 读取全部内容

    # 需要更改
    prize = '全国就业与社会保障先进民营企业和全国关爱员工实现双赢先进集体与个人'
    # 需要更改
    prize_year = '2018年'

    for line in lines:
        if(len(line.split(' ')) == 2):
            try:
                # 单独的单位，没有性别民族，职位
                cur.execute(query, (line.split(' ')[0], None, None, line.split(' ')[1], '1', prize, prize_year))
                # 提交到数据库执行
                con.commit()
            except:
                # 如果发生错误则回滚
                print(line, '发生错误')
                con.rollback()
        elif(len(line.split(' ')) == 1):
            try:
                # 单独的单位，没有性别民族，职位
                cur.execute(query, (line.split(' ')[0], None, None, None, '0', prize, prize_year))
                # 提交到数据库执行
                con.commit()
            except:
                # 如果发生错误则回滚
                print(line, '发生错误')
                con.rollback()