from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def deleteThisWordSet(wordset_id):
    print('starting function deleteWordSet()')

    with driver.session() as session:
        results = session.run(
            '''MATCH (set:WordSet)
            WHERE id(set) = {wordset_id}
            DETACH DELETE set
            RETURN set'''.format(wordset_id=wordset_id)
        )
        return results

