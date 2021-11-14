from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def checkUserNeo(client_id):

    print('starting function checkUserNeo')

    with driver.session() as session:
        results = session.run(
            '''MATCH(person: Person {{id: {client_id} }})
            RETURN person
            '''.format(client_id=client_id)
        )

        nodes = []
        for record in results:
            nodes.append({
                "id": record["person"]["id"],
            })
        if len(nodes) < 1:
            nodes.append({"id":"None"})
            return nodes

        else:
            import json
            personArray = json.dumps(nodes)
            return personArray


# checkedUser = checkUserNeo(client_id=1)
