x, y = map(int, input("").split())

hasil = 0

for i in range(1, x + 1):
    total = 0
    for j in range(i, 0, -1):
        perkalian_kelipatan = j * y
        print(f"({j} * {y})", end="")
        total += perkalian_kelipatan
        if j > 1:
            print(" + ", end="")
    
    print(f" = {total}")
    hasil += total

print(hasil)
