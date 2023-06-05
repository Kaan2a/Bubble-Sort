import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

sayilar = []

n = int(input("Girmek istediğiniz sayı adedini yazınız? "))

for i in range(n):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

print("Sayılar (Öncesinde):", sayilar)

start_time = time.time()

siralama = bubble_sort(sayilar)

end_time = time.time()

print("Sayılar (Sonrasında):", siralama)
print("Sıralama süresi:", end_time - start_time, "saniye")
