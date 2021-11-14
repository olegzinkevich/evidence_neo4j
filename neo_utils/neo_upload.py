from neo4j import GraphDatabase, basic_auth


# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def uploadArticleSentences(article, text, language):
    with driver.session() as session:

        results = session.run("""
        MATCH(a:Article {{article: "{0}" }})
        CREATE(b:Sentence {{text: "{1}" }})
        CREATE(b)-[c:HAS_LANGUAGE_{2}]->(a)
        CREATE(b)-[d:HAS_RIGHT_ANSWER_OF]->(a)
        return c,d""".format(article, text, language))

        nodes = []
        for count, record in enumerate(results):
            nodes.append({"record": record["c"]["relashionship"], "record": record['d']['relashionship'], "id": count})

        print(nodes)
        print('Inserted sentences:', len(nodes))
        return nodes

def uploadArticleSentencesPreTest(article, text, language):
    with driver.session() as session:

        results = session.run("""
        MATCH(a:Article {{article: "{0}" }})
        CREATE(b:Sentence {{text: "{1}", preliminary_test: "yes" }})
        CREATE(b)-[c:HAS_LANGUAGE_{2}]->(a)
        CREATE(b)-[d:HAS_RIGHT_ANSWER_OF]->(a)
        return c,d""".format(article, text, language))

        nodes = []
        for count, record in enumerate(results):
            nodes.append({"record": record["c"]["relashionship"], "record": record['d']['relashionship'], "id": count})

        print(nodes)
        print('Inserted sentences:', len(nodes))
        return nodes


def uploadPrepositionSentences(preposition, text, language, preposition_type):
    with driver.session() as session:

        results = session.run("""
        MATCH(a:Preposition {{preposition: "{0}" }})
        CREATE(b:Sentence {{text: "{1}" }})
        CREATE(b)-[c:HAS_LANGUAGE_{2}]->(a)
        CREATE(b)-[d:HAS_RIGHT_ANSWER_OF]->(a)
        CREATE(b)-[e:HAS_TYPE_{3}]->(a)
        return c,d,e""".format(preposition, text, language, preposition_type))
        print('Inserted sentences')

texts = ["I do not drink ____ black coffee. I prefer cappuccino.",
"____ sea water does not freeze at  0ºC.",
"He is already ____ bed. He is sleeping.",
"I have been afraid to take ____ exams all my life.",
"___ Lake Baikal is in danger.",
"I want to go to ____ France.",
"They left the room with ____ dignity."]

#########################################################
##### Upload article sentences
#########################################################

# article = 'AN'
# chosenLang = 'RU'
#
# for x in texts:
#     uploadArticleSentences(article=article, text=x, language=chosenLang)

#########################################################
##### Upload article sentences for Preliminary Test
#########################################################

article = '(A)'
chosenLang = 'EN'

for x in texts:
    uploadArticleSentencesPreTest(article=article, text=x, language=chosenLang)

#########################################################
##### Upload preposition sentences
#########################################################

# preposition = 'IN'
# chosenLang = 'EN'
# preposition_type = 'OF_TIME'
#
# for x in texts:
#     uploadPrepositionSentences(preposition=preposition, text=x, language=chosenLang, preposition_type=preposition_type)




