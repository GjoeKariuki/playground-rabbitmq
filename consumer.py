import pika, os


# connection string
string_url = 'amqps://rxamkjhr:IU3qfRHi52P3Lw4vi5Xx_8zrVFiUoRSR@whale.rmq.cloudamqp.com/rxamkjhr'
url = os.environ.get('CLOUDAMQP_URL', string_url)
params = pika.URLParameters(url)





connection = pika.BlockingConnection(params) #waits for all requests to complete    

channel = connection.channel() # create a channel


channel.queue_declare(queue='test_queue') # declare a queue

def callback(ch,method, properties,body):
    print(' [x] Received %r' % body)


channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
channel.close()
connection.close()