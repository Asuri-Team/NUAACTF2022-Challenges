from hashlib import md5
from tqdm import tqdm

aim = 1919810
sequence = [0, 1]
for i in tqdm(range(2, aim)):
    sequence.append(233 * 114514 ** i + 1919810 * sequence[i-1] + sequence[i-2])

print(len(sequence))
print(sequence[-1])
flag = md5(str(sequence[-1]).encode()).hexdigest()
flag = 'NUAACTF{' + flag + '}'
print(flag)