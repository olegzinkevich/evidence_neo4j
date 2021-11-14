from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def neoDeleteUser(user_id):
    print('starting function neoDeleteUser()')

    with driver.session() as session:
        results = session.run(
            '''MATCH (person {{ id: {client_id} }}) 
            DETACH DELETE person'''.format(client_id=user_id)
        )
        return results