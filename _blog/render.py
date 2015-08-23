#!/usr/bin/python3

import hoep
import jinja2
import os
import datetime
import dateutil.parser


def parse_article(articlefile):
    with open(articlefile, "r") as f:
        article = f.read()

    in_meta = False
    lines = article.splitlines()

    title, date = None, None
    for i, line in enumerate(lines):
        if line == "---":
            if in_meta:
                break
            in_meta = True
        elif in_meta:
            if line.startswith("title:"):
                title = line.replace("title:", "").strip()
            elif line.startswith("date:"):
                date = line.replace("date:", "").strip()
                date = dateutil.parser.parse(date)
            else:
                raise AssertionError("Unknown meta field '%s'" % line)

    if not title:
        raise ValueError("title is missing in article %s" % articlefile)
    if not date:
        raise ValueError("date is missing in article %s" % articlefile)

    i += 1
    while not lines[i].strip():
        i += 1


    body = "\n".join(lines[i:])
    html = hoep.render(body, 0, 0)

    return {
        "title": title,
        "date": date,
        "body": html,
    }




if __name__ == "__main__":
    with open("base.html", "r") as f:
        template = jinja2.Template(f.read())

    print("creating blog page")

    articles = []
    articles_path = "../_articles"
    for article in os.listdir(articles_path):
        if article.endswith(".md"):
            article = parse_article(os.path.join(articles_path, article))
            articles.append(article)
            print("included article \t'%s'" % article["title"])

    page = template.render(articles=articles)
    with open("../index.html", "w") as out:
        out.write(page)

