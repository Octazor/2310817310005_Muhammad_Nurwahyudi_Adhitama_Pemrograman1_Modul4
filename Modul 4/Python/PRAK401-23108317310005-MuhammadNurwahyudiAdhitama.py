kelipatan, simbol = input(" ").split()

kelipatan = int(kelipatan)

for bilangan in range(1, 51):
    if bilangan % kelipatan == 0:
        print(simbol, end=" ")
    else:
        print(bilangan, end=" ")

