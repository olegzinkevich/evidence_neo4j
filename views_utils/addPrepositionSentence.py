from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def addPrepositionSentence(preposition, type, language, text):
    """
    article = AN, A, THE, (A)
    language = RU / EN
    """
    print('Start addPrepositionSentence()')

    with driver.session() as session:

        results = session.run("""
        MATCH(a:Preposition {{preposition: "{preposition}" }})
        CREATE(b:Sentence {{text: "{text}" }})
        CREATE(b)-[c:HAS_LANGUAGE_{language}]->(a)
        CREATE(b)-[d:HAS_RIGHT_ANSWER_OF]->(a)
        CREATE(b)-[e:HAS_TYPE_{type}]->(a)
        return id(b),c,d""".format(preposition=preposition, type=type, language=language, text=text))

        nodes = []
        for record in results:
            nodes.append({"record": record["c"]["relashionship"],
                          "id": record['id(b)']
                          })

        print(nodes)
        print('Inserted sentence')
        return nodes


# addPrepositionSentence(preposition='ON', type='OF_TIME', language='EN', text='test5', )


