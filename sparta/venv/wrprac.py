from wordcloud import WordCloud

text = ''
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        text += line
print(text)


wc = WordCloud(font_path='C:/WINDOWS/Fonts/NanumBarunGothic.ttf', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")
