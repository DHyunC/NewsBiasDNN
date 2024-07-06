import requests
import io
from inscriptis import get_text
from bs4 import BeautifulSoup

# abc articles
abc = ["https://www.abc.net.au/news/2024-07-06/uk-election-result-leaves-uk-conservative-party-in-tatters/104033260",
"https://www.abc.net.au/news/2024-07-06/fatima-payman-labor-departing-reflects-divisions-gaza/104064894",
"https://www.abc.net.au/news/2024-07-06/dulcie-flower-recognised-naidoc-lifetime-achievement-award/104052414",
"https://www.abc.net.au/news/2024-07-06/joe-biden-rejects-polling-numbers-and-refuses-to-drop-out/104067250",
"https://www.abc.net.au/news/2024-07-06/nsw-police-stateline-sexual-assault-saro-convictions/104064490"]

#fox articles
fox = ["https://www.foxnews.com/us/biden-initiates-debate-damage-control-with-strategic-white-house-meeting-more-top-headlines",
"https://www.foxnews.com/politics/biden-faces-most-consequential-weekend-his-presidential-rematch-trump",
"https://www.foxnews.com/politics/fetterman-emerges-fierce-biden-defender-comparing-post-stroke-debate-biden-blunder",
"https://www.foxnews.com/politics/missouri-ag-sues-new-york-over-reprehensible-lawfare-against-trump-poisonous-american-democracy",
"https://www.foxnews.com/politics/capitol-police-investigating-pro-israel-house-democrat-office-vandalized"]

for url in abc:
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    header = soup.find('h1').text
    paragraphs = soup.find_all('p')

    with io.open('train_data/abc_article' + str(abc.index(url)+1) + '.txt', 'w', encoding='utf8') as f_out:
        f_out.write(header + '\n')

        for paragraph in paragraphs:
            paragraph = paragraph.text
            f_out.write(paragraph + '\n')
        
        f_out.close()

for url in fox:
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    header = soup.find('h1').text
    paragraphs = soup.find_all('p')

    with io.open('train_data/fox_article' + str(fox.index(url)+1) + '.txt', 'w', encoding='utf8') as f_out:
        f_out.write(header + '\n')

        for paragraph in paragraphs:
            paragraph = paragraph.text
            f_out.write(paragraph + '\n')
        
        f_out.close()
