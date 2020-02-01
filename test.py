import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/home/chamodi/stanford-corenlp-full-2018-10-05', quiet=False)

# kbp extracts(subject, relation, object) triples from sentences.
props = {'annotators': 'ner, coref, kbp', 'pipelineLanguage': 'en'}


def subject(a):
    return (a + 0.8) / 2


def not_subject(a):
    return (a + 0.1) / 2


def subject_check(parties, kbps):
    for each in kbps:
        if len(each.get('kbp')) > 0:
            for i in parties:
                if each.get('kbp')[0].get('subject') == i:
                    parties[i] = subject(parties[i])
    return parties


text = 'Barack Obama was born in Hawaii.  He is the president. Obama was elected in 2008. His wife is Mitchell. She is nice. That is at least what people think. But they are crazy anyways.'

result = json.loads(nlp.annotate(text, properties=props))

sentences = result['sentences']

# Coref clusters
corefs = result['corefs']

# Calculate rough values for party_probability
parties = {}
init_value = 1.0
for each in corefs.values():
    parties[each[0].get('text')] = init_value


# Update probability if identified as a subject.
parties = subject_check(parties, sentences)

print(parties)




