import requests
from config import MODEL, OLLAMA_URL

def analyze_articles(articles):
    content = "\n\n".join([
        f"Title: {a['title']}\nSummary: {a['summary']}"
        for a in articles
    ])

    prompt = f"""
You are a cybersecurity expert writing blog posts for small and medium-sized businesses.

Your task:
Generate 3 separate high-quality blog post based on the trends in the articles.

Each must:
- Be separated by ---POST_SEPARATOR---
- Include full frontmatter + content

IMPORTANT:
- Output MUST be valid Markdown
- Include frontmatter EXACTLY in this format:

---
title: "..."
slug: ...
date: 2026-03-25
author: Fredrik Söderborg
description: "..."
tags:
  - cybersecurity
  - smb
published: false
lang: en
---

Then write the full blog post.

Guidelines:
- Focus on real-world risks for SMBs
- Target non-technical readers like CEOs and office managers
- Be practical, not theoretical
- Use concrete examples of real risks
- Keep tone clear and slightly urgent
- Avoid generic AI wording
- Length: 600–900 words
Articles:
{content}
"""
    return ask_llm(prompt)