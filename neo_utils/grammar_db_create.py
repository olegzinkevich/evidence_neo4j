CREATE (anna:Person {name: 'Бочаров', surname: 'Станислав', id: 1})
CREATE (SyntaxConstructionAxis:SyntaxConstructionAxis {axis: 'SyntaxConstructionAxis'})

CREATE (Existence:Existence {token: 'Existence'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(Existence)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(Existence)

CREATE (PropertyEndow:PropertyEndow {token: 'PropertyEndow'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(PropertyEndow)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(PropertyEndow)

CREATE (Equating:Equating {token: 'Equating'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(Equating)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(Equating)

CREATE (PersonalAction:PersonalAction {token: 'PersonalAction'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(PersonalAction)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(PersonalAction)

CREATE (StandardModel:StandardModel {token: 'StandardModel'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(StandardModel)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(StandardModel)

CREATE (ExtendedModel:ExtendedModel {token: 'ExtendedModel'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(ExtendedModel)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(ExtendedModel)

CREATE (CausativeForm:CausativeForm {token: 'CausativeForm'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(CausativeForm)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(CausativeForm)

CREATE (Passive:Passive {token: 'Passive'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(Passive)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(Passive)

CREATE (GoalExpression:GoalExpression {token: 'GoalExpression'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(GoalExpression)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(GoalExpression)

CREATE (Desire:Desire {token: 'Desire'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(Desire)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(Desire)

CREATE (Imperative:Imperative {token: 'Imperative'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(Imperative)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(Imperative)

CREATE (CompoundSentence:CompoundSentence {token: 'CompoundSentence'})
CREATE (SyntaxConstructionAxis)<-[:TOKEN_BELONGS_TO_AXIS]-(CompoundSentence)
CREATE (anna)-[:KNOWS_AT_LEVEL_0 {timestamp: '19.02.2020', iteration: 0}]->(CompoundSentence)
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
#
