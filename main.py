# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n # initialize each thread to start at time 0
    for i in range(m):
        thread_id = threads.index(min(threads)) # find the next available thread
        start_time = threads[thread_id] # the start time for the task is the current time for the thread
        output.append((thread_id, start_time)) # add the output pair to the list
        threads[thread_id] += data[i] # update the current time for the thread based on the processing time for the task
    return output



def main():
    # read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # simulate parallel processing
    result = parallel_processing(n, m, data)

    # print output pairs
    for thread_id, start_time in result:
        print(thread_id, start_time)



if __name__ == "__main__":
    main()
