from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def grammarMapFetchChart(user_id, axisName):

    #  getting UTC timestamp
    from time import gmtime, strftime
    timestamp = strftime("%Y-%m-%d", gmtime())

    from datetime import datetime
    import re

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
                    "comment": record["person"]["comment"],
                    "surname": record["person"]["surname"],
                    "registered": record["person"]["registered"],
                    "axis": record["axis"]["axis"],
                    "token": record["token"]["token"],
                    "token_id": record["token"]["id"],
                    "token_rus": record["token"]["token_rus"],
                    "relashionship":re.findall('\d+', record["relashionship"].type)[0],
                    "relashionship_timestamp": record["relashionship"]["timestamp"],
                    "relashionship_iteration": record["relashionship"]["iteration"],
                    "current_timestamp": timestamp
                })

            tokensWithoutDuplicates.add(record["token"]["token"])

        # tokensWithoutDuplicates = list(tokensWithoutDuplicates)
        # print(tokensWithoutDuplicates)
        # sort in place by timestamp
        # nodes.sort(key=lambda d: d['relashionship_timestamp'])

        # print(nodes)

        # perform sorting by token_id
        sortedNodes = sorted(nodes, key=lambda k: k['token_id'])

        import json
        jsonArray = json.dumps(sortedNodes)

        return jsonArray


# grammarMapFetchChart(user_id=1009, axisName='TensesAxis')

