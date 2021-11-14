from neo4j import GraphDatabase, basic_auth

# chosenLang = RU or EN
def fetchUserLearningPoints(user_id):

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:
        results = session.run(
            """MATCH (node:Person)
            WHERE node.id = {user_id}
            RETURN node""".format(user_id=user_id))

        nodes = []
        for record in results:
            nodes.append(
                {"surname": record['node']['surname'],
                 "name": record['node']['name'],
                 "learningPointA": record['node']['learningPointA'],
                 "learningPointB": record['node']['learningPointB'],
                 })

    import json
    jsonArray = json.dumps(nodes)
    # print(jsonArray)

    return jsonArray

print(fetchUserLearningPoints(2010))