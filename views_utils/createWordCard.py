
from neo4j import GraphDatabase, basic_auth

# host = 'bolt://localhost:7473'
host = 'bolt://semantiqa.com:7687'
db_name = 'neo4j'
password = 'cazzhack'

driver = GraphDatabase.driver(host, auth=("neo4j", password))

def createWordCard(part_of_speech, name, translation, transcription, origin, antonyms, synonyms, collocations, gramm_forms, context_ru, context_en, img_base_64):
    """
    morph_type = NOUN, VERB, ADV, ADJ
    """
    with driver.session() as session:

        results = session.run("""
        MATCH (d:Dictionary {{node:'Dictionary'}})
        MERGE (d)-[rel:IS_{part_of_speech}]->(w:Word {{name: '{name}', translation: '{translation}', transcription: '{transcription}', origin:'{origin}', antonyms: '{antonyms}', synonyms: '{synonyms}', collocations: '{collocations}', grammForms: '{gramm_forms}', imgBase64: '{img_base_64}'  }})
        
        MERGE (w)-[r2:HAS_CONTEXT_RU]->(c1:Context {{contextRu: "{context_ru}"}})
        MERGE (w)-[r3:HAS_CONTEXT_EN]->(c2:Context {{contextEn: "{context_en}"}})
        
        RETURN id(w)""".format(part_of_speech=part_of_speech, name=name, translation=translation, transcription=transcription, origin=origin, antonyms=antonyms, synonyms=synonyms, collocations=collocations, gramm_forms=gramm_forms, context_ru=context_ru, context_en=context_en, img_base_64=img_base_64 ))

        nodes = []
        for record in results:
            print(record)
            nodes.append({
                "id": record['id(w)']
            })

        print(nodes)
        return nodes


# createWordCard(morph_type='NOUN', name='Test', translation='Книга', transcription='[buk]', origin='bkg', antonyms='antonym', synonyms='synonym', collocations='read', gramm_forms='books, to book', context_rus='вот book', context_eng='read a book')




