import os
from paddlenlp import Taskflow
from collections import Counter

if __name__ == '__main__':
    filePath = "./劳动理论"  # 文件夹路径
    fileList = os.listdir(filePath)
    sentence_list = []
    for file in fileList:
        f = open(os.path.join(filePath, file),encoding='utf-8')
        print(file)  # 文件名

        while True:
            line = f.readline()
            if not line:
                break
            # 删除指定字符，strip('\n')删除换行符
            line = line.strip('\n')
            # 不传参数，默认删除换行符和空格。
            # line =line.strip()
            sentence_list.append(line)
            # print(line)  # txt文件内容
        f.close()


    ner = Taskflow("ner",entity_only=True)
    s_list = ner(sentence_list)
    print(s_list)
    se_list = []
    for s in s_list:
        se_list += s
    final_list = []
    for se in se_list:
        final_list.append(se[0])
    result = Counter(final_list)
    print(result)
