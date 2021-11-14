from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def createNode(node_name, node_key, node_value):
    with driver.session() as session:

        # CREATE(a:Article {article: "AN" })
        results = session.run("""
        CREATE(a:{node_name} {{ {node_key}: "{node_value}" }})
        return a""".format(node_name=node_name, node_key=node_key, node_value=node_value))

        print("Created a new node")


# def createChildNode(parent_node_name, parent_node_key, parent_node_value):
#     with driver.session() as session:
#
#         # MATCH(a:Article {article: "A"})
# # CREATE(b:Sentence {text: "Могу я принести вам ______ чашку чая, пока вы ждете? " })
# # CREATE(b)-[c:HAS_RIGHT_ANSWER_OF]->(a)
# # return c
#
#         results = session.run("""
#         CREATE(a:{parent_node_name} {{ {parent_node_key}: "{parent_node_value}" }})
#         CREATE(b:Sentence {{text: "{}" }})
#         return a""".format(parent_node_name=parent_node_name, parent_node_key=parent_node_key, parent_node_value=parent_node_value))
#
#         print("Created a new node")

# (a:Article {article: "A"})
createNode(node_name='Preposition', node_key='preposition', node_value='ON')




