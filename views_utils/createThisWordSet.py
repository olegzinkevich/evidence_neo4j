from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7473'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

wordsIds = [982,983]

def createThisWordSet(wordset_name, word_id):

    with driver.session() as session:

        # (?i){name} = lowercase/uppercase pattern for matching name
        results = session.run("""
        MATCH (w:Word)
        WHERE id(w) = {word_id}
        MERGE (set:WordSet {{wordSetName: "{wordset_name}"}})
        MERGE (w)-[r:BELONGS_TO_WORDSET]->(set)
        RETURN w, set, id(set)""".format(word_id=word_id, wordset_name=wordset_name))

        node = []

        for record in results:
            node.append({
                "id": record['id(set)'],
                "name": record['set']['wordSetName'],
            })
        # print(node)

        if len(node) > 0:
            return node
        else:
            return None

# x = createWordSet(wordset_name='X', word_id='982')
# print(x)
# print(x)
# if x is None:
#     print('yes none')


