def fcfs_scheduling(processes):
    n = len(processes)
    wait_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        wait_time[i] = processes[i-1][1] + wait_time[i-1]

    for i in range(n):
        turnaround_time[i] = processes[i][1] + wait_time[i]

    total_waiting_time = sum(wait_time)
    total_turnaround_time = sum(turnaround_time)

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{wait_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nTotal Waiting Time: {total_waiting_time}")
    print(f"Average Waiting Time: {average_waiting_time:.2f}")
    print(f"Total Turnaround Time: {total_turnaround_time}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

num_processes = int(input("Enter the number of processes: "))

processes = []
for i in range(num_processes):
    process_name = input(f"Enter the name of process {i+1}: ")
    burst_time = int(input(f"Enter the burst time for process {process_name}: "))
    processes.append((process_name, burst_time))

fcfs_scheduling(processes)
