
from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7473'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def fetchAllWordsCards():
    """
    morph_type = NOUN, VERB, ADV, ADJ
    """
    with driver.session() as session:

        results = session.run("""
        MATCH (d:Dictionary {node:'Dictionary'})-[partOfSpeech:IS_NOUN|IS_VERB|IS_ADJ|IS_ADV]->(w:Word)
        MATCH (w)-[r2]->(Context)
        RETURN id(w),w,type(partOfSpeech)""")

        nodes = []
        for record in results:
            print(record)
            nodes.append({
                "name": record["w"]["name"],
                "translation": record['w']['translation'],
                "partOfSpeech": record['type(partOfSpeech)'],
                "id": record['id(w)'],
            })


        nodes = list({v['id']:v for v in nodes}.values())
        print(nodes)
        return nodes

# fetchThisWordCard(word_id=972)

# print(fetchAllWordsCards())


