from neo4j import GraphDatabase, basic_auth


def editThisSentence(text_id, new_text):

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:
        results = session.run(
            """MATCH (token:Sentence)
            WHERE id(token) = {id}
            SET token.text = "{new_text}"
            RETURN token
            """.format(id=text_id, new_text=new_text))