import os
import platform
import pandas as pd

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
clear_screen()

df = pd.read_excel("dataset_paper.xlsx")
df = df.dropna(subset=["Judul Paper", "Tahun Terbit", "Nama Penulis"])
df["Tahun Terbit"] = df["Tahun Terbit"].astype(int)

dataset = df[[
    "Judul Paper",
    "Tahun Terbit",
    "Nama Penulis",
    "Abstrak (langusung copas dari paper)",
    "Kesimpulan (Langusung copas dari paper)",
    "Link Paper"
]].to_dict(orient="records")

def linear_search(data, key, value):
    return [
        item for item in data
        if (value.lower() in str(item[key]).lower() if key == "Judul Paper" else item[key] == value)
    ]

def binary_search(data, key, value):
    if key == "Judul Paper":
        print("Binary search tidak mendukung pencarian sebagian judul.")
        return []

    sorted_data = sorted(data, key=lambda x: str(x[key]).lower() if isinstance(x[key], str) else x[key])
    low, high = 0, len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = str(sorted_data[mid][key]).lower() if isinstance(sorted_data[mid][key], str) else sorted_data[mid][key]

        if mid_val == value:
            return [sorted_data[mid]]
        elif mid_val < value:
            low = mid + 1
        else:
            high = mid - 1
    return []

# Menu input
print("Pilih metode pencarian: 1. Linear | 2. Binary")
metode = input("Masukkan pilihan (1/2): ")
print("Pilih kolom pencarian: 1. Judul | 2. Tahun | 3. Penulis")
kolom_input = input("Masukkan pilihan (1/2/3): ")
kolom_map = {"1": "Judul Paper", "2": "Tahun Terbit", "3": "Nama Penulis"}
key = kolom_map[kolom_input]

if key == "Tahun Terbit":
    try:
        value = int(input("Masukkan tahun (contoh: 2021): "))
    except ValueError:
        print("Input tahun tidak valid. Harus berupa angka.")
        exit()
else:
    value = input("Masukkan nilai pencarian: ")
clear_screen()

hasil = linear_search(dataset, key, value) if metode == "1" else binary_search(dataset, key, value)
if hasil:
    print("\nHasil ditemukan:")
    for item in hasil:
        print("-" * 50)
        print(f"Judul     : {item['Judul Paper']}")
        print(f"Tahun     : {item['Tahun Terbit']}")
        print(f"Penulis   : {item['Nama Penulis']}")
        print(f"Abstrak   : {item.get('Abstrak (langusung copas dari paper)', 'N/A')}")
        print(f"Kesimpulan: {item.get('Kesimpulan (Langusung copas dari paper)', 'N/A')}")
        print(f"Link      : {item.get('Link Paper', 'N/A')}")
        print("-" * 50)
else:
    print("Data tidak ditemukan.")