import pandas
import string
import random

data = list(list(''.join(list(random.choice(string.ascii_letters) for _ in range(5))) for _ in range(5)) for _ in range(5))
print(data)
print(pandas.DataFrame(data))
