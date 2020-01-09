
import json
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/home/chamodi/stanford-corenlp-full-2018-10-05', quiet=False)
props = {'annotators': 'coref', 'pipelineLanguage': 'en'}

text = 'Barack Obama was born in Hawaii.  He is the president. Obama was elected in 2008. His wife is Mitchell. She is nice. That is at least what people think. But they are crazy anyways.'

result = json.loads(nlp.annotate(text, properties=props))

cluster_list = list(result['corefs'].values())


print(cluster_list)

# mentions = result['corefs'].items()[0]
# for mention in mentions:
#     print(mention)
