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
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
