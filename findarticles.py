from newsapi.articles import Articles
from newsapi.sources import Sources

def listOfSources():
    s = Sources(API_KEY="40e40820d389493abb369f099605fec3")
    a = s.all()

    sourceList = []
    for source in a['sources']:
        sourceList.append(source['id'])

    return sourceList

def listOfArticles():
    sourceList = listOfSources()
    articleList = []

    a = Articles(API_KEY="40e40820d389493abb369f099605fec3")

    for source in sourceList:
        try:
            b = a.get_by_latest(source=source)
            articleList.extend(b['articles'])
        except:
            pass
    return articleList

def findArticles(country):
    articleList = listOfArticles()
    articles = []
    articlecount = 0
    for article in articleList:
        if country in article['title']:
            articles.append([article['title'], article['url']])
            articlecount += 1
    # returns a tuple
    # 1st is a list of title, url
    # second is article count
    return(articles, articlecount)