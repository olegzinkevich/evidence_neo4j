from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
# host = 'bolt://semantiqa.com:7687'
# db_name = 'neo4j'
# password = 'cazzhack'

driver = GraphDatabase.driver("bolt+s://8ff3f68cd5db0d870d7990fbaab10461.neo4jsandbox.com:7687", auth)

def createSimpleNode(node_name):

    with driver.session() as session:

        results = session.run("""
        CREATE (GrammarCheckboxes:{node_name})""".format(node_name=node_name))

        print("Created a new Node")


createSimpleNode(node_name='GrammarCheckboxes')




