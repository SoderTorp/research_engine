from fetch import fetch_articles
from analyze import analyze_articles
from db import save_topic_ideas
from datetime import datetime
import os
import re

def extract_title(markdown):
    match = re.search(r'title:\s*"(.*?)"', markdown)
    return match.group(1) if match else "untitled"

def slugify(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

def save_multiple_markdowns(content):
    posts = content.split("---POST_SEPARATOR---")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    os.makedirs("../outputs", exist_ok=True)

    for i, post in enumerate(posts):
        post = post.strip()

        title = extract_title(post)
        slug = slugify(title)

        filename = f"../outputs/{today}_{slug}.md"

        with open(filename, "w") as f:
            f.write(post)

        print(f"Saved: {filename}")

def main():
    articles = fetch_articles()
    ideas = analyze_articles(articles)

    print("\n=== BLOG IDEAS ===\n")
    print(ideas)

    save_multiple_markdowns(ideas)

if __name__ == "__main__":
    main()