from neo4j import GraphDatabase, basic_auth
import json

def fetchUserGrammarCheckboxes(user_id):

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

# MATCH (a:Person {id: 2000})-[r:HAS_PERSONAL_GRAMMAR_MAP]->(b:GrammarCheckboxes)
# return a,r, b

    with driver.session() as session:
        results = session.run(
            """MATCH (node:Person {{id: {user_id} }})-[r:HAS_PERSONAL_GRAMMAR_MAP]->(b:GrammarCheckboxes)
            RETURN r""".format(user_id=user_id))

        nodes = []

        import ast
        for record in results:
         # and convert to dict because we store map/dict/json object in neo4j relashionship parameter
            nodes.append(
                {"checkboxes": ast.literal_eval(record['r']['checkboxes'])})
            # if we create a new user, it doesn't have any checkboxes

    import json
    jsonArray = json.dumps(nodes)
    print(jsonArray)

    return jsonArray

x = fetchUserGrammarCheckboxes(5600)
print(x)
