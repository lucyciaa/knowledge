# 去掉txt空行

if __name__ == '__main__':
    file1 = open('../奖项/全国工会系统先进集体/2018年/2018年全国工会系统先进集体.txt', 'r', encoding='utf-8')  # 打开要去掉空行的文件
    file2 = open('../奖项/全国工会系统先进集体/2018年/2018年全国工会系统先进集体_out.txt', 'w', encoding='utf-8')  # 生成没有空行的文件

    for line in file1.readlines():
        if line == '\n':
            line = line.strip('\n')
        file2.write(line)

    file1.close()
    file2.close()