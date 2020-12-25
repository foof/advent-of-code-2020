
with open('./data') as f:
    key1, key2 = [int(i) for i in f.read().split("\n")]
    mod = 20201227

def transform(value, subject_number):
    return value * subject_number % mod

value = 1
loop_size = 1
while (value := transform(value, 7)) != key2:
    loop_size+=1

encryption_key = pow(key1, loop_size, mod)

print(encryption_key)
