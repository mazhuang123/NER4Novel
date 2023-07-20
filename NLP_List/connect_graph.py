from py2neo import Graph,Node,Relationship
#上面要导包,需要用pip的方式: pip install py2neo
# 连接服务器
#这里用的是http开头的,所以要在设置里将 server.http.enabled=true 和 server.http.listen_address=:7474 都放开,默认的是bolt
server_url = "http://localhost:7474"
user_name = "neo4j" #默认用户名就是这个
password = "12345678"#密码是创建数据库时设置的,如果没设置,默认就是 neo4j
# 以下两种方法皆可,但要注意最后一定要再拼上 name = "neo4j",否则后续创建graph的时候就会报jsondecodererror的错误
# graph = Graph(server_url,username = user_name,password = password,name = "neo4j")
graph = Graph(server_url,auth= (user_name,password),name="neo4j")