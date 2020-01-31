import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/home/chamodi/stanford-corenlp-full-2018-10-05', quiet=False)

# kbp extracts(subject, relation, object) triples from sentences.
props = {'annotators': 'ner, coref, kbp', 'pipelineLanguage': 'en'}


def subject(a):
    return (a + 0.8) / 2


def not_subject(a):
    return (a + 0.1) / 2


text = 'Barack Obama was born in Hawaii.  He is the president. Obama was elected in 2008. His wife is Mitchell. She is nice. That is at least what people think. But they are crazy anyways.'

result = json.loads(nlp.annotate(text, properties=props))

r = result['sentences']

# NERs
for each in r:
    q = each.get("tokens")
    print(q)
    for i in q:
        print(i.get("word"), i.get("ner"))

# Coref clusters
corefs = result['corefs']
for each in corefs.values():
    print(each)

# For identifying the subject
for each in r:
    print(each.get('kbp'))

# Calculate rough values for party_probability
parties = {}
init_value = 1.0
for each in corefs.values():
    parties[each[0].get('text')] = init_value


# Update probability if identified as a subject.
kbps = result['sentences']
for each in kbps:
    if len(each.get('kbp')) > 0:
        for i in parties:
            if each.get('kbp')[0].get('subject') == i:
                parties[i] = subject(parties[i])
