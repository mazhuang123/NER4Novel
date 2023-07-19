from LAC import LAC
def lac_username(sentences: str) -> list:
    # 装载LAC模型
    user_name_list = []
    lac = LAC(mode="lac")
    lac_result = lac.run(sentences)
    for index, lac_label in enumerate(lac_result[1]):
        if lac_label == "PER":
            user_name_list.append(lac_result[0][index])
    return user_name_list


if __name__ == '__main__':
    # f = open("E:\\work\\python_project_list\\NER4Novel\\book\\天价毫宠_完全版.txt")
    # text = f.read()
    # f.close()

    text = "周树人（1881年9月25日－1936年10月19日），原名周樟寿，字豫山、豫亭，后改字豫才，以笔名鲁迅聞名於世，浙江紹興人"
    lac_user = lac_username(text)
    print("NLP_List:", lac_user)