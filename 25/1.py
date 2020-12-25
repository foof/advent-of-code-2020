
with open('./data') as f:
    keys = f.read().split("\n")
    card_public_key = int(keys[0])
    door_public_key = int(keys[1])

def transform(value, subject_number):
    value *= subject_number
    value %= 20201227
    return value

value = 1
door_loop_size = 0
while value != door_public_key:
    value = transform(value, 7)
    door_loop_size+=1
print('door_loop_size', door_loop_size)

encryption_key = 1
for _ in range(door_loop_size):
    encryption_key = transform(encryption_key, card_public_key)

print(encryption_key)
