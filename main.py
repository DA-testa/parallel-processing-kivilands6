# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    # create threads
    
    t=[]

    for i in range(n):
        t.append(0)

    time = 0;

    while data:

        for i in range(n):
            if t[i] == 0:
                output.append((i, time))
                t[i] = data[0] - 1
                data.pop(0)
            else:
                t[i] = t[i] - 1

        time = time + 1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    variables = list(map(int, input().split()))
    # n - thread count 
    n = variables[0]
    # m - job count
    m = variables[0]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i,j in result:
        print(i,j)



if __name__ == "__main__":
    main()
