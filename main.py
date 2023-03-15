# python3

def parallel_processing(n, m, data):
    output = []
    start_time = 0
    for i in range(0, m, n):
        for j in range(n):
            if i + j < m:
                output.append((j, start_time))
        start_time += 1
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
