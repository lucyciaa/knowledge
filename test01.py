from paddlenlp import Taskflow

if __name__ == '__main__':
    schema = ['姓名', '部门', '职位']
    ie = Taskflow('information_extraction', schema=schema)
    print(ie('陈爱玲(女) 中铁五局集团路桥工程有限责任公司贵州双龙港水环境综合整治项目部党工委书记、经理'))
