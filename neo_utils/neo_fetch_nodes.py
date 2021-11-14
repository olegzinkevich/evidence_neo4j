from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def getArticleSentences(article, language):
    with driver.session() as session:
        results = session.run(
            """MATCH (a:Article {{article: "{}" }}) <-[t:HAS_LANGUAGE_{}]-(s:Sentence) RETURN a,s,t""".format(
                article, language))

        # results = session.run("MATCH (a:Article {article: {articleTag}})"
        #                       "<-[r:HAS_RIGHT_ANSWER_OF]-(s:Sentence)"
        #                       "RETURN a,r,s", articleTag=articleTag)
        nodes = []
        for count, record in enumerate(results):
            # print(record)
            nodes.append(
                {"answer": record["a"]["article"], "preliminary_test": record["s"]["preliminary_test"], "sentence": record['s']['text'], "id": count})

        # print()
        print(nodes)
        return nodes

# final_sentences = []
# final_sentences.append(getArticleSentences(article='A', language=chosenLang))
# final_sentences.append(getArticleSentences(article='A', language='RU'))
# final_sentences.append(getArticleSentences(article='(A)', language=chosenLang))
# final_sentences.append(getArticleSentences(article='AN', language=chosenLang))
# print(final_sentences)

# flat_sentences_list = [item for sublist in final_sentences for item in sublist]
# # print(flat_sentences_list)
# sentences_count = len(flat_sentences_list)
# print('sentences count', sentences_count)


#########################################################
##### Fetch prepositions sentences
#########################################################

def getPrepositionsSentences(preposition, preposition_type, language):
    with driver.session() as session:
        results = session.run(
            """MATCH (a:Preposition {{preposition: "{0}" }})
            MATCH(a)<-[b:HAS_LANGUAGE_{1}]-(s:Sentence)
            MATCH(a)<-[c:HAS_TYPE_{2}]-(s:Sentence) RETURN a,s""".format(
                preposition, language, preposition_type))
        nodes = []
        for count, record in enumerate(results):
            # print(record)
            nodes.append(
                {"answer": record["a"]["preposition"], "sentence": record['s']['text'], "id": count})

        # print()
        print(nodes)
        return nodes

# getPrepositionsSentences(preposition='AT', preposition_type='OF_PLACE', language='RU')

########################################################
#### Fetch sentences for correction
########################################################

def getArticlesSentencesPreliminaryTest(article, language):
    with driver.session() as session:
        results = session.run(
            """MATCH (a:Article {{article: "{}" }}) <-[t:HAS_LANGUAGE_{}]-(s:Sentence {{ preliminary_test: "yes" }}) RETURN a,s,t""".format(
                article, language))

        nodes = []
        for count, record in enumerate(results):
            # print(record)
            nodes.append(
                {"answer": record["a"]["article"], "preliminary_test": record["s"]["preliminary_test"], "sentence": record['s']['text'], "id": count})

        # print()
        print(nodes)
        return nodes

# final_sentences = []
# final_sentences.append(getArticlesSentencesPreliminaryTest(article='THE', language='EN'))
# final_sentences.append(getArticlesSentencesPreliminaryTest(article='A', language='EN'))
# final_sentences.append(getArticlesSentencesPreliminaryTest(article='AN', language='EN'))
# final_sentences.append(getArticlesSentencesPreliminaryTest(article='(A)', language='EN'))
# print(final_sentences)
#
# flat_sentences_list = [item for sublist in final_sentences for item in sublist]
# print(flat_sentences_list)
# sentences_count = len(flat_sentences_list)
# print('sentences count', sentences_count)

########################################################
#### Fetch Node and its relashionships with final tokens
########################################################

def grammarMapFetch(user_id):

    #  getting UTC timestamp
    from time import gmtime, strftime
    timestamp = strftime("%Y-%m-%d", gmtime())


    with driver.session() as session:
        results = session.run(
            '''MATCH(person: Person {{id: {user_id} }})-[relashionship]->(token)
        RETURN person, relashionship, token'''.format(user_id=user_id)
        )

        nodes = []
        for count, record in enumerate(results):
            # print(record)
            nodes.append({
                "id": record["person"]["id"],
                "name": record["person"]["name"],
                "surname": record["person"]["surname"],
                "axis": record["token"]["axis_name"],
                "token": record["token"]["token"],
                "relashionship": record["relashionship"].type,
                "relashionship_timestamp": record["relashionship"]["timestamp"],
                "relashionship_iteration": record["relashionship"]["iteration"],
                "current_timestamp": timestamp
            })

        import json
        json_array = json.dumps(nodes, indent=2, ensure_ascii=False)


        print(nodes)
        print()
        print(json_array)

        return nodes


grammarMapFetch(user_id=1)




