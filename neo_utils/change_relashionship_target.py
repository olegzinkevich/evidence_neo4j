from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def createAxisNode(token, new_target_node):
    '''
    Changes relashionship target of a node
    '''
    with driver.session() as session:

        results = session.run("""
        MATCH (token:{token})-[rel_old:TOKEN_BELONGS_TO_AXIS]->(old_target_node),(new_target_node:{new_target_node})
        CREATE (token)-[rel_new:TOKEN_BELONGS_TO_AXIS]->(new_target_node)
        SET rel_new=rel_old
        DELETE rel_old
        RETURN token, new_target_node
""".format(token=token, new_target_node=new_target_node))

        print("Node relashionship has been changed")


createAxisNode(token='SetPointers', new_target_node='DeterminantsAxis')




