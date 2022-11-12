from paddlenlp import Taskflow
import pymysql

if __name__ == '__main__':
    schema = ['姓名', '性别', '民族']
    ie = Taskflow('information_extraction', schema=schema)
    con = pymysql.connect(host='localhost', password='root', port=3306, user='root', charset='utf8',database='knowledge')   # 链接数据库
    cur = con.cursor()
    query = "INSERT INTO entity(name,性别,民族,职位,flag,奖项,奖项年份) VALUES(%s,%s,%s,%s,%s,%s,%s)"     # 插入语句

    unmake = open('../处理无干扰项数据/未成功处理数据.txt', 'w', encoding='utf-8')  # 保存未处理数据

    f = open("../奖项/全国工会系统先进集体/2018年/2018年全国工会系统先进集体_out.txt", "r", encoding='utf-8')
    lines = f.readlines()  # 读取全部内容

    # 需要更改
    prize = '全国工会系统先进集体'
    prize_year = '2018年'

    for line in lines:
        # 如果划分之后为独立的个体，那么有两种情况，单位名称，或者是数据处理的不好，没有空格
        if(len(line.split(' ')) == 1):
            if(len(line.split('(女')) == 1):
                try:
                    # 单独的单位，没有性别民族，职位
                    cur.execute(query, (line, None, None, None, '0', prize, prize_year))
                    # 提交到数据库执行
                    con.commit()
                except:
                    # 如果发生错误则回滚
                    print(line,'发生错误')
                    con.rollback()
            #将不符合处理条件的数据放入单独的文件
            else:
                unmake.write(line)
        elif(len(line.split(' ')) == 2):
            list = ie(line.split(' ')[0])
            # 将要插入数据库的数据放到该列表下，最后转成元组
            entityList = []
            if('姓名' in list[0]):
                entityList.append(list[0]['姓名'][0]['text'])
            else:
                # 不能识别姓名的统一放到未成功处理数据
                unmake.write(line)
                continue
            if('性别' in list[0]):
                entityList.append(list[0]['性别'][0]['text'])
            else:
                entityList.append(None)
            if ('民族' in list[0]):
                entityList.append(list[0]['民族'][0]['text'])
            else:
                entityList.append(None)
            # 设置职位
            entityList.append(line.split(' ')[1])
            # 设置flag
            entityList.append('1')
            # 设置奖项和年份
            entityList.append(prize)
            entityList.append(prize_year)
            # 插入数据库
            try:
                # 执行sql语句
                cur.execute(query, tuple(entityList))
                # 提交到数据库执行
                con.commit()
            except:
                # 如果发生错误则回滚
                print(line, '发生错误')
                con.rollback()
        else:
            #其他情况为不能处理的数据，放入单独的文件
            unmake.write(line)
    unmake.close()

