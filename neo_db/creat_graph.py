from py2neo import Graph, Node, Relationship
from config import graph

with open("D:/A_Keyan/GitHub/KGQA_HLM-master/raw_data/relation.txt", encoding="utf-8") as f:
    for line in f.readlines():
        rela_array = line.strip("\n").split(",")
        print(rela_array)

        # 创建或合并节点
        graph.run("MERGE (p:Person {cate: $cate1, Name: $name1})", cate1=rela_array[3], name1=rela_array[0])
        graph.run("MERGE (p:Person {cate: $cate2, Name: $name2})", cate2=rela_array[4], name2=rela_array[1])

        # 创建关系
        graph.run(
            """
            MATCH (e:Person), (cc:Person)
            WHERE e.Name = $name1 AND cc.Name = $name2
            CREATE (e)-[r:%s {relation: $relation}]->(cc)
            RETURN r
            """ % rela_array[2],
            name1=rela_array[0], name2=rela_array[1], relation=rela_array[2]
        )
