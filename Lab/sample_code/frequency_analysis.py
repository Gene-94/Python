import pprint
message = "To laugh often and much \
to win the respect of intelligent people and the affection of children \
to earn the appreciation of honest criticism \
and endure the betrayal of false friends \
to appreciate beauty and find the best in others \
to leave this world a bit better whether by a healthy child, \
a garden patch, a redeemed social condition \
to know even one life has breathed easier because you have lived \
this is to have succeeded."
count = {}

for char in message.upper():
    count.setdefault(char, 0)
    count[char] = count[char] + 1

print(count)

for key, value in count.items():
    print(key,":",value)

pprint.pprint(count)

total = 0
for item in count.values():
    total += item

for item in count:
    count[item] = 100*count[item]/total


for key, value in count.items():
    print(key,":",str(round(value*100)/100)+"%")
    
total = 0
for item in count.values():
    total += item
print("total:",total)