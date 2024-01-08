import time

# начальное время
start_time = time.time()

def calc(n):
    return n + n

# calc = lambda n: n + n

# код, время выполнения которого нужно измерить
for i in range(100000):
    calc(i)

# конечное время
end_time = time.time()

# разница между конечным и начальным временем
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)