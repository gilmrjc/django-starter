import multiprocessing

bind = ":8000"
workers = multiprocessing.cpu_count() + 1
threads = multiprocessing.cpu_count()
