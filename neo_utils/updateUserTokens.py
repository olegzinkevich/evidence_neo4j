from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

tokensList = ['Existence', 'PropertyEndow', 'Equating', 'PersonalAction', 'StandardModel', 'ExtendedModel', 'CausativeForm', 'Passive', 'GoalExpression', 'Desire', 'Imperative', 'CompoundSentence', 'Present', 'Past', 'Future', 'General', 'Event', 'Continuous', 'Perfect', 'PerfectContinuous', 'Positive', 'Negative', 'Narrative', 'Question', 'Zero', 'PhysicalAbility', 'Assumptions', 'SociallyManipulative', 'Politeness', 'Fantasy', 'IndirectSpeech', 'ConditionalSentences', 'DoAmplifier', 'DoubleNegation', 'Exclamation', 'ItIsThatWho', 'ItIsNotUntil', 'NotTill', 'FutureSimpleEvent', 'PastSimpleEvent', 'FutureSimpleGeneral', 'PresentSimpleGeneral', 'PastSimpleGeneral', 'FutureContinuous', 'PresentContinuous', 'PastContinuous','FuturePerfeсt','PresentPerfect','PastPerfect','FuturePerfectContinuous','PresentPerfectContinuous', 'PastPerfectContinuous','Must','Can','Could','May','Might','Shall','Should','Will','Would','WouldBetter','HadRather','Dare','Let','Need','HaveTo','BeAbleTo','BeAllowedTo','BeAllowedTo','BeGoingTo','BeTo','UsedTo','Would','BeUsedTo','GetUsedTo','Noun','ProperName','PersonalPronoun','Possessive','Demonstrative','CardinalNumbers','SetPointers','NounObject','ProperNameObject','ObjectPronoun','PossessivePronounObject','Plural','Singular','Сountable','Uncountable','DoAuxiliary','BeAuxiliary','WillAuxiliary','HaveAuxiliary','Infinitive','PresentTenseFormIWe','PresentTenseFormHeShe','ParticipleOfContinuingAction','PastTenseForm','ParticipleOfCompletedAction','Indefinite', 'Negative','Reflexive','Mutual','AdjectivesOrder','DegreesOfComparison','SSingular','SPlural','OfForm','AdverbsOrder','AdverbsDegreesOfComparison','AdverbsTypes']

# When using MERGE on full patterns, the behavior is that either the whole pattern matches, or the whole pattern is created. MERGE will not partially use existing patterns — it’s all or nothing.

def neoUpdateUser(clientId, timestamp):

    for tkn in tokensList:
        print('token rel updated for: ', tkn)

        with driver.session() as session:
            results = session.run(
                '''MATCH (person:Person {{ id: {client_id} }})
        
                WITH person
                MATCH ({token}:{token} {{token: '{token}'}})
                MERGE (person)-[:KNOWS_AT_LEVEL_1 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                MERGE (person)-[:KNOWS_AT_LEVEL_2 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                MERGE (person)-[:KNOWS_AT_LEVEL_3 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                MERGE (person)-[:KNOWS_AT_LEVEL_4 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                MERGE (person)-[:KNOWS_AT_LEVEL_5 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                MERGE (person)-[:KNOWS_AT_LEVEL_6 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                MERGE (person)-[:KNOWS_AT_LEVEL_7 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                MERGE (person)-[:KNOWS_AT_LEVEL_8 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                MERGE (person)-[:KNOWS_AT_LEVEL_9 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                MERGE (person)-[:KNOWS_AT_LEVEL_10 {{ timestamp: "{timestamp}", iteration: 0}} ]->({token})
                '''.format(client_id=clientId, token=tkn, timestamp=timestamp)
            )

neoUpdateUser(clientId=64,  timestamp='25.02.2020')