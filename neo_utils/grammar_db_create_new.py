from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def createNode(name, id, surname):
    with driver.session() as session:

        results = session.run("""
        CREATE ({name}:Person {{name: '{name}', surname: '{surname}', id: {id} }})
        CREATE (SyntaxConstructionAxis:SyntaxConstructionAxis {axis: 'SyntaxConstructionAxis'})""".format(name=name, surname=surname, id=id))

        print("Created a new node")


createNode(name='Preposition', surname='preposition', id='ON')




