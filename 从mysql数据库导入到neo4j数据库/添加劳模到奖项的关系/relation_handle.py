from py2neo import Graph, Node, Relationship

if __name__ == '__main__':
    graph = Graph("http://localhost:7474", username="neo4j", password='root')  # 输入自己设置的账号密码
    model_node = Node('modelWorker', name='劳模')  # 该结点语义类型是modelWorker  结点名字是劳模   也是它的属性
    nodes = list(graph.nodes.match('award'))
    for node in nodes:
        relation = Relationship(model_node, '奖项', node)
        graph.create(relation)  # 创建关系