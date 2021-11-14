from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def syntaxMapFetch(user_id, axisName):

    #  getting UTC timestamp
    from time import gmtime, strftime
    timestamp = strftime("%Y-%m-%d", gmtime())

    with driver.session() as session:
        results = session.run(
            '''MATCH(person: Person {{id: {user_id} }})-[relashionship]->(token)
        RETURN person, relashionship, token'''.format(user_id=user_id)
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
                    "axis": record["token"]["axis_name"],
                    "token": record["token"]["token"],
                    "relashionship": record["relashionship"].type,
                    "relashionship_timestamp": record["relashionship"]["timestamp"],
                    "relashionship_iteration": record["relashionship"]["iteration"],
                    "current_timestamp": timestamp
                })

            tokensWithoutDuplicates.add(record["token"]["token"])

        import json
        json_array = json.dumps(nodes)
        print(json_array)

        return json_array


# syntaxMapFetch(user_id=3)