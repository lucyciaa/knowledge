from paddlenlp import Taskflow

if __name__ == '__main__':
    schema = ['姓名', '性别', '民族', '职位', '部门']
    ie = Taskflow('information_extraction', schema=schema)
    print(ie('中国铁路乌鲁木齐局集团有限公司库尔勒客运段和田一队“民族团结一家亲”号'))
