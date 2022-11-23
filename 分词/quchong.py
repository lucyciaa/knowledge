

if __name__ == '__main__':
        f_read = open(r'./user_dict.txt', 'r', encoding='utf-8')  # 将需要去除重复值的txt文本重命名text.txt
        f_write = open(r'./my_dict.txt', 'w', encoding='utf-8')  # 去除重复值之后，生成新的txt文本 --“去除重复值后的文本.txt”
        data = set()
        for a in [a.strip('\n') for a in list(f_read)]:
            if a not in data:
                f_write.write(a + '\n')
                data.add(a)
        f_read.close()
        f_write.close()

