
with open('./data') as f:
    keys = f.read().split("\n")
    card_public_key = int(keys[0])
    door_public_key = int(keys[1])
    mod = 20201227

def transform(value, subject_number):
    return value * subject_number % mod

value = 1
door_loop_size = 1
while (value := transform(value, 7)) != door_public_key:
    door_loop_size+=1

encryption_key = pow(card_public_key, door_loop_size, mod)

print(encryption_key)
