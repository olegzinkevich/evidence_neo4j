from neo4j import GraphDatabase, basic_auth

def grammarMapSetRel(level, token):

    host = 'bolt://localhost:7687'
    # host = 'bolt://semantiqa.com:7687'
    db_name = 'neo4j'
    password = 'cazzhack'

    driver = GraphDatabase.driver(host, auth=("neo4j", password))

    #  getting UTC timestamp
    from time import gmtime, strftime
    timestamp = strftime("%Y-%m-%d", gmtime())

    with driver.session() as session:
        results = session.run(
            """MATCH (n:Person)-[rel:KNOWS_AT_LEVEL_{level} {{timestamp: '17.02.2020', iteration: 0}}]->(m:{token})
MERGE (n)-[:KNOWS_AT_LEVEL_3 {timestamp: '17.02.2020', iteration: 0}]->(m) DELETE rel""".format(level=level, token=token))

        return results