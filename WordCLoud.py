import jieba
import wordcloud

f = open("SmallRedBook.txt", "r", encoding="utf-8")
t = f.read()
f.close()

excludes = {"我", "是", "的", "都", "就", "了", "也", "很", "啊", "在", "就是"}
ls = jieba.lcut(t)
ls = [word for word in ls if word not in excludes]

txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white")
w.generate(txt)
w.to_file("red_book.png")
