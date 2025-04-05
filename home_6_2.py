import time

result = time.localtime(224930)

print(f'{result.tm_mday} дні, {result.tm_hour}:{result.tm_min}:{result.tm_sec}')