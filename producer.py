import pika
from faker import Faker
from models import Contact

fake = Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

for _ in range(10):
    contact = Contact(
        full_name=fake.name(),
        email=fake.email()
    )
    contact.save() 
    channel.basic_publish(exchange='', routing_key='email_queue', body=str(contact.id))
    print(f'Queued contact: {contact.full_name}, {contact.email}')

connection.close()