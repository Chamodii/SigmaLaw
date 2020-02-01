import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('stanford-corenlp-full-2018-10-05', quiet=False)


#To increase the value if the word is a person or organization
def potential_party(a):
    return (a + 0.9) / 2

#To update parties based on ner
def NER(text,nlp,parties):
	props = {'annotators': 'ner', 'pipelineLanguage': 'en'}
	result = json.loads(nlp.annotate(text, properties=props))
	r=result['sentences']
	
	ner=[]
	for each in r:
		q=each.get("tokens")
		for i in q:
			if (i.get("ner")=="PERSON" or i.get("ner")=="ORGANIZATION"):
				ner.append(i.get("word"))
	for j in parties:
		if j in ner:
			parties[j] = potential_party(parties[j])

	return parties
    			







