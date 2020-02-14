import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/home/chamodi/stanford-corenlp-full-2018-10-05', quiet=False)

# kbp extracts(subject, relation, object) triples from sentences.
props = {'annotators': 'ner, coref, kbp', 'pipelineLanguage': 'en'}


def potential_party(a):
    return (a + 0.8) / 2


def not_subject(a):
    return (a + 0.1) / 2


def subject_check(parties, kbps):
    for each in kbps:
        if len(each.get('kbp')) > 0:
            for i in parties:
                if each.get('kbp')[0].get('subject') == i:
                    parties[i] = potential_party(parties[i])

    print("After subject_check: ", parties)
    return parties


def build_complete_ner(word, ner, l):
    if (l[0].get('ner') == ner):
     word = word + " " + build_complete_ner(l[0].get("word"), l[0].get('ner'), l[1:len(l)])
    # print("built" + word)
    return word


# To update parties based on ner
def NER(parties, r):
    # props = {'annotators': 'ner', 'pipelineLanguage': 'en'}
    # result = json.loads(nlp.annotate(text, properties=props))
    # r = result['sentences']

    ner = []

    for each in sentences:
        q = each.get("tokens")
        # print(q)

        for j in range(0, len(q)):
            if q[j].get("ner") == "PERSON" or q[j].get("ner") == "ORGANIZATION":
                # print("test " + q[j].get("word"))
                word = build_complete_ner(q[j].get("word"), q[j].get("ner"), q[j + 1: len(q)])
                # print("final"+word)
                if j == 0:
                    ner.append(word)
                if j != 0 and q[j - 1].get("ner") != q[j].get("ner"):
                    ner.append(word)
    print(ner)

    for j in parties:
        if j in ner:
            parties[j] = potential_party(parties[j])

    print("After NER check: ", parties)

    return parties


text = 'Petitioner Jae Lee moved to the United States from South Korea with his parents when he was 13. In the 35 ' \
       'years he has spent in this country, he has never returned to South Korea, nor has he become a U. S. citizen, ' \
       'living instead as a lawful permanent resident. '
result = json.loads(nlp.annotate(text, properties=props))

sentences = result['sentences']

# Coref clusters
corefs = result['corefs']

# Calculate rough values for party_probability
parties = {}
init_value = 0.0
for each in corefs.values():
    parties[each[0].get('text')] = init_value


# Update probability if identified as a subject.
parties = subject_check(parties, sentences)

# Update probability with NER.
parties = NER(parties, sentences)

print(parties)




