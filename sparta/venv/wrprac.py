from wordcloud import WordCloud
from PIL import Image
import numpy as np
text = ''
with open("1020talk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[2:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ','').replace('ㅎ','').replace('ㅠ','').replace('ㅜ','').replace('이모티콘\n','').replace('사진\n','').replace('저는','').replace('저도','')


print(text)


wc = WordCloud(font_path='C:/WINDOWS/Fonts/HOONSAEMAULUNDONGR.ttf', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")



mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/WINDOWS/Fonts/HOONSAEMAULUNDONGR.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked2.png")
