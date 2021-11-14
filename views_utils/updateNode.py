from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def setNode(token, id, rus_trans):

    with driver.session() as session:

        results = session.run("""
        MATCH (tkn:{token})
        SET tkn.id = {id}, tkn.token_rus = '{rus_trans}'
        RETURN tkn
        """.format(token=token, id=id, rus_trans=rus_trans))


        print("Node updated")


# setNode(token='NotTill', id=6, rus_trans='Not till')




