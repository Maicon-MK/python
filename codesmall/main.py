def main():
    n = int(input("Whats n: "))
    for i in bee(n):
        print(i)


def bee(n):
    swarm = []
    for i in range(n):
       yield 'ZzZ'*i #
    return swarm

if __name__ == "__main__":
    main()