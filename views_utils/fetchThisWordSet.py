
from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7473'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def fetchThisWordSet(wordset_id):

    with driver.session() as session:

        # (?i){name} = lowercase/uppercase pattern for matching name
        results = session.run("""
        MATCH (set:WordSet)<-[r:BELONGS_TO_WORDSET]-(w:Word)-[r2:HAS_CONTEXT_RU]->(c1:Context)
        WHERE id(set) = {wordset_id}
        RETURN set, id(set), id(w), w, c1""".format(wordset_id=wordset_id))

        wordSet = []
        words = []

        for record in results:
            wordSet.append({
                "id": record['id(set)'],
                "wordSetName": record['set']['wordSetName'],
            })
            words.append({
                "wordName": record['w']['name'],
                "wordId": record['id(w)'],
                "imgBase64": record['w']['imgBase64'],
                "contextRu": record['c1']['contextRu'],
            })
        # print(wordSet)
        # print(words)

        # saving only unique values
        wordSet = list({v['id']:v for v in wordSet}.values())

        finalData = [{
            "wordSet": wordSet,
            "words": words,
        }]

        return finalData

print(fetchThisWordSet(wordset_id=1030))







