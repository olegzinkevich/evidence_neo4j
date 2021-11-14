from neo4j import GraphDatabase, basic_auth

def neoArticlesPreliminaryTestFetch(chosenLang):

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    def fetchSentences(article, language):

        with driver.session() as session:
            results = session.run(
                """MATCH (a:Article {{article: "{}" }}) <-[t:HAS_LANGUAGE_{}]-(s:Sentence {{ preliminary_test: "yes" }}) RETURN a,s,t""".format(
                    article, language))

            nodes = []
            for count, record in enumerate(results):

                nodes.append(
                    {"rightAnswer": record["a"]["article"], "preliminary_test": record["s"]["preliminary_test"], "sentence": record['s']['text'], "id": count})

            return nodes

    final_sentences = []
    final_sentences.append(fetchSentences(article='THE', language=chosenLang))
    final_sentences.append(fetchSentences(article='A', language=chosenLang))
    final_sentences.append(fetchSentences(article='AN', language=chosenLang))
    final_sentences.append(fetchSentences(article='(-)', language=chosenLang))

    flat_sentences_list = [item for sublist in final_sentences for item in sublist]

    from random import shuffle
    # randomizing in place
    shuffle(flat_sentences_list)

    return flat_sentences_list

# print(neoArticlesPreliminaryTestFetch('EN'))