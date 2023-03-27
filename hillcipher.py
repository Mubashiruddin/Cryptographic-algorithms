import numpy as np

p = input("Enter plain text : ")

k = [int(i) for i in input("Enter key:").split(' ')]

ch = input("1. Encrypt\n2. Decrypt\nEnter your choice : ")


print("encrypt")
diagrams = [[ord(p[i]) - 65, ord(p[i+1]) - 65] if p[i].isupper() else [ord(p[i]) - 97, ord(p[i+1]) - 97] for i in range(0, len(p)-1, 2)]
letters = []
k = np.array(k).reshape([2, 2])


if ch == '2':
    print("decrypt")
    k = (((np.linalg.det(k) * np.linalg.inv(k)) %26) * (pow(int(np.linalg.det(k)), -1, 26)) % 26)

for i in diagrams:
    ha = np.array(i).reshape([2, 1])
    res = (np.dot(k, ha) % 26).reshape([2])
    letters += [x for x in res.tolist()]


print(''.join([chr(int(letters[i]) + 65) if p[i].isupper()
          else chr(int(letters[i]) + 97) for i in range(len(letters))]))