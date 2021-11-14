from neo4j import GraphDatabase, basic_auth


def editUserPersonalInfo(user_id, name, surname, comment, email, middlename, phone, birthday):

    print('start function: editUserPersonalInfo')

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:
        results = session.run(
            """MATCH (node:Person)
            WHERE node.id = {user_id}
            SET node.name = "{name}"
            SET node.surname = "{surname}"
            SET node.comment = "{comment}"
            SET node.email = "{email}"
            SET node.middlename = "{middlename}"
            SET node.phone = "{phone}"
            SET node.birthday = "{birthday}"
            RETURN node
            """.format(user_id=user_id, name=name, surname=surname, comment=comment, email=email, middlename=middlename, phone=phone, birthday=birthday))