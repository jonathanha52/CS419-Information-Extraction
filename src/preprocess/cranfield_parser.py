import os
import json
import logging

path = ".\datasets\cran\cran.all.1400"
test_path = "test\data\crantest2.txt"

def join_object(title, author, publisher, text):
    content_object = {}
    if (len(title) == 0) and (len(author) == 0) and (len(publisher)) == 0 and (len(text)) == 0:
        return None
    content_object["title"] = " ".join(title)
    content_object["author"] = " ".join(author)
    content_object["publisher"] = " ".join(publisher)
    content_object["text"] = " ".join(text)
    return content_object

def cranfield_parser(path):
    parsed_content = []
    current_mode = 'title'
    text = []
    title = []
    author = []
    publisher = []
    with open(path) as f:
        content = f.readlines()
    for i, line in enumerate(content):
        if line[:2] == ".I":
            result = join_object(title, author, publisher, text)
            if result is not None:
                parsed_content.append(join_object(title, author, publisher, text))
            continue
        elif line[:2] == ".T":
            current_mode = "title"
            title.clear()
            continue
        elif line[:2] == ".A":
            current_mode = "author"
            author.clear()
            continue
        elif line[:2] == ".B":
            current_mode = "publisher"
            publisher.clear()
            continue
        elif line[:2] == ".W":
            current_mode = "text"
            text.clear()
            continue

        if current_mode == "title":
            title.append(line.strip())
        elif current_mode == "author":
            author.append(line.strip())
        elif current_mode == "publisher":
            publisher.append(line.strip())
        elif current_mode == "text":
            text.append(line.strip())
        if len(content)-1 == i:
            result = join_object(title, author, publisher, text)
            if result is not None:
                parsed_content.append(join_object(title, author, publisher, text))
    return parsed_content

def export_to_file(dicts):
    for i, dict in enumerate(dicts):
        with open(os.path.join("datasets\processed\cran" , str(i) +".json"), "w+") as f:
            json.dump(dict, f)

dicts = cranfield_parser(path)
export_to_file(dicts)