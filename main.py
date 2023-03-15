# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n 
    for i in range(m):
        thread_id = threads.index(min(threads)) 
        start_time = threads[thread_id] 
        output.append((thread_id, start_time)) 
        threads[thread_id] += data[i] 
    return output



def main():
    # read input
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    
    result = parallel_processing(n, m, data)

    # print output
    for thread_id, start_time in result:
        print(thread_id, start_time)



if __name__ == "__main__":
    main()
