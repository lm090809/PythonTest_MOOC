import random
from email.contentmanager import raw_data_manager
random.seed(2)
print(random.random())
print(random.uniform(1,5.8))
print(random.randint(-20,70))
print(random.randrange(5,100,20))
print(random.choice("hello,world"))
print(random.choice([1,2,'okk',33.33,'beijing']))
lst = [1,2,3,4,5,6]
random.shuffle(lst)
print(lst)
print(random.sample(lst,3))