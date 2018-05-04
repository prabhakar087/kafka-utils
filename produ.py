import random
import time

from confluent_kafka import Producer
 
p = Producer({'bootstrap.servers': 'localhost:9092'})
for x in range(100):
  rand = random.randrange(-50,50)
#  print rand 
  p.produce('test_topic',str(rand))
  time.sleep(0.1)
p.flush(30)
