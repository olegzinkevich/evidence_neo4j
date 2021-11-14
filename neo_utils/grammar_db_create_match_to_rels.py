MATCH (person:Person {id: 3}), (token:Existence {token: 'Existence'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:PropertyEndow {token: 'PropertyEndow'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:Equating {token: 'Equating'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:PersonalAction {token: 'PersonalAction'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:StandardModel {token: 'StandardModel'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:ExtendedModel {token: 'ExtendedModel'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:CausativeForm {token: 'CausativeForm'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:Passive {token: 'Passive'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:GoalExpression {token: 'GoalExpression'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:Desire {token: 'Desire'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token


MATCH (person:Person {id: 3}), (token:Imperative {token: 'Imperative'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token

MATCH (person:Person {id: 3}), (token:CompoundSentence {token: 'CompoundSentence'})
CREATE (person)-[:KNOWS_AT_LEVEL_1 {timestamp: '19.02.2020', iteration: 0}]->(token)
return person, token




#
# 	CREATE (SubjectClause:SubjectClause {token: 'SubjectClause'})
#     CREATE (CompoundSentence)<-[:TOKEN_BELONGS_TO_TOKEN]-(SubjectClause)
#     CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(SubjectClause)
#
# 	CREATE (ObjectClause:ObjectClause {token: 'ObjectClause'})
#     CREATE (CompoundSentence) < -[: TOKEN_BELONGS_TO_TOKEN]-(ObjectClause)
#     CREATE (anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(ObjectClause)
#
# 	CREATE (AttributiveСlause:AttributiveСlause {token: 'AttributiveСlause'})
#     CREATE(CompoundSentence) < -[: TOKEN_BELONGS_TO_TOKEN]-(AttributiveСlause)
#     CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AttributiveСlause)
#
# 		CREATE (AttributiveDefining:AttributiveDefining {token: 'AttributiveDefining'})
#         CREATE(AttributiveСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AttributiveDefining)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AttributiveDefining)
#
# 		CREATE (AttributiveNonDefining:AttributiveNonDefining {token: 'AttributiveNonDefining'})
#         CREATE(AttributiveСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AttributiveNonDefining)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AttributiveNonDefining)
#
#         CREATE (AdverbialСlause:AdverbialСlause {token: 'AdverbialСlause'})
#         CREATE(CompoundSentence) < -[: TOKEN_BELONGS_TO_TOKEN]-(AdverbialСlause)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AdverbialСlause)
#
#             CREATE (AdverbialOfTime:AdverbialOfTime {token: 'AdverbialOfTime'})
#             CREATE(AdverbialСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AdverbialOfTime)
#             CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AdverbialOfTime)
#
# 		CREATE (AdverbialOfPlace:AdverbialOfPlace {token: 'AdverbialOfPlace'})
#         CREATE(AdverbialСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AdverbialOfPlace)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AdverbialOfPlace)
#
# 		CREATE (AdverbialOfCondition:AdverbialOfCondition {token: 'AdverbialOfCondition'})
#         CREATE(AdverbialСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AdverbialOfCondition)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AdverbialOfCondition)
#
# 		CREATE (AdverbialOfPurpose:AdverbialOfPurpose {token: 'AdverbialOfPurpose'})
#         CREATE(AdverbialСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AdverbialOfPurpose)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AdverbialOfPurpose)
#
# 		CREATE (AdverbialOfResult:AdverbialOfResult {token: 'AdverbialOfResult'})
#         CREATE(AdverbialСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AdverbialOfResult)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AdverbialOfResult)
#
# 		CREATE (AdverbialOfReason:AdverbialOfReason {token: 'AdverbialOfReason'})
#         CREATE(AdverbialСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AdverbialOfReason)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AdverbialOfReason)
#
# 		CREATE (AdverbialOfConcession:AdverbialOfConcession {token: 'AdverbialOfConcession'})
#         CREATE(AdverbialСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AdverbialOfConcession)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AdverbialOfConcession)
#
# 		CREATE (AdverbialOfManner:AdverbialOfManner {token: 'AdverbialOfManner'})
#         CREATE(AdverbialСlause) < -[: TOKEN_BELONGS_TO_TOKEN]-(AdverbialOfManner)
#         CREATE(anna) - [: KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(AdverbialOfManner)
#

# !!!!!!!!!!!!!!! Create rels to a new created person

CREATE (person:Person { id: 1000, name: 'Testname', surname: 'Testsurname', comment: 'Comment' })
WITH person
            MATCH (Existence:Existence {token: 'Existence'})
            CREATE (person)-[:KNOWS_AT_LEVEL_1 { timestamp: '19.15.2019', iteration: 0} ]->(Existence)
WITH person
            MATCH (PropertyEndow:PropertyEndow {token: 'PropertyEndow'})
            CREATE (person)-[:KNOWS_AT_LEVEL_1 { timestamp: '19.15.2019', iteration: 0 }]->(PropertyEndow)
WITH person
            MATCH (Equating:Equating {token: 'Equating'})
            CREATE (person)-[:KNOWS_AT_LEVEL_1 { timestamp: '19.15.2019', iteration: 0 }]->(Equating)
            return person
#
