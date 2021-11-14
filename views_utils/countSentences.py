from neo4j import GraphDatabase, basic_auth

def countSentences():

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:
        results = session.run(
            """MATCH (n:Sentence)
            RETURN count(n) as count""")

        nodes = []
        for record in results:
            nodes.append(
                {"count": record["count"],
                 })

    return nodes


# print(countSentences())

