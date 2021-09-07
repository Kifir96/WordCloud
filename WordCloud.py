import json
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud


url = ('https://newsapi.org/v2/everything?'
       'q=Russia&'
       'from=2021-08-01&'
       'to=2021-09-01&'
       'sortBy=popularity&'
       'apiKey=87a3c7b7f4814bae808672841baed257')


response = requests.get(url)
response_dict = response.json()
readable_file = 'data/readable_hn_data.json'


with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
with open(readable_file) as f:
    my_dict = json.load(f)


my_titles = []
my_list = my_dict['articles']
for i in my_list:
    for k, v in i.items():
        if k == 'title':
            my_titles.append(v)

top_titles = ''.join(sorted(my_titles)[:50])


wordcloud = WordCloud(width=1000,
                      height=800,
                      max_font_size=100,
                      max_words=200,
                      background_color="white").generate(top_titles)


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
