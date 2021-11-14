from neo4j import GraphDatabase, basic_auth

# chosenLang = RU or EN
def editArticlesSentences(chosenLang):

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    def get_sentences(article, language):
        with driver.session() as session:
            results = session.run(
                """MATCH (a:Article {{article: "{}" }}) <-[t:HAS_LANGUAGE_{}]-(s:Sentence) RETURN a, s,id(s)""".format(
                    article, language))

            nodes = []
            for count, record in enumerate(results):
                print(record)
                print()
                nodes.append(
                    {"answer": record["a"]["article"],
                     "sentence": record['s']['text'],
                     "id": record['id(s)']})

            return nodes

    final_sentences = []
    final_sentences.append(get_sentences(article='A', language=chosenLang))
    final_sentences.append(get_sentences(article='THE', language=chosenLang))
    final_sentences.append(get_sentences(article='(A)', language=chosenLang))
    final_sentences.append(get_sentences(article='AN', language=chosenLang))

    flat_sentences_list = [item for sublist in final_sentences for item in sublist]

    return flat_sentences_list

# print(neoArticlesSentencesFetch(chosenLang='EN'))