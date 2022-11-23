



if __name__ == '__main__':
    f = open('test.txt',encoding='utf-8')
    line = f.readline()
    mydict = eval(line)
    f = open('分词.txt', 'w')
    for key in mydict:
        f.write(key)
        f.write('  :  ')
        f.write(str(mydict[key]))
        f.write('\n')
