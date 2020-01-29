

import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('stanford-corenlp-full-2018-10-05', quiet=False)
props = {'annotators': 'ner', 'pipelineLanguage': 'en'}


text= "Lee, on the other hand, argues he can establish prejudice under Hill because he never would have accepted a guilty plea had he known that he would be deported as a result. Lee insists he would have gambled on trial, risking more jail time for whatever small chance there might be of an acquittal that would let him remain in the United States."

result = json.loads(nlp.annotate(text, properties=props))
r=result['sentences']
for each in r:
	q=each.get("tokens")
	for i in q:
		print(i.get("word"), i.get("ner"))
	
