import re

p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
p2 = re.compile('^[a-zA-Z0-9][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
emails = ['python@mail.example.com', 'python+kr@example.com',  # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',  # 올바른 형식
          'python.dojang@e-xample.com',  # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']  # 잘못된 형식

for email in emails:
    print(p.match(email) is not None, end=' ')

print()

for email in emails:
    print(p2.match(email) is not None, end=" ")
