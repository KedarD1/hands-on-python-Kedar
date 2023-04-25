NAMES = ["John", "Paul", "George", "Kedar"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1
print("--------------------------------")
for name in NAMES:
    print(name)
print("--------------------------------")

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")
print("--------------------------------")

for name in reversed(NAMES):
    print(name)
print("--------------------------------")

for i in range(5):
    print(i)
print("--------------------------------")

# enumerate
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
