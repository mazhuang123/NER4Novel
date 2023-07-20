
from litie.pipelines import RelationExtractionPipeline
from transformers import pipeline

from NLP_List.create_graph import createRelationGraph

if __name__ == '__main__':
    # p = pipeline('fill-mask', 'IDEA-CCNL/Erlangshen-BERT-120M-IE-Chinese')
    # # p = pipeline('named-entity-recognition', 'damo/nlp_maoe_named-entity-recognition_chinese-base-general')
    # p = pipeline('relation-extraction', 'damo/nlp_bert_relation-extraction_chinese-base')
    p = RelationExtractionPipeline("gplinker", model_name_or_path="xusenlin/duie-gplinker", model_type="bert")
    # p = pipeline(Tasks.named_entity_recognition, 'damo/nlp_raner_named-entity-recognition_chinese-base-book')
    result = p('张三是张四的爸爸,关羽是刘备的弟弟')
    # dict_list = list(dict(result))
    print(result)


    # temp_dict = dict(result[0])
    # first_key = list(temp_dict.keys())[0]
    # first_value = temp_dict[first_key]
    # parent_result= list(first_value)[0]['object']
    # child_result = list(first_value)[0]['subject']
    # relation_result = list(temp_dict.keys())[0]
    # print(parent_result,child_result,relation_result)
    # createRelationGraph(parent_result,child_result,relation_result)
