import requests
from bs4 import BeautifulSoup 

url_head = 'https://j-lyric.net'
#url = 'https://j-lyric.net/artist/a001fed/'
url = 'https://j-lyric.net/artist/a0039c4/'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)

title_links = soup.select('p.ttl > a')
print(len(title_links))

for index, t_link in enumerate(title_links):
    print(index, t_link.text) # song title
    song_link = f'{url_head}{t_link["href"]}' # song link
    song_res = requests.get(song_link) # request for song lyric
    song_res.raise_for_status()
    song_soup = BeautifulSoup(song_res.text, 'lxml')
    lyric_content = song_soup.select('#Lyric')[0]
    lyric_text = str(lyric_content).replace('<p id="Lyric">', '').replace('</p>', '').replace('<br/>', '\n') # lyric text
    f = open(f'WANDS/{t_link.text}.txt', 'w')
    f.write(t_link.text)
    f.write('\n')
    f.write('------------------------------')
    f.write('\n\n')
    f.write(lyric_text)
    f.close()

print('***** DONE *****')