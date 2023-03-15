import heapq

def parallel_processing(n, m, data):
    output = []
    # Create a priority queue and populate it with the first n jobs
    queue = [(0, i) for i in range(n)]
    heapq.heapify(queue)
    # Iterate through the remaining jobs
    for i in range(n, m):
        # Get the next available thread and the time it will finish its current job
        time, thread = heapq.heappop(queue)
        # Append the thread and the job index to the output
        output.append((thread, time))
        # Update the finish time of the thread with the new job
        finish_time = time + data[i]
        # Add the thread and its new finish time to the priority queue
        heapq.heappush(queue, (finish_time, thread))
    # Process the remaining jobs
    while queue:
        time, thread = heapq.heappop(queue)
        # Append the thread and the job index to the output
        output.append((thread, time))
    # Sort the output by the job index
    output.sort(key=lambda x: x[0])
    # Format the output as a string
    output_str = "\n".join([f"{t[0]} {t[1]}" for t in output])
    return output_str

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    print(result)

if __name__ == "__main__":
    main()
