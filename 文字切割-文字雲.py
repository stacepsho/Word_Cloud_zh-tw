# coding: utf-8
# 部分參考: https://ithelp.ithome.com.tw/articles/10192043 
#       非常感謝王選仲大大
# 部分參考 http://blog.fukuball.com/ru-he-shi-yong-jieba-jie-ba-zhong-wen-fen-ci-cheng-shi/
#       非禪感謝林志傑 Fukuball大大
# 字典來自 https://git.oschina.net/fxsjy/jieba
#       真的是做最好的中文分词组件
#

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import numpy as np
from collections import Counter

#要分析的來源，這個範例是五月天20首歌
text_from_file_with_apath = open(r'lyrics.txt', "r",encoding="utf-8").read()

#設定字典
jieba.set_dictionary('dict.txt.big')
#設定自訂的字典，譬如五月天的 "動次"
jieba.load_userdict(r'userdict_mayday.txt')

#設定停用詞，譬如唱歌會用到的oh，喔
with open(r'stopWord_mayday.txt', 'r', encoding='utf8') as f:  
    stops = f.read().split('\n') 

#
#開始段詞與排序，沒錯就這麼簡單就做完了
#
terms = [t for t in jieba.cut(text_from_file_with_apath, cut_all=True) if t not in stops]
sorted(Counter(terms).items(), key=lambda x:x[1], reverse=True) 


#中文繪圖需要中文字體，請自己從windows font目錄抓
#微軟正黑體
font = r'msjh.ttc'
#想要文字雲出現的圖示
mask = np.array(Image.open(r"mayday_mask.png"))

#背景顏色預設黑色，改為白色
#mark改用五月天的皇冠
#其他參數請自行參考wordcloud
my_wordcloud = WordCloud(background_color="white",mask=mask,font_path=font,collocations=False, width=2400, height=2400, margin=2)  
my_wordcloud.generate_from_frequencies(frequencies=Counter(terms))

#產生圖片
plt.figure( figsize=(20,10), facecolor='k')
plt.imshow(my_wordcloud,interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
#顯示用
plt.show()

#存檔用
#plt.savefig("Mayday_Wordcloud.png")