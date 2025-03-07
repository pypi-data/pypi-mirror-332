import sys
import time


def progress_bar(progress, total, bar_length=30):
    percent = progress / total
    bar = '█' * int(percent * bar_length) + '-' * (bar_length - int(percent * bar_length))
    # elapsed = time.time() - start_time
    # eta = (elapsed / progress) * (total - progress) if progress else 0

    sys.stdout.write(f'\r[{bar}] {percent*100:.2f}%')  # Carriage return 
    sys.stdout.flush() 