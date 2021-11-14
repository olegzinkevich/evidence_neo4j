from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def createAxisNode(axis_name, axis_rus):

    with driver.session() as session:

        results = session.run("""
        CREATE (axis:{axis_name} {{ axis: '{axis_name}', axis_rus: '{axis_rus}' }})""".format(axis_name=axis_name, axis_rus=axis_rus))

        print("Created a new axis")


createAxisNode(axis_name='AdverbsAxis', axis_rus='Наречия')




