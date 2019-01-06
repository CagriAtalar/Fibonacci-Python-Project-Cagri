import matplotlib.pyplot as plt

def show_graph():
    n = 15 # How many terms shall we include?

    fiblist = [0,1]
    for i in range(n - 1):
        fiblist.append(fiblist[i] + fiblist[i+1])


    gratio = [fiblist[i]/float(fiblist[i-1]) for i in range(2,len(fiblist))]

    plt.xlabel("Fib[0]")
    plt.ylabel("Fib[1]")

    plt.plot(gratio, 'r--')
    plt.show()


if __name__ == '__main__':
    show_graph()



