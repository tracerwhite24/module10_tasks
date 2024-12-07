import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data

if __name__ == "__main__":
    files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

    start_time = time.time()
    for file_name in files:
        data = read_info(file_name)
    linear_execution_time = time.time() - start_time
    print(f"Линейный вывод: {linear_execution_time:.2f} секунд")

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(read_info, files)
    parallel_execution_time = time.time() - start_time
    print(f"Многопроцессный вывод: {parallel_execution_time:.2f} секунд")
