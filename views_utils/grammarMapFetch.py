from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def grammarMapFetch(user_id, axisName):

    #  getting UTC timestamp
    from time import gmtime, strftime
    timestamp = strftime("%Y-%m-%d", gmtime())

    with driver.session() as session:
        results = session.run(
            '''MATCH(person: Person {{id: {user_id} }})-[relashionship]->(token)-[BELONGS_TO_AXIS]->(axis: {axisName})
        RETURN person, relashionship, token, axis
        ORDER BY relashionship.timestamp DESC
        '''.format(user_id=user_id, axisName=axisName)
        )

        personArray = []
        nodes = []
        tokensWithoutDuplicates = set()
        # finalArray = [ {person: {id:100, name: Alex}}, {token: {token:Passive}}  ]

        for count, record in enumerate(results):
            # personArray.append({
            #     "id": record["person"]["id"],
            #     "name": record["person"]["name"],
            #     "comment": record["person"]["comment"],
            #     "surname": record["person"]["surname"],
            #     "registered": record["person"]["registered"],
            # })
            # print(record)

            if record["token"]["token"] not in tokensWithoutDuplicates:
                nodes.append({
                    "id": record["person"]["id"],
                    "name": record["person"]["name"],
                    "middlename": record["person"]["middlename"],
                    "comment": record["person"]["comment"],
                    "surname": record["person"]["surname"],
                    "email":record["person"]["email"],
                    "phone":record["person"]["phone"],
                    "birthday":record["person"]["birthday"],
                    "registered": record["person"]["registered"],
                    "axis": record["axis"]["axis"],
                    "axis_rus": record["axis"]["axis_rus"],
                    "token": record["token"]["token"],
                    "token_id": record["token"]["id"],
                    "token_rus": record["token"]["token_rus"],
                    "relashionship": record["relashionship"].type,
                    "relashionship_timestamp": record["relashionship"]["timestamp"],
                    "relashionship_iteration": record["relashionship"]["iteration"],
                    "current_timestamp": timestamp
                })

            tokensWithoutDuplicates.add(record["token"]["token"])

        # perform sorting by token_id
        sortedNodes = sorted(nodes, key=lambda k: k['token_id'])

        import json
        jsonArray = json.dumps(sortedNodes)
        print(jsonArray)

        return jsonArray


# grammarMapFetch(user_id=1, axisName='SyntaxConstructionAxis')
