
from py2neo import Graph,Node,Relationship

from connect_graph import graph


# 以下代码为官方指定方式:
# https://py2neo.org/v4/database.html#py2neo.database.Transaction.create
# graph = Graph()
# transaction = g.begin()

# a = Node("Person", name="Alice")
# transaction.create(a)

# b = Node("Person", name="Bob")
# transaction.create(b)

# ab = Relationship(a, "KNOWS", b) # 中间的Knows代表a和b之间的关系
# transaction.create(ab)

# graph.commit(transaction)

# 插入成功后可以去neo4j数据里执行 match(n) return n;


def createRelationGraph(parent_name:str, child_name:str, rel:str):
    transaction = graph.begin()
    rootLabel = "Person"
    node_0 = Node(rootLabel, label=rootLabel, name=parent_name)
    transaction.create(node_0)
    node_1 = Node(rootLabel, label=rootLabel, name=child_name)
    transaction.create(node_1)
    relation_node0 = Relationship(node_0, rel, node_1)
    transaction.create(relation_node0)
    graph.commit(transaction)


































