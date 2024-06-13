import json
from mongoengine import connect
from models import Author, Quote


connect(
    db="homework_web_8",
    host="mongodb+srv://fironovayu:eK4q7lSZbSWgOSDr@cluster0.ldcyd36.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)


with open('authors.json', 'r', encoding='utf-8') as f:
    authors_data = json.load(f)


with open('quotes.json', 'r', encoding='utf-8') as f:
    quotes_data = json.load(f)


author_objs = {}
for author in authors_data:
    author_obj = Author(  
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )
    author_obj.save()
    author_objs[author['fullname']] = author_obj


for quote in quotes_data:
    quote_obj = Quote(
        tags=quote['tags'],
        author=author_objs[quote['author']],
        quote=quote['quote']
    )
    quote_obj.save()
