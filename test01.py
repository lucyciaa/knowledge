from collections import Counter
import jieba

if __name__ == '__main__':
    strs = ["我来到北京清华大学", "乒乓球拍卖完了", "中国科学技术大学开学了"]
    for str in strs:
        seg_list = jieba.cut(str, cut_all=True)
        print("Full Mode: " + "/ ".join(seg_list))  # 全模式
