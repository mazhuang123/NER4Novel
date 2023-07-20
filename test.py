from pyhanlp import *


# 加载停用词词典
def load_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        contents = f.readlines()
    result = []
    for content in contents:
        result.append(content.strip())

    return result

def hanlp_username(sentences: str) -> list:
    from pyhanlp import HanLP
    segment = HanLP.newSegment().enableNameRecognize(True)
    seg_words = segment.seg(sentences)
    user_list = []
    for value in seg_words:
        split_words = str(value).split('/')  # check //m
        word, tag = split_words[0], split_words[-1]
        if tag == 'nr':
            user_list.append(word)
    return user_list

# 去停用词
def remove_stop_words(text, dic):
    result = []
    for k in text:
        if k.word not in dic:
            result.append(k.word)
    return result

if __name__ == '__main__':
    HanLP.Config.ShowTermNature = False
    segment = DoubleArrayTrieSegment()
    segment.enablePartOfSpeechTagging(True)
    with open("/book/天价豪宠前6章.txt") as f:
        text = f.read()
    # text = segment.seg('江西鄱阳湖干枯了，中国最大的淡水湖变成了大草原')
    # print(text)
    temp = segment.seg(text)
    dic = load_file('HanNlp/stopwords.txt')
    result = remove_stop_words(temp, dic)
    print(result)
