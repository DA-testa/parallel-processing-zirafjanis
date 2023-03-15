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


# Test
input_data = "2 5\n1 2 3 4 5"
expected_output = "0 0\n1 0\n0 1\n1 2\n0 4"
assert parallel_processing(*map(str.strip, input_data.split('\n'))) == expected_output
