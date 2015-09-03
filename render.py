#!/usr/bin/python3

import hoep
import jinja2
import jinja2.filters
import os
import datetime
import dateutil.parser


def date_cesky(date):
    month = [
        "ledna", "února", "března", "dubna", "května", "června", "července",
        "srpna", "září", "října", "listopadu", "prosince"
    ][date.month - 1]
    return "{}. {} {}".format(date.day, month, date.year)

def parse_article(articlename, articlefile):
    with open(articlefile, "r") as f:
        article = f.read()

    in_meta = False
    lines = article.splitlines()

    title, date, location = None, None, None
    for i, line in enumerate(lines):
        if line == "---":
            if in_meta:
                break
            in_meta = True
        elif in_meta:
            if line.startswith("title:"):
                title = line.replace("title:", "").strip()
            elif line.startswith("location:"):
                location = line.replace("location:", "").strip()
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
        "name": articlename,
        "title": title,
        "date": date,
        "body": html,
        "location": location,
    }



if __name__ == "__main__":
    jinja2.filters.FILTERS["date_cesky"] = date_cesky
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("_layouts"))

    print("creating blog page")

    articles = []
    articles_path = "_articles"
    for article in os.listdir(articles_path):
        if article.endswith(".md"):
            name = article.rstrip(".md")
            article = parse_article(name, os.path.join(articles_path, article))
            articles.append(article)
            print("included article \t'%s'" % article["title"])

    article_template = env.get_template("article.html")
    for article in articles:
        page = article_template.render(article=article)
        with open(os.path.join("a", article["name"] + ".html"), "w") as out:
            out.write(page)

    index_template = env.get_template("index.html")
    page = index_template.render(articles=articles)
    with open("index.html", "w") as out:
        out.write(page)

