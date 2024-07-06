import urllib.request
from inscriptis import get_text

# abc articles
abc = ["https://www.abc.net.au/news/2024-07-06/uk-election-result-leaves-uk-conservative-party-in-tatters/104033260",
"https://www.abc.net.au/news/2024-07-06/fatima-payman-labor-departing-reflects-divisions-gaza/104064894",
"https://www.abc.net.au/news/2024-07-06/dulcie-flower-recognised-naidoc-lifetime-achievement-award/104052414",
"https://www.abc.net.au/news/2024-07-06/joe-biden-rejects-polling-numbers-and-refuses-to-drop-out/104067250",
"https://www.abc.net.au/news/2024-07-06/nsw-police-stateline-sexual-assault-saro-convictions/104064490"]

#fox articles
fox = [
"https://www.foxnews.com/live-news/biden-campaign-drop-out-july-5",
"https://www.foxnews.com/politics/biden-faces-most-consequential-weekend-his-presidential-rematch-trump",
"https://www.foxnews.com/politics/fetterman-emerges-fierce-biden-defender-comparing-post-stroke-debate-biden-blunder",
"https://www.foxnews.com/politics/missouri-ag-sues-new-york-over-reprehensible-lawfare-against-trump-poisonous-american-democracy",
"https://www.foxnews.com/us/biden-initiates-debate-damage-control-with-strategic-white-house-meeting-more-top-headlines"
]

for article in abc:
    html = urllib.request.urlopen(article).read().decode('utf-8')
    text = get_text(html)
    print("NEW ARTICLE")
    #print(text)
    with open('abc_article' + str(abc.index(article)+1) + '.txt', 'x') as f:
        f.write(text)

for article in fox:
    html = urllib.request.urlopen(article).read().decode('utf-8')
    text = get_text(html)
    print("NEW ARTICLE")
    #print(text)
    with open('fox_article' + str(abc.index(article)+1) + '.txt', 'x') as f:
        f.write(text)
