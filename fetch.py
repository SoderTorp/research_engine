import feedparser
from config import FEEDS

def fetch_articles():
    articles = []

    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:5]:
            articles.append({
                "title": entry.title,
                "summary": entry.summary,
                "link": entry.link,
                "source": feed_url
            })

    return articles