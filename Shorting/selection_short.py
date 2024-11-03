import random
def makeDist_generate(banyak_data):
    list_data = []
    for i in range(banyak_data):
        list_data.append(random.randint(1,100))
    return list_data

def selection_short(data):
    n = len(data)

    for i in range(n):
        min_idx = i #minimum index posisi ke i
        for j in range(i+1,n): #dari i+1 ke n
            if data[j]  < data [min_idx]:
                min_idx = j 

        data[i],data[min_idx] = data[min_idx],data[i]


value = int(input("Banyak data yang akan di looping : "))
list_data = makeDist_generate(value)
print("List data sebelum diurutkan: ")
print(list_data)
print("\nList data setelah diurutkan: ")
selection_short(list_data)
print(list_data)