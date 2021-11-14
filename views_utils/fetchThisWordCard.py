
from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7473'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def fetchThisWordCard(word_id):
    """
    morph_type = NOUN, VERB, ADV, ADJ
    """
    with driver.session() as session:

        results = session.run("""
        MATCH (d:Dictionary {{node:'Dictionary'}})
        MATCH (d)-[partOfSpeech]->(w:Word)
        MATCH (w)-[r2:HAS_CONTEXT_RU]->(cntxtRu:Context)
        MATCH (w)-[r3:HAS_CONTEXT_EN]->(cntxtEn:Context)
        WHERE id(w) = {word_id}
        RETURN d,type(partOfSpeech),cntxtRu,cntxtEn,id(w),w""".format(word_id=word_id))

        node = []
        contextsRu = []
        contextsEn = []
        for record in results:
            print(record)
            node.append({
                "name": record["w"]["name"],
                "translation": record['w']['translation'],
                "transcription": record['w']['transcription'],
                "origin": record['w']['origin'],
                "antonyms": record['w']['antonyms'],
                "synonyms": record['w']['synonyms'],
                "collocations": record['w']['collocations'],
                "grammForms": record['w']['grammForms'],
                "imgBase64": record['w']['imgBase64'],
                "partOfSpeech": record['type(partOfSpeech)'],
                "id": record['id(w)'],
            })
            contextsRu.append({
                "contextRu": record['cntxtRu']['contextRu'],
            })
            contextsEn.append({
                "contextEn": record['cntxtEn']['contextEn']
            })

        print(node[0])
        print()

        # saving only unique values from dictionaries. Because it duplicated values for all fetched nodes
        contextsRu = list({v['contextRu']:v for v in contextsRu}.values())
        contextsEn = list({v['contextEn']:v for v in contextsEn}.values())
        node = list({v['id']:v for v in node}.values())
        print(contextsRu)
        print(contextsEn)
        print(node)

        finalData = [{
            "contextsRu": contextsRu,
            "contextsEn": contextsEn,
            "node": node
        }]
        print(finalData)

        return finalData

# fetchThisWordCard(word_id=972)




