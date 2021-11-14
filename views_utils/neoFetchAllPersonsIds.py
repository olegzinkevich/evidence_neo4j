from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def neoFetchAllPersonsIds():

    print('starting function neoFetchAllUsers')

    with driver.session() as session:
        results = session.run(
            '''MATCH(person: Person )
            RETURN person
            ''')

        nodes = []
        for record in results:
            nodes.append({
                "id": record["person"]["id"],
            })

        import json
        usersArray = json.dumps(nodes)

        return usersArray

