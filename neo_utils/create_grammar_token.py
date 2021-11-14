from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

axis = 'SyntaxConstructionAxis'
tokensList = [{'token':'Existence', 'token_rus':'Существование'},
              ]

def createToken(axisName):

    # enumerate start with 1
    for count, tkn in enumerate(tokensList, 0):

        token_name = tkn.get('token')
        token_rus = tkn.get('token_rus')

        with driver.session() as session:

            results = session.run(
                """
            MATCH (axis:{axisName})
            CREATE (token: {token} {{ token:'{token}', id:{id}, token_rus:'{token_rus}' }})-[rel:TOKEN_BELONGS_TO_AXIS]->(axis)
                """.format(axisName=axisName, token=token_name, token_rus=token_rus, id=count)
            )

            print("Created a new node")

createToken(axisName=axis)




