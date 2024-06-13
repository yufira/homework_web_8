from mongoengine import Document, StringField, ListField, ReferenceField, BooleanField, connect

connect(
    db="homework_web_8",
    host="mongodb+srv://fironovayu:eK4q7lSZbSWgOSDr@cluster0.ldcyd36.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)


class Author(Document):
    fullname = StringField(max_length=50, required=True)
    born_date = StringField(max_length=50, required=True)
    born_location = StringField(max_length=50, required=True)
    description = StringField(required=True)


class Quote(Document):
    tags = ListField(StringField(max_length=120, required=True))
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)


class Contact(Document):
    full_name = StringField(max_length=100, required=True)
    email = StringField(max_length=100, required=True)
    message_sent = BooleanField(default=False)