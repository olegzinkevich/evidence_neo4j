
from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7473'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def fetchAllWordSets():

    with driver.session() as session:

        # (?i){name} = lowercase/uppercase pattern for matching name
        results = session.run("""
        MATCH (set:WordSet)
        RETURN set, id(set)""")

        node = []

        for record in results:
            node.append({
                "id": record['id(set)'],
                "name": record['set']['wordSetName'],
            })
        print(node)

        return node

# x = fetchAllWordSets()






