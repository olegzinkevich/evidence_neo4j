
from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7473'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def fetchWordByName(name):

    with driver.session() as session:

        # (?i){name} = lowercase/uppercase pattern for matching name
        results = session.run("""
        MATCH (w:Word)
        WHERE w.name =~ "(?i){name}"
        RETURN w, id(w)""".format(name=name))

        node = []

        for record in results:
            node.append({
                "id": record['id(w)'],
                "name": record['w']['name'],
            })
        print(node)

        if len(node) > 0:
            return node
        else:
            return None

# x = fetchWordByName(name='smth snew')
# print(x)
# if x is None:
#     print('yes none')




