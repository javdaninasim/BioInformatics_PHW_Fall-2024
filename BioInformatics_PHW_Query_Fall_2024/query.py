from collections import defaultdict

num, size = map(int, input().split())

count_dict = defaultdict(int)
for _ in range(num):
    seq = input().strip()
    count_dict[seq] += 1

queries = int(input())
results = []

for _ in range(queries):
    pattern = input().strip()
    length = len(pattern)
    
    if length < size:
        results.append(-1)
        continue
    
    needed = defaultdict(int)
    for i in range(length - size + 1):
        part = pattern[i:i+size]
        needed[part] += 1
    
    min_times = float('inf')
    for part in needed:
        if part not in count_dict:
            min_times = 0
            break
        possible = count_dict[part] // needed[part]
        if possible < min_times:
            min_times = possible
    
    if min_times == float('inf'):
        results.append(-1)
    else:
        results.append(min_times)
        
for res in results:
    print(res)
