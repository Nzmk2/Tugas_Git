data_panen ={
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen':{
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen':{
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen':{
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen':{
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen':{
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}


print("Berikut merupakan seluruh data panen")
for i in data_panen.items():
    print(i)


print("="*60)
print(":"*60)
print("/"*60)

print(f"Jumlah hasil panen jagung dari lokasi 2 atau {data_panen['lokasi2']['nama_lokasi']}")
print(f"Jumlahnya adalah {data_panen['lokasi2']['hasil_panen']['jagung']} ")


print("="*60)
print(f"Nama lokasi dari lokasi 3 adalah {data_panen['lokasi3']['nama_lokasi']}")

print("="*60)

print(":"*60)

print("/"*60)
print(f"Nama lokasi dari lokasi 3 adalah {data_panen['lokasi3']['nama_lokasi']}")

print("/"*60)
for j, y in data_panen.items():
    nama_lok = y['nama_lokasi']
    padi = y['hasil_panen']['padi']
    jagung = y['hasil_panen']['jagung']

    print(f"Nama lokasi: {nama_lok}\n"
          f"Jumlah panen padi {padi}\n"
          f"Jumlah panen jagung {jagung}")
    
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {nama_lok} memerlukan perhatian khusus\n")
    else:
        print(f"Lokasi {nama_lok} dalam kondisi baik\n")