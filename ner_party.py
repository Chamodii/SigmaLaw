import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('stanford-corenlp-full-2018-10-05', quiet=False)

text= "The attorney advised Lee that going to trial was “very risky” and that, if he pleaded guilty, he would receive a lighter sentence than he would if convicted at trial. App. 167. Lee informed his attorney of his noncitizen status and repeatedly asked him whether he would face deportation as a result of the criminal proceedings."

props = {'annotators': 'ner', 'pipelineLanguage': 'en'}
result = json.loads(nlp.annotate(text, properties=props))
r=result['sentences']

# NERs
def NER(r):
	
	ner=[]
	for each in r:
		q=each.get("tokens")
		for i in q:
			if (i.get("ner")=="PERSON" or i.get("ner")=="ORGANIZATION"):
				ner.append(i.get("word"))
	return ner
    			




print(NER(r))

#output-["Lee","Lee"]


