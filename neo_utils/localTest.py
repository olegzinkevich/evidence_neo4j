
from neo4j import GraphDatabase, basic_auth

host = 'bolt://localhost:7687'
# host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def fetchWords(morph_type):
    """
    morph_type = NOUN, VERB, ADV, ADJ
    """
    with driver.session() as session:

        results = session.run("""
        MATCH (d:Dictionary {{node:'Dictionary'}})-[rel:IS_{morph_type}]->(w:Word)
        RETURN d,type(rel),w,id(w)""".format(morph_type=morph_type))

        nodes = []
        for record in results:
            print(record)
            nodes.append({
                "name": record["w"]["name"],
                "translation": record['w']['translation'],
                "plural": record['w']['plural'],
                "type": record['type(rel)'],
                "id": record['id(w)']
            })

        print(nodes)
        return nodes


fetchWords(morph_type='NOUN')




