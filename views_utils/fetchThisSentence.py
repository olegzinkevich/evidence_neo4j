from neo4j import GraphDatabase, basic_auth

# chosenLang = RU or EN
def fetchThisSentence(text_id):

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:
        results = session.run(
            """MATCH (token:Sentence)
            WHERE id(token) = {id}
            RETURN token, id(token)""".format(id=text_id))

        nodes = []
        for record in results:
            nodes.append(
                {"sentence": record['token']['text'],
                 "id": record['id(token)']})

    import json
    jsonArray = json.dumps(nodes)
    # print(jsonArray)

    return jsonArray

# print(fetchThisSentence(0))