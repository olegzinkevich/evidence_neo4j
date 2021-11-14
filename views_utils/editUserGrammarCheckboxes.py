from neo4j import GraphDatabase, basic_auth

def editUserGrammarCheckboxes(user_id, checkboxes):

    print('start function: editUserGrammarCheckboxes')

    driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))

    with driver.session() as session:
        results = session.run(
            """MATCH (node:Person {{id: {user_id} }})-[r:HAS_PERSONAL_GRAMMAR_MAP]->(b:GrammarCheckboxes)
            SET r.checkboxes = "{checkboxes}"
            RETURN node, r
            """.format(user_id=user_id, checkboxes=checkboxes))


# dbChecksArray = {
#     "adjectivesDegreesOfComparison_Comparative": "false",
#     "adjectivesDegreesOfComparison_Positive": "false",
#     "adjectivesDegreesOfComparison_Superlative": "false",
#     "adverbsDegreesOfComparison_Comparative": "false",
#     "adverbsDegreesOfComparison_Positive": "false",
#     "adverbsDegreesOfComparison_Superlative": "false",
#     "articles_Definite": "false",
#     "articles_Indefinite": "false",
# #     "articles_Zero": "false",
# #     "baseSyntax_CausativeForm": "true",
# #     "baseSyntax_CompoundSentence": "true",
# #     "baseSyntax_Desire": "false",
# #     "baseSyntax_Equating": "false",
# #     "baseSyntax_ExistenceConcept": "false",
# #     "baseSyntax_ExtendedModel": "false",
# #     "baseSyntax_GoalExpression": "false",
# #     "baseSyntax_Imperative": "false",
# #     "baseSyntax_Passive": "false",
# #     "baseSyntax_PersonalAction": "false",
# #     "baseSyntax_PropertyEndow": "false",
# #     "baseSyntax_StandardModel": "false",
# #     "baseEnglishSentence_StandardModel": "false",
#     "conditionalSentences_MixType": "false",
#     "conditionalSentences_RealPresentFuture": "false",
#     "conditionalSentences_UnrealPast": "false",
#     "conditionalSentences_UnrealPresentFuture": "false",
#     "determinants_Articles": "false",
#     "determinants_CardinalNumbers": "false",
#     "determinants_Demonstrative": "false",
#     "determinants_Posessive": "false",
#     "determinants_SetPointers": "false",
#     "modality_BeAble": "false",
#     "modality_Can": "false",
#     "modality_Could": "false",
#     "modality_HaveTo": "false",
#     "modality_May": "false",
#     "modality_Might": "false",
#     "modality_Must": "false",
#     "modality_Need": "false",
#     "modality_PastModals": "false",
#     "modality_Shall": "false",
#     "modality_Should": "false",
#     "modality_Will": "false",
#     "modality_Would": "false",
#     "orderOfAdjectives": "false",
#     "sentenceTypes_Interrogative": "false",
#     "sentenceTypes_Narrative": "false",
#     "sentenceTypes_QuestionTypeIsIt": "false",
#     "sentenceTypes_QuestionTypeIsntIt": "false",
#     "sentenceTypes_QuestionTypeOrOr": "false",
#     "sentenceTypes_QuestionTypeSpecial": "false",
#     "sentenceTypes_QuestionTypeYesNo": "false",
#     "sentenceTypes_SentenceFormNegative": "false",
#     "sentenceTypes_SentenceFormPositive": "false",
#     "sequenceOfTenses_ComplexSentences": "false",
#     "sequenceOfTenses_IndirectSpeech": "false",
#     "sequenceOfTenses_Passive": "false",
#     "syntaxClarifications_ComplexObject": "false",
#     "syntaxClarifications_ComplexSubject": "false",
#     "syntaxClarifications_CompoundSentenceVariants": "false",
#     "syntaxClarifications_ExtendedStandardModel": "false",
#     "tenses_FutureContinuous": "false",
#     "tenses_FuturePerfect": "false",
#     "tenses_FuturePerfectContinuous": "false",
#     "tenses_FutureSimpleEvent": "false",
#     "tenses_FutureSimpleGeneral": "false",
#     "tenses_PastContinuous": "false",
#     "tenses_PastPerfect": "false",
#     "tenses_PastPerfectContinuous": "false",
#     "tenses_PastSimpleEvent": "false",
#     "tenses_PastSimpleGeneral": "false",
#     "tenses_PresentContinuous": "false",
#     "tenses_PresentPerfect": "false",
#     "tenses_PresentPerfectContinuous": "false",
#     "tenses_PresentSimpleGeneral": "false",
#     "verbForms_Imperative": "false",
#     "verbForms_Infinitive": "false",
#     "verbForms_ParticipleOfCompletedAction": "false",
#     "verbForms_ParticipleOfContinuingAction": "false",
#     "verbForms_PastTenseForm": "false",
#     "verbForms_PresentTenseFormHeShe": "false",
#     "verbForms_PresentTenseFormIWe": "false",
# }

# editUserGrammarCheckboxes(user_id=2010, checkboxes=dbChecksArray)