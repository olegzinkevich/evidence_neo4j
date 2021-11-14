from neo4j import GraphDatabase, basic_auth

def prepositionsSentencesFetchByType(preposition, grammarType, language):
    """ grammarType = 'OF_TIME', 'OF_PLACE',
        chosenLang = 'RU', 'EN' """

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:

        results = session.run(
            """MATCH (a:Preposition {{preposition: "{0}" }})
            MATCH(a)<-[b:HAS_LANGUAGE_{1}]-(s:Sentence)
            MATCH(a)<-[c:HAS_TYPE_{2}]-(s:Sentence) 
            MATCH(a)<-[d:HAS_RIGHT_ANSWER_OF]-(s)
            RETURN a,s, id(s)""".format(
                preposition, language, grammarType))

        nodes = []
        for count, record in enumerate(results):

            nodes.append(
                {"answer": record["a"]["preposition"],
                 "sentence": record['s']['text'],
                 "id": record['id(s)']})

        return nodes

# print(prepositionsSentencesFetchByType(preposition="ON", grammarType="OF_TIME", language="EN"))