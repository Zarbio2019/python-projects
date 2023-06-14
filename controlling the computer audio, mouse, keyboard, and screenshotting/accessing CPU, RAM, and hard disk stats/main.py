import psutil

# CPU
# accessing processor statistics (CPU)
print(psutil.cpu_count()) # get number of cores
print(psutil.cpu_count(logical=False)) # get number of physical cores

print(psutil.cpu_percent(interval=1)) # get current percentage your CPU is being used on your computer

print(psutil.cpu_times()) # get seconds that the CPU has spent in given mode
print(psutil.cpu_times().system)

print(psutil.cpu_stats())
print(psutil.cpu_freq())

# RAM
print(psutil.virtual_memory())
print(psutil.swap_memory())

# Hard Disk
print(psutil.disk_usage('/'))
print(psutil.disk_usage('/').percent)

# https://psutil.readthedocs.io/en/latest
