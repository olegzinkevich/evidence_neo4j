from neo4j import GraphDatabase

class HelloWorldExample(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]


from neo4j import GraphDatabase, basic_auth

# driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "cazzhack"))

#
# def add_friend(tx, name, friend_name):
#     tx.run("MERGE (a:Person {name: $name}) "
#            "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
#            name=name, friend_name=friend_name)
#
# def print_friends(tx, name):
#     for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
#                          "RETURN friend.name ORDER BY friend.name", name=name):
#         print(record["friend.name"])
#
# with driver.session() as session:
#     session.write_transaction(add_friend, "Arthur", "Guinevere")
#     session.write_transaction(add_friend, "Arthur", "Lancelot")
#     session.write_transaction(add_friend, "Arthur", "Merlin")
#     session.read_transaction(print_friends, "Arthur")
#
# driver.close()

driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

print(driver)
# importing data

sentence_obj = {
    "sentence_id": 1,
    "text": "Он работает врачом",
    "answer": "A",
}

# with driver.session() as session:
#     session.run('''
#         WITH {sentence} as sentence
#         CREATE (t:Sentence {sentence_id: sentence.sentence_id})
#         SET t.text = sentence.text,
#             t.answer = sentence.answer
#
#     ''', parameters={'sentence': sentence_obj}).consume()

# with driver.session() as session:
#     session.run('''
#         MATCH (n1)-[r]->(n2) RETURN n1 LIMIT 25
#
#     ''', parameters={'sentence': sentence_obj}).consume()

# def print_sentences_of(tx):
#     records_list = []
#     for record in tx.run("MATCH (n1)-[r]->(n2) "
#                          "RETURN n1"):
#         print(record)
#         print(type(record))
#         records_list.append(record)
#         for x in record:
#             x.get('properties', default=None)
#             print(x[0])
#
#     return records_list
#
# with driver.session() as session:
#     records_list = session.read_transaction(print_sentences_of)
#
# "MATCH (a:Article)-[:HAS_A_RIGHT_ANSWER_OF]->(s:Sentence)"
# "RETURN a, s "

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "cazzhack"))
# driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

chosenLang = 'EN'
numSentences =4

def get_sentences(article, language):
    with driver.session() as session:

        results = session.run("""MATCH (a:Article {{article: "{}" }}) <-[t:HAS_LANGUAGE_{}]-(s:Sentence) RETURN a,s,t""".format(article, language))

        # MATCH (a:Article {article: "AN"}) <-[t:HAS_LANGUAGE_EN]-(s:Sentence) RETURN a,s,t


        # results = session.run("MATCH (a:Article {article: {articleTag}})"
        #                       "<-[r:HAS_RIGHT_ANSWER_OF]-(s:Sentence)"
        #                       "<-[r:HAS_LANGUAGE_{lang}]-(s:Sentence)"
        #                       "RETURN a,r,s", articleTag=articleTag)
        nodes = []
        for count, record in enumerate(results):
            # print(record)
            nodes.append({"answer": record["a"]["article"], "sentence": record['s']['text'], "id": count})

        # print()
        # print(nodes)
        return nodes


final_sentences = []
final_sentences.append(get_sentences(article="AN", language=chosenLang))
final_sentences.append(get_sentences(article='THE', language=chosenLang))
final_sentences.append(get_sentences(article='(A)', language=chosenLang))
final_sentences.append(get_sentences(article='AN', language=chosenLang))
#
# flat_sentences_list = [item for sublist in final_sentences for item in sublist]
# # print(flat_sentences_list)
# sentences_count = len(flat_sentences_list)
# print(len(flat_sentences_list))
#
# from random import shuffle
#
# # randomizing in place
# shuffle(flat_sentences_list)
# #  ! put the shuffled list or idsList to session
#
# def extract(num):
#     idsList = []
#     for x in flat_sentences_list[0:num]:
#         if x not in idsList:
#             idsList.append(x)
#     print()
#     print(idsList)
#     print(len(idsList))
#
# extract(4)


def get_sentences(article, language):
    with driver.session() as session:

        results = session.run("""MATCH (a:Article {{article: "{}" }}) <-[t:HAS_LANGUAGE_{}]-(s:Sentence) RETURN a,s,t""".format(article, language))

        # MATCH (a:Article {article: "AN"}) <-[t:HAS_LANGUAGE_EN]-(s:Sentence) RETURN a,s,t


        # results = session.run("MATCH (a:Article {article: {articleTag}})"
        #                       "<-[r:HAS_RIGHT_ANSWER_OF]-(s:Sentence)"
        #                       "<-[r:HAS_LANGUAGE_{lang}]-(s:Sentence)"
        #                       "RETURN a,r,s", articleTag=articleTag)
        nodes = []
        for count, record in enumerate(results):
            # print(record)
            nodes.append({"answer": record["a"]["article"], "sentence": record['s']['text'], "id": count})

        # print()
        # print(nodes)
        return nodes
