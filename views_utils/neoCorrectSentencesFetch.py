from neo4j import GraphDatabase, basic_auth

def neoCorrectSentencesFetch():

    flat_sentences_list = [
        {"sentenceWithMistake": "I drink a milk every day.", "sentenceWithoutMistake": "I drink milk every day."},
        {"sentenceWithMistake": "There is apple on the table.",
         "sentenceWithoutMistake": "There is an apple on the table."},
        {"sentenceWithMistake": "Can I get you a cup of a tea?",
         "sentenceWithoutMistake": "Can I get you a cup of tea?"},
        {"sentenceWithMistake": "This is a house that Jack built.",
         "sentenceWithoutMistake": "This is the house that Jack built."},
        {"sentenceWithMistake": "A trees produce oxygen.", "sentenceWithoutMistake": "Trees produce oxygen."},
        {"sentenceWithMistake": "Will you be back in the hour?",
         "sentenceWithoutMistake": "Will you be back in an hour?"},
        {"sentenceWithMistake": "A life will change a lot in 100 years.",
         "sentenceWithoutMistake": "Life will change a lot in 100 years."},
        {"sentenceWithMistake": "The lake Baikal is the deepest lake in the world.",
         "sentenceWithoutMistake": "Lake Baikal is the deepest lake in the world."},
        {"sentenceWithMistake": "What is a capital of Canada?",
         "sentenceWithoutMistake": "What is the capital of Canada?"},
        {"sentenceWithMistake": "My mother is a doctors.", "sentenceWithoutMistake": "My mother is a doctor."},
        {"sentenceWithMistake": "There were an interesting people at the party.",
         "sentenceWithoutMistake": "There were interesting people at the party."},
        {"sentenceWithMistake": "Are you coming to a party next Saturday?",
         "sentenceWithoutMistake": "Are you coming to the party next Saturday?"},
        {"sentenceWithMistake": "I bought new TV set yesterday.",
         "sentenceWithoutMistake": "I bought a new TV set yesterday."},
        {"sentenceWithMistake": "I think a man over there is very ill. He can't stand on his feet.",
         "sentenceWithoutMistake": "I think the man over there is very ill. He can't stand on his feet."},
        {"sentenceWithMistake": "I watched a video you had sent me.",
         "sentenceWithoutMistake": "I watched the video you had sent me."},
        {"sentenceWithMistake": "She was wearing a ugly dress when she met him.",
         "sentenceWithoutMistake": "She was wearing an ugly dress when she met him."},
        {"sentenceWithMistake": "I am crazy about reading a history books.",
         "sentenceWithoutMistake": "I am crazy about reading history books."},
        {"sentenceWithMistake": "She is an nice girl.", "sentenceWithoutMistake": "She is a nice girl."},
        {"sentenceWithMistake": "Do you want to go to a restaurant where we first met?",
         "sentenceWithoutMistake": "Do you want to go to the restaurant where we first met?"},
        {"sentenceWithMistake": "He is a engineer.", "sentenceWithoutMistake": "He is an engineer."},
        {"sentenceWithMistake": "He thinks that a love is what will save us all.",
         "sentenceWithoutMistake": "He thinks that love is what will save us all."},
        {"sentenceWithMistake": "We need to buy a sugar.", "sentenceWithoutMistake": "We need to buy sugar."},
        {"sentenceWithMistake": "I live in a house. A house is quite old and has four bedrooms.",
         "sentenceWithoutMistake": "I live in a house. The house is quite old and has four bedrooms."},
        {"sentenceWithMistake": "He lives in Washington near the Mount Rainier.",
         "sentenceWithoutMistake": "He lives in Washington near Mount Rainier."},
        {"sentenceWithMistake": "He writes a books.", "sentenceWithoutMistake": "He writes books."},
        {"sentenceWithMistake": "I'd like piece of cake.", "sentenceWithoutMistake": "I'd like a piece of cake."},
        {"sentenceWithMistake": "A car over there is fast.", "sentenceWithoutMistake": "The car over there is fast."},
        {"sentenceWithMistake": "My brother doesn't eat the meat. He is a vegeterian.",
         "sentenceWithoutMistake": "My brother doesn't eat meat. He is a vegeterian."},
        {"sentenceWithMistake": "She travelled to the Mexico last year.",
         "sentenceWithoutMistake": "She travelled to Mexico last year."},
        {"sentenceWithMistake": "Browns live next door.", "sentenceWithoutMistake": "The Browns live next door."},
        {"sentenceWithMistake": "That is girl I told you about.",
         "sentenceWithoutMistake": "That is the girl I told you about."},
        {"sentenceWithMistake": "What is highest building in the world?",
         "sentenceWithoutMistake": "What is the highest building in the world?"},
        {"sentenceWithMistake": "The mount Everest is the highest mountain.",
         "sentenceWithoutMistake": "Mount Everest is the highest mountain."},
        {"sentenceWithMistake": "I like reading a books.", "sentenceWithoutMistake": "I like reading books."},
        {"sentenceWithMistake": "I am looking for the new job.",
         "sentenceWithoutMistake": "I am looking for a new job."},
        {"sentenceWithMistake": "We arrived in a USA two days ago.",
         "sentenceWithoutMistake": "We arrived in the USA two days ago."},
        {"sentenceWithMistake": "I like the cats more than dogs.",
         "sentenceWithoutMistake": "I like cats more than dogs."},
        {"sentenceWithMistake": "He is already in the bed.", "sentenceWithoutMistake": "He is already in bed."},
        {"sentenceWithMistake": "You're not allowed to drive more than 50 miles the hour.",
         "sentenceWithoutMistake": "You're not allowed to drive more than 50 miles an hour."},
        {"sentenceWithMistake": "It was best meal I've ever eaten.",
         "sentenceWithoutMistake": "It was the best meal I've ever eaten."},
        {"sentenceWithMistake": "We usually go to work by a bus.",
         "sentenceWithoutMistake": "We usually go to work by bus."},
        {"sentenceWithMistake": "They always have the tea for breakfast.",
         "sentenceWithoutMistake": "They always have tea for breakfast."}]

    from random import shuffle
    # randomizing in place
    shuffle(flat_sentences_list)

    return flat_sentences_list

    # driver = GraphDatabase.driver("bolt://semantiqa.com:7687", auth=("neo4j", "cazzhack"))
    #
    # def get_sentences(article, language):
    #     with driver.session() as session:
    #         results = session.run(
    #             """MATCH (a:Article {{article: "{}" }}) <-[t:HAS_LANGUAGE_{}]-(s:Sentence) RETURN a,s,t""".format(
    #                 article, language))
    #
    #         nodes = []
    #         for count, record in enumerate(results):
    #
    #             nodes.append(
    #                 {"answer": record["a"]["article"], "sentence": record['s']['text'], "id": count})
    #
    #         return nodes
    #
    # final_sentences = []
    # final_sentences.append(get_sentences(article='A', language=chosenLang))
    # final_sentences.append(get_sentences(article='THE', language=chosenLang))
    # final_sentences.append(get_sentences(article='(A)', language=chosenLang))
    # final_sentences.append(get_sentences(article='AN', language=chosenLang))
    #
    # flat_sentences_list = [item for sublist in final_sentences for item in sublist]
    # # print(flat_sentences_list)
    # sentences_count = len(flat_sentences_list)
    #
    # from random import shuffle
    # # randomizing in place
    # shuffle(flat_sentences_list)
    #
    # return flat_sentences_list