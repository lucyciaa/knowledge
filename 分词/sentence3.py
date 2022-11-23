import os
from paddlenlp import Taskflow
from collections import Counter
import time

if __name__ == '__main__':

    start_time = time.time()
    filePath = "./测试文件"  # 文件夹路径
    fileList = os.listdir(filePath)
    sentence_list = []
    for file in fileList:
        f = open(os.path.join(filePath, file),encoding='utf-8')
        while True:
            line = f.readline()
            if not line:
                break
            # 删除指定字符，strip('\n')删除换行符
            line = line.strip('\n')
            # 不传参数，默认删除换行符和空格。
            # line =line.strip()
            a_list = line.split('。')
            for a in a_list:
                sentence_list.append(a)
            # print(line)  # txt文件内容
        f.close()
    print('一共',len(fileList),'个文件, ','共分成了',len(sentence_list),'句话')
    ner = Taskflow("ner",entity_only=True,user_dict="my_dict.txt")
    s_list = ner(sentence_list)
    se_list = []
    for s in s_list:
        se_list += s
    final_list = []
    for se in se_list:
        final_list.append(se[0])
    result = Counter(final_list)
    print(result)

    end_time = time.time()  # 程序结束时间
    run_time = end_time - start_time  # 程序的运行时间，单位为秒
    print('一共运行了',run_time/60,'分钟')
