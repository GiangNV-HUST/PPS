import Lagrange1 as Lg1
import Lagrange2 as Lg2
# import Lagrange1 as Lg1

if __name__ == "__main__":
    X = []
    Y = []

    with open("input.txt", "r") as file:
        for line in file:
            data = line.strip().split(" ")
            X.append(float(data[0]))
            Y.append(float(data[1]))

    print(Lg1.TinhPn(X, X, Y))
    # TODO print(Lg2.TinhPn(X,X,Y))
    # @print(Lg1.TinhLj(X,X[0])) 