from py2neo import Graph, Node, Relationship
import pymysql

if __name__ == '__main__':
    graph = Graph("http://localhost:7474", username="neo4j", password='root')  # 输入自己设置的账号密码
    graph.delete_all()  # 清除neo4j中原有的结点等所有信息

    con = pymysql.connect(host='localhost', password='root', port=3306, user='root', charset='utf8',
                          database='knowledge')  # 链接mysql数据库
    cur = con.cursor()
    query = "SELECT * FROM entity"  # 查询语句
    cur.execute(query)
    rows = cur.fetchall()

    # 依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示

    for row in rows:
        row = list(row)
        prize_name = row[5]
        prize_year = row[6]
        nodes = list(graph.nodes.match('award', name=prize_name, 年份=prize_year))
        if (len(nodes) == 0):  # 判断数据库中是否已经该奖项，如果不存在就创建该节点
            awardNode = Node('award', name=prize_name, 年份=prize_year)
            graph.create(awardNode)
        else:  # 如果存在该奖项赋值给awardNode
            awardNode = graph.nodes.match('award').where(name=prize_name, 年份=prize_year).first()
        if(row[4] == '1'):
            entity_name = row[0]
            entity_sex = row[1]
            entity_nation = row[2]
            entity_job = row[3]
            node = Node('person', name = entity_name, 性别 = entity_sex, 民族 = entity_nation, 职业 = entity_job)
            relation = Relationship(awardNode, '获奖人', node)
            graph.create(node)  # 创建节点
            graph.create(relation)  # 创建关系
        elif(row[4] == '0'):
            entity_name = row[0]
            node = Node('community', name=entity_name)
            relation = Relationship(awardNode, '获奖单位', node)
            graph.create(node)  # 创建节点
            graph.create(relation)  # 创建关系