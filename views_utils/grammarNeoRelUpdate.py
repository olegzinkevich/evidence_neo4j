from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def grammarNeoRelUpdate(client_id, token, level, iteration, timestamp):

    print('starting function grammarNeoRelUpdate')

    with driver.session() as session:
        results = session.run(
            '''MATCH (person:Person {{ id: {client_id} }}), (token:{token})
            MERGE (person)-[rel:KNOWS_AT_LEVEL_{lvl}]->(token)
            ON CREATE SET rel.iteration = {iteration}
            ON MATCH SET rel.iteration = {iteration}
            ON CREATE SET rel.timestamp = '{timestamp}'
            ON MATCH SET rel.timestamp = '{timestamp}'
            RETURN rel'''.format(client_id=client_id, token=token, lvl=level, iteration=iteration, timestamp=timestamp)
        )
        return results

#
# grammarNeoRelUpdate(client_id=1, token='Passive', level=3, iteration=3, timestamp='2020-02-24')