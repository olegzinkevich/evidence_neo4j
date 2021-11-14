from neo4j import GraphDatabase, basic_auth

def neoPrepositionsSentencesFetch(grammarType, chosenLang):
    """ grammarType = 'OF_TIME', 'OF_PLACE',
        chosenLang = 'RU', 'EN' """

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    def getPrepositionsSentences(preposition, preposition_type, language):

        with driver.session() as session:

                results = session.run(
                    """MATCH (a:Preposition {{preposition: "{0}" }})
                    MATCH(a)<-[b:HAS_LANGUAGE_{1}]-(s:Sentence)
                    MATCH(a)<-[c:HAS_TYPE_{2}]-(s:Sentence) RETURN a,s, id(s)""".format(
                        preposition, language, preposition_type))

                nodes = []
                for count, record in enumerate(results):

                    nodes.append(
                        {"rightAnswer": record["a"]["preposition"],
                         "sentence": record['s']['text'],
                         "id": record['id(s)']})

                return nodes

    final_sentences = []
    final_sentences.append(getPrepositionsSentences(preposition='AT', preposition_type=grammarType, language=chosenLang))
    final_sentences.append(getPrepositionsSentences(preposition='AT', preposition_type=grammarType, language=chosenLang))
    final_sentences.append(getPrepositionsSentences(preposition='AT', preposition_type=grammarType, language=chosenLang))
    final_sentences.append(getPrepositionsSentences(preposition='ON', preposition_type=grammarType, language=chosenLang))
    final_sentences.append(getPrepositionsSentences(preposition='ON', preposition_type=grammarType, language=chosenLang))
    final_sentences.append(getPrepositionsSentences(preposition='ON', preposition_type=grammarType, language=chosenLang))
    final_sentences.append(getPrepositionsSentences(preposition='IN', preposition_type=grammarType, language=chosenLang))
    final_sentences.append(getPrepositionsSentences(preposition='IN', preposition_type=grammarType, language=chosenLang))
    final_sentences.append(getPrepositionsSentences(preposition='IN', preposition_type=grammarType, language=chosenLang))

    flat_sentences_list = [item for sublist in final_sentences for item in sublist]

    from random import shuffle
    # randomizing in place
    shuffle(flat_sentences_list)

    return flat_sentences_list

# print(neoPrepositionsSentencesFetch(grammarType='OF_PLACE', chosenLang='RU'))