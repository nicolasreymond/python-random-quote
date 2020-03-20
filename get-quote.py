import random
import sys

def primary():

    if len(sys.argv)>1:
        f = open("quotes.txt", "a")
        f.write(sys.argv[1])
        f.close()
    else:
        f = open("quotes.txt")
        quotes = f.readlines()
        f.close()

        last = 15

        rnd2 = random.randint(0, last)

        for x in range(rnd2):
            print(quotes[random.randint(0, last)]),


if __name__== "__main__":
    primary()
