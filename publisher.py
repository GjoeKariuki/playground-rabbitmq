# publishing messages
import os, pika


# connection string
string_url = 'amqps://rxamkjhr:IU3qfRHi52P3Lw4vi5Xx_8zrVFiUoRSR@whale.rmq.cloudamqp.com/rxamkjhr'
url = os.environ.get('CLOUDAMQP_URL', string_url)


params = pika.URLParameters(url)

connection = pika.BlockingConnection(params) #waits for all requests to complete    

channel = connection.channel() # create a channel

channel.exchange_declare('test_exchange') # declare an exchange

channel.queue_declare(queue='test_queue') # declare a queue


# queue bound to exchange with key test_queue
channel.queue_bind('test_queue', 'test_exchange', 'tests')
channel.basic_publish(exchange='test_exchange',
    routing_key='tests',
    body='Hello World!')

print(" [x] Sent 'Hello World!'")
channel.close()
connection.close()