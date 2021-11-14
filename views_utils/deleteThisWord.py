from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def deleteThisWord(word_id):
    print('starting function deleteToken()')

    with driver.session() as session:
        results = session.run(
            '''MATCH (w:Word)
            WHERE id(w) = {word_id}
            DETACH DELETE w
            RETURN w'''.format(word_id=word_id)
        )
        return results