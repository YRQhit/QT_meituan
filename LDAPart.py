import os
import pandas as pd
import re
import jieba
import jieba.posseg as psg

class LDA():
    import os
    def chinese_word_cut(self, mytext):

        # root_dir = os.getcwd()
        #
        # dic_file = os.path.join(root_dir, r",\stopWord\dict.txt")

        dic_file = r".\stopWord\dict.txt"
        stop_file = r".\stopWord\fourStopwords.txt"
        jieba.load_userdict(dic_file)  # 加载用户词典
        jieba.initialize()  # 手动初始化（可选）

        # 加载用户停用词表
        try:
            stopword_list = open(stop_file, encoding='utf-8')
        except:
            stopword_list = []
            print("error in stop_file")

        stop_list = []  # 存储用户停用词
        flag_list = ['n', 'nz', 'vn']  # 指定在jieba.posseg分词函数中只保存n：名词、nz：其他专名、vn：动名词
        for line in stopword_list:
            line = re.sub(u'\n|\\r', '', line)
            stop_list.append(line)

        word_list = []
        seg_list = psg.cut(mytext)  # jieba.posseg分词

        # 原称之为粑粑山型的 词语过滤
        for seg_word in seg_list:
            word = re.sub(u'[^\u4e00-\u9fa5]', '', seg_word.word)  # 只匹配所有中文
            find = 0  # 标志位
            for stop_word in stop_list:
                if stop_word == word or len(word) < 2:  # 长度小于2或者在用户停用词表中，将被过滤
                    find = 1
                    break
            if find == 0 and seg_word.flag in flag_list:  # 标志位为0且是需要的词性则添加至word_list
                word_list.append(word)
        return (" ").join(word_list)
    def run(self, ID):
        if os.path.exists(".\\LDA\\result\\{}.html".format(ID)):
            print("the files have been calculated")
            pass
        else:
            data = pd.read_csv('.\comments\productId={}.csv'.format(ID))

            data["content_cutted"] = data.评论内容.apply(self.chinese_word_cut)

            from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
            from sklearn.decomposition import LatentDirichletAllocation

            # 在notebook中展示一下LDA分析结果，可去除
            def print_top_words(model, feature_names, n_top_words):
                tword = []
                for topic_idx, topic in enumerate(model.components_):
                    print("Topic #%d:" % topic_idx)
                    topic_w = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
                    tword.append(topic_w)
                    print(topic_w)
                return tword

            n_features = 1000  # 提取1000个特征词语
            tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                            max_features=n_features,
                                            stop_words='english',
                                            max_df=0.7,
                                            min_df=6)
            tf = tf_vectorizer.fit_transform(data.content_cutted)
            n_topics = 7  # 手动指定分类数
            lda = LatentDirichletAllocation(n_components=n_topics, max_iter=50,
                                            learning_method='batch',
                                            learning_offset=50,
                                            doc_topic_prior=0.1,
                                            topic_word_prior=0.01,
                                            random_state=0)
            lda.fit(tf)

            LatentDirichletAllocation(doc_topic_prior=0.1, learning_offset=50, max_iter=50,
                                      n_components=7, random_state=0,
                                      topic_word_prior=0.01)

            n_top_words = 25
            tf_feature_names = tf_vectorizer.get_feature_names_out()
            topic_word = print_top_words(lda, tf_feature_names, n_top_words)

            import numpy as np

            topics = lda.transform(tf)
            topic = []

            # output_path = r'.\LDA\result'
            # os.chdir(output_path)

            for t in topics:
                topic.append(list(t).index(np.max(t)))
            data['topic'] = topic
            data.to_excel(".\\LDA\\result\\{}.xlsx".format(ID), index=False)

            import pyLDAvis
            import pyLDAvis.sklearn
            # pyLDAvis.enable_notebook()                                  #在notebook中展示
            pic = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
            pyLDAvis.save_html(pic, '.\\LDA\\result\\' + ID + '.html')
            print("LDA已经被下载")

    def openHTML(self,ID):
        import webbrowser
        # currentPATH = os.getcwd()
        # print(currentPATH)

        output_path = r'.\LDA\result'
        # os.chdir(output_path)

        # print(os.path.join(output_path, "{}.html".format(ID)))
        file_path = os.path.join(output_path, "{}.html".format(ID))
        webbrowser.open(file_path)


if __name__ == "__main__":
    lda = LDA()
    ID = "10072795033886"
    lda.run(ID)
    lda.openHTML(ID)