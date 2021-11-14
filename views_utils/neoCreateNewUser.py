from neo4j import GraphDatabase, basic_auth
import json

# host = 'bolt://localhost:7687'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password), max_connection_lifetime=200)

tokensList = ['Existence', 'PropertyEndow', 'Equating', 'PersonalAction', 'StandardModel', 'ExtendedModel', 'CausativeForm', 'Passive', 'GoalExpression', 'Desire', 'Imperative', 'CompoundSentence', 'Present', 'Past', 'Future', 'General', 'Event', 'Continuous', 'Perfect', 'PerfectContinuous', 'Positive', 'Negative', 'Narrative', 'Question', 'Zero', 'PhysicalAbility', 'Assumptions', 'SociallyManipulative', 'Politeness', 'Fantasy', 'IndirectSpeech', 'ConditionalSentences', 'DoAmplifier', 'DoubleNegation', 'Exclamation', 'ItIsThatWho', 'ItIsNotUntil', 'NotTill', 'FutureSimpleEvent', 'PastSimpleEvent', 'FutureSimpleGeneral', 'PresentSimpleGeneral', 'PastSimpleGeneral', 'FutureContinuous', 'PresentContinuous', 'PastContinuous','FuturePerfeсt','PresentPerfect','PastPerfect','FuturePerfectContinuous','PresentPerfectContinuous', 'PastPerfectContinuous','Must','Can','Could','May','Might','Shall','Should','Will','Would','WouldBetter','HadRather','Dare','Let','Need','HaveTo','BeAbleTo','BeAllowedTo','BeAllowedTo','BeGoingTo','BeTo','UsedTo','Would','BeUsedTo','GetUsedTo','Noun','ProperName','PersonalPronoun','Possessive','Demonstrative','CardinalNumbers','SetPointers','NounObject','ProperNameObject','ObjectPronoun','PossessivePronounObject','Plural','Singular','Сountable','Uncountable','DoAuxiliary','BeAuxiliary','WillAuxiliary','HaveAuxiliary','Infinitive','PresentTenseFormIWe','PresentTenseFormHeShe','ParticipleOfContinuingAction','PastTenseForm','ParticipleOfCompletedAction','Indefinite', 'Negative','Reflexive','Mutual','AdjectivesOrder','DegreesOfComparison','SSingular','SPlural','OfForm','AdverbsOrder','AdverbsDegreesOfComparison','AdverbsTypes']

personalGrammarMapCheckboxes = """{
    'adjectivesDegreesOfComparison_Comparative': 'false',
    'adjectivesDegreesOfComparison_Positive': 'false',
    'adjectivesDegreesOfComparison_Superlative': 'false',
    'adverbsDegreesOfComparison_Comparative': 'false',
    'adverbsDegreesOfComparison_Positive': 'false',
    'adverbsDegreesOfComparison_Superlative': 'false',
    'articles_Definite': 'false',
    'articles_Indefinite': 'false',
    'articles_Zero': 'false',
    'baseSyntax_CausativeForm': 'false',
    'baseSyntax_CompoundSentence': 'false',
    'baseSyntax_Desire': 'false',
    'baseSyntax_Equating': 'false',
    'baseSyntax_ExistenceConcept': 'false',
    'baseSyntax_ExtendedModel': 'false',
    'baseSyntax_GoalExpression': 'false',
    'baseSyntax_Imperative': 'false',
    'baseSyntax_Passive': 'false',
    'baseSyntax_PersonalAction': 'false',
    'baseSyntax_PropertyEndow': 'false',
    'baseSyntax_StandardModel': 'false',
    'baseEnglishSentence_StandardModel': 'false',
    'conditionalSentences_MixType': 'false',
    'conditionalSentences_RealPresentFuture': 'false',
    'conditionalSentences_UnrealPast': 'false',
    'conditionalSentences_UnrealPresentFuture': 'false',
    'determinants_Articles': 'false',
    'determinants_CardinalNumbers': 'false',
    'determinants_Demonstrative': 'false',
    'determinants_Posessive': 'false',
    'determinants_SetPointers': 'false',
    'modality_BeAble': 'false',
    'modality_Can': 'false',
    'modality_Could': 'false',
    'modality_HaveTo': 'false',
    'modality_May': 'false',
    'modality_Might': 'false',
    'modality_Must': 'false',
    'modality_Need': 'false',
    'modality_PastModals': 'false',
    'modality_Shall': 'false',
    'modality_Should': 'false',
    'modality_Will': 'false',
    'modality_Would': 'false',
    'orderOfAdjectives': 'false',
    'sentenceTypes_Interrogative': 'false',
    'sentenceTypes_Narrative': 'false',
    'sentenceTypes_QuestionTypeIsIt': 'false',
    'sentenceTypes_QuestionTypeIsntIt': 'false',
    'sentenceTypes_QuestionTypeOrOr': 'false',
    'sentenceTypes_QuestionTypeSpecial': 'false',
    'sentenceTypes_QuestionTypeYesNo': 'false',
    'sentenceTypes_SentenceFormNegative': 'false',
    'sentenceTypes_SentenceFormPositive': 'false',
    'sequenceOfTenses_ComplexSentences': 'false',
    'sequenceOfTenses_IndirectSpeech': 'false',
    'sequenceOfTenses_Passive': 'false',
    'syntaxClarifications_ComplexObject': 'false',
    'syntaxClarifications_ComplexSubject': 'false',
    'syntaxClarifications_CompoundSentenceVariants': 'false',
    'syntaxClarifications_ExtendedStandardModel': 'false',
    'tenses_FutureContinuous': 'false',
    'tenses_FuturePerfect': 'false',
    'tenses_FuturePerfectContinuous': 'false',
    'tenses_FutureSimpleEvent': 'false',
    'tenses_FutureSimpleGeneral': 'false',
    'tenses_PastContinuous': 'false',
    'tenses_PastPerfect': 'false',
    'tenses_PastPerfectContinuous': 'false',
    'tenses_PastSimpleEvent': 'false',
    'tenses_PastSimpleGeneral': 'false',
    'tenses_PresentContinuous': 'false',
    'tenses_PresentPerfect': 'false',
    'tenses_PresentPerfectContinuous': 'false',
    'tenses_PresentSimpleGeneral': 'false',
    'verbForms_Imperative': 'false',
    'verbForms_Infinitive': 'false',
    'verbForms_ParticipleOfCompletedAction': 'false',
    'verbForms_ParticipleOfContinuingAction': 'false',
    'verbForms_PastTenseForm': 'false',
    'verbForms_PresentTenseFormHeShe': 'false',
    'verbForms_PresentTenseFormIWe': 'false',
}"""

def neoCreateNewUser(clientId, clientName, clientSurname, clientComment, clientBirthday, clientMiddlename, clientEmail, clientPhone, timestamp):
    print('starting function neoCreateNewUser()')

    with driver.session() as session:
        session.run(
            '''MERGE (person:Person {{ id: {client_id}, name: "{name}", surname: "{surname}", comment: "{comment}", birthday: "{birthday}", middlename: "{middle_name}", email:"{email}", phone:"{phone}", registered: "{timestamp}", learningPointA: "", learningPointB: "" }})'''.format(client_id=clientId, name=clientName, surname=clientSurname, comment=clientComment, birthday=clientBirthday, middle_name=clientMiddlename, email=clientEmail, phone=clientPhone, timestamp=timestamp)
            )

    # adding learning checkboxes for personal grammar map
    with driver.session() as session:
        session.run(
            '''MATCH (person:Person {{ id: {client_id} }})
            WITH person
            MATCH (GrammarCheckboxes:GrammarCheckboxes)
            MERGE (person)-[:HAS_PERSONAL_GRAMMAR_MAP {{checkboxes: "{personalGrammarMapCheckboxes}" }}]->(GrammarCheckboxes)
            '''.format(client_id=clientId, personalGrammarMapCheckboxes=personalGrammarMapCheckboxes)
        )

    for tkn in tokensList:
        print('token rel saved for: ', tkn)

        # When using MERGE on full patterns, the behavior is that either the whole pattern matches, or the whole pattern is created. MERGE will not partially use existing patterns — it’s all or nothing.

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
#
# neoCreateNewUser(clientId=5600, clientName='Yp', clientSurname='yuy', clientComment='some comment', timestamp='04.03.2020', clientBirthday='', clientMiddlename='', clientEmail='', clientPhone='')