def test():
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    d = [11, 12, 13, 14, 15, 16]
    for i in range(0, len(c)):
        if i >= len(c):
            c = d
            i = 0
            print(c)
        else:
            print(c)


def like_cheese():
    print("That's awesome!")


while True:
    like_cheese()


if __name__ == "__main__":
    like_cheese()
