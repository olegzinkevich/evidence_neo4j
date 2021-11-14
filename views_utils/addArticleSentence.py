from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))


def addArticleSentence(article, text, language):
    """
    article = AN, A, THE, (A)
    language = RU / EN
    """
    with driver.session() as session:

        results = session.run("""
        MATCH(a:Article {{article: "{article}" }})
        CREATE(b:Sentence {{text: "{text}" }})
        CREATE(b)-[c:HAS_LANGUAGE_{language}]->(a)
        CREATE(b)-[d:HAS_RIGHT_ANSWER_OF]->(a)
        return c,d""".format(article=article, text=text, language=language))

        nodes = []
        for record in results:
            nodes.append({"record": record["c"]["relashionship"], "record": record['d']['relashionship']})

        print(nodes)
        print('Inserted sentence')
        return nodes


# addArticleSentence(article='THE', text='I have decided to repair ____ Macbook Pro Notebook', language='EN')


