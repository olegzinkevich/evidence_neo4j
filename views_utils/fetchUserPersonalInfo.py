from neo4j import GraphDatabase, basic_auth

# chosenLang = RU or EN
def fetchUserPersonalInfo(user_id):

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:
        results = session.run(
            """MATCH (node:Person)
            WHERE node.id = {user_id}
            RETURN node""".format(user_id=user_id))

        nodes = []
        for record in results:
            nodes.append(
                {"phone": record['node']['phone'],
                 "surname": record['node']['surname'],
                 "name": record['node']['name'],
                 "middlename": record['node']['middlename'],
                 "comment": record['node']['comment'],
                 "email": record['node']['email'],
                 "birthday": record['node']['birthday'],
                 })

    import json
    jsonArray = json.dumps(nodes)
    # print(jsonArray)

    return jsonArray

# print(fetchUserPersonalInfo(1))