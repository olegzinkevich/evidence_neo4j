from neo4j import GraphDatabase, basic_auth

def articlesSentencesFetchByType(article, language):

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:
        results = session.run(
            """MATCH (a:Article {{article: "{}" }}) <-[t:HAS_LANGUAGE_{}]-(s:Sentence) RETURN a, s,id(s)""".format(article, language))

        nodes = []
        for record in results:
            nodes.append(
                {"answer": record["a"]["article"],
                 "sentence": record['s']['text'],
                 "id": record['id(s)']})

        return nodes

# print(articlesSentencesFetchByType(article='(A)', language='RU'))