from mongoengine import connect
from models import Author, Quote


connect(
    db="homework_web_8",
    host="mongodb+srv://fironovayu:eK4q7lSZbSWgOSDr@cluster0.ldcyd36.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)


def search_by_author(name):
    try:
        author = Author.objects(fullname=name).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.quote.encode('utf-8').decode('utf-8'))
        else:
            print(f"No quotes found for author: {name}")
    except Exception as e:
        print(f"An error occurred: {e}")


def search_by_tag(tag):
    try:
        quotes = Quote.objects(tags=tag)
        for quote in quotes:
            print(quote.quote.encode('utf-8').decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")  


def search_by_tags(tags):
    try:
        tags_list = tags.split(',')
        quotes = Quote.objects(tags__in=tags_list)
        for quote in quotes:
            print(quote.quote.encode('utf-8').decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        try:
            command = input("Enter command: ")
            if command.startswith("name:"):
                name = command[len("name:"):].strip()
                search_by_author(name)
            elif command.startswith("tag:"):
                tag = command[len("tag:"):].strip()
                search_by_tag(tag)
            elif command.startswith("tags:"):
                tags = command[len("tags:"):].strip()
                search_by_tags(tags)
            elif command == "exit":
                break
            else:
                print("Invalid command")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
