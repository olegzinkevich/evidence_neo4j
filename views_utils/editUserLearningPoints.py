from neo4j import GraphDatabase, basic_auth

def editUserLearningPoints(user_id, learning_point_a, learning_point_b):

    print('start function: editUserLearningPoints')

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:
        results = session.run(
            """MATCH (node:Person)
            WHERE node.id = {user_id}
            SET node.learningPointA = "{learning_point_a}"
            SET node.learningPointB = "{learning_point_b}"
            RETURN node
            """.format(user_id=user_id, learning_point_a=learning_point_a, learning_point_b=learning_point_b))

# editUserLearningPoints(user_id=2010, learning_point_a="Хочу изучить...", learning_point_b="ХОчу работать в компании...")