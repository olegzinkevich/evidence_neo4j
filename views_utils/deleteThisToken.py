from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def deleteThisToken(token_id):
    print('starting function deleteToken()')

    with driver.session() as session:
        results = session.run(
            '''MATCH (token:Sentence)
            WHERE id(token) = {token_id}
            DETACH DELETE token
            RETURN token'''.format(token_id=token_id)
        )
        return results