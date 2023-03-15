# python3

def parallel_processing(n, m, data):
    output = []
    start_times = [0] * n  # initialize start times for each thread to 0
    for i in range(m):
        # find the earliest available thread
        thread_index = start_times.index(min(start_times))
        start_time = start_times[thread_index]
        processing_time = data[i]
        output.append((thread_index, start_time))
        start_times[thread_index] += processing_time
    return output

def main():
    # read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # get the results
    result = parallel_processing(n, m, data)

    # print out the results
    for thread_index, start_time in result:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()
