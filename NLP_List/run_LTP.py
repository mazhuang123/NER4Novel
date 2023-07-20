from ltp import LTP
from transformers import pipeline


def ltp_username(sentences: str) -> list:
    ltp = LTP()  # 默认加载 Small 模型，下载的路径是：~/.cache/torch/ltp
    result = ltp.pipeline([sentences], tasks=["cws", "ner"])
    # seg, hidden = ltp.seg([sentences])  # 分词
    # nh_user_list = []
    # pos_index_values = ltp.pos(hidden)
    # # seg 是 list to list 的格式
    # for index, seg_i in enumerate(seg):
    #     pos_values = pos_index_values[index]
    #     for _index, _pos in enumerate(pos_values):
    #         if _pos == "nh":
    #             nh_user_list.append(seg_i[_index])
    return result['ner']

if __name__ == '__main__':
    # f = open("E:\\work\\python_project_list\\NER4Novel\\book\\test.txt")
    # text = f.read()
    # f.close()
    # text = "刘玉双的房子在市中心的一个高档小区内，乔锦按响门铃，一个精神矍铄、头发银白的优雅老太太开了门。"
    # ltp_user = ltp_username(text)
    # print("LTP:", ltp_user)

    p = pipeline('named-entity-recognition', 'damo/nlp_raner_named-entity-recognition_chinese-base-book')
    p('风族最强大的存在，风帝，为当世顶尖强者之一。',)
    print(p)






























