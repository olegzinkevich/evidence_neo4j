queries = [
           '''MATCH (person:Person {id: 6}), (token:Existence {token: 'Existence'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token''',
    '''MATCH (person:Person {id: 6}), (token:PropertyEndow {token: 'PropertyEndow'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token ''',
    '''MATCH (person:Person {id: 6}), (token:Equating {token: 'Equating'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token ''',
    ''' MATCH (person:Person {id: 6}), (token:PersonalAction {token: 'PersonalAction'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token''',
    '''MATCH (person:Person {id: 6}), (token:StandardModel {token: 'StandardModel'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token ''',
    '''MATCH (person:Person {id: 6}), (token:ExtendedModel {token: 'ExtendedModel'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token ''',
    ''' MATCH (person:Person {id: 6}), (token:CausativeForm {token: 'CausativeForm'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token''',
    '''MATCH (person:Person {id: 6}), (token:Passive {token: 'Passive'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token ''',
    ''' MATCH (person:Person {id: 6}), (token:GoalExpression {token: 'GoalExpression'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token''', '''
MATCH (person:Person {id: 6}), (token:Desire {token: 'Desire'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token ''',
    '''MATCH (person:Person {id: 6}), (token:Imperative {token: 'Imperative'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token''',
    ''' MATCH (person:Person {id: 6}), (token:CompoundSentence {token: 'CompoundSentence'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token''' ]

for statement in queries:

    from neo4j import GraphDatabase, basic_auth

    # host = 'bolt://localhost:7687'
    host = 'bolt://semantiqa.com:7687'
    db_name = 'neo4j'
    password = 'cazzhack'

    driver = GraphDatabase.driver(host, auth=("neo4j", password))

    with driver.session() as session:

        results = session.run(statement)






















