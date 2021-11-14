from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def grammarNeoCommentUpdate(client_id, comment):

    print('starting function grammarNeoCommentUpdate')

    with driver.session() as session:
        results = session.run(
            '''MATCH (person:Person {{ id: {client_id} }}), 
            SET person.comment = '{comment}'
            RETURN person'''.format(client_id=client_id, comment=comment)
        )
        return results


# grammarNeoCommentUpdate(client_id=1, comment='Smth new 7')