from py2neo import Graph, Node, Relationship

if __name__ == '__main__':
    graph = Graph("http://localhost:7474", username="neo4j", password='root')   # 输入自己设置的账号密码
    graph.delete_all()  # 清除neo4j中原有的结点等所有信息

    # 创建结点
    node1 = Node('person', name='刘继忠')  # 该结点语义类型是person  结点名字是刘继忠  也是它的属性
    node2 = Node('person', name='李晶')
    node3 = Node('person', name='郭立新')
    node4 = Node('person', name='黄涛')

    node5 = Node('award', name='全国五一劳动奖章')  # 该结点语义类型是award  结点名字是全国五一劳动奖章   也是它的属性
    node6 = Node('award', name='全国五一劳动奖章')

    node7 = Node('person', name='吉林省公安厅交通警察总队高速公路支队')
    node8 = Node('person', name='吉林省长春市公安局交通警察支队')
    node9 = Node('person', name='长春市公路客运总站')
    node10 = Node('person', name='延边东北亚客运集团有限公司')


    node11 = Node('modelWorker', name='劳模')     # 该结点语义类型是modelWorker  结点名字是劳模   也是它的属性


    node1['职称'] = '国家国防科技工业局探月与航天工程中心探月工程副总指挥'  # 为node1添加新的属性
    node2['职称'] = '交通运输部中国交通通信信息中心交通运输导航产业化中心副主任'
    node3['职称'] = '北京医院内分泌科主任'
    node4['职称'] = '国家广播电视总局北京地球站党委书记、站长'
    node5['year'] = 2018
    node6['year'] = 2014

    # 把结点实例化 在Neo4j中显示出来
    graph.create(node1)
    graph.create(node2)
    graph.create(node3)
    graph.create(node4)
    graph.create(node5)
    graph.create(node6)
    graph.create(node7)
    graph.create(node8)
    graph.create(node9)
    graph.create(node10)

    # 创建关系
    awardee1 = Relationship(node5, '获奖人/单位', node1)
    awardee2 = Relationship(node5, '获奖人/单位', node2)
    awardee3 = Relationship(node5, '获奖人/单位', node3)
    awardee4 = Relationship(node5, '获奖人/单位', node4)
    awardee5 = Relationship(node6, '获奖人/单位', node7)
    awardee6 = Relationship(node6, '获奖人/单位', node8)
    awardee7 = Relationship(node6, '获奖人/单位', node9)
    awardee8 = Relationship(node6, '获奖人/单位', node10)
    awardee9 = Relationship(node11, '奖项', node5)
    awardee10 = Relationship(node11, '奖项', node6)
    awardee11 = Relationship(node6, '获奖人/单位', node1)
    # 把关系实例化 在Neo4j中显示出来
    graph.create(awardee1)
    graph.create(awardee2)
    graph.create(awardee3)
    graph.create(awardee4)
    graph.create(awardee5)
    graph.create(awardee6)
    graph.create(awardee7)
    graph.create(awardee8)
    graph.create(awardee9)
    graph.create(awardee10)
    graph.create(awardee11)
