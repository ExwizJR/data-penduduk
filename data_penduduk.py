#LOUIS MAHARDHIKA 5230411139
#(kode 1=PNS, 2=TNI/POLRI, 3=Pedagang, 4=Petani, 5=Nelayan, 6=Buruh) 
#(kode 1=Islam, 2=Prostestan, 3=Katholik, 4=Hindu, 5=Budha, 6=Konghucu)
#(kode L=Laki-laki, P=Perempuan)

import os

data = {
    "1": {
        "nik": "12331",
        "nama": "Adi",
        "jenis_kelamin": "L",
        "agama": 1,
        "status": "belum kawin",
        "pekerjaan": 4,
    },
    "2": {
        "nik": "12332",
        "nama": "Leo",
        "jenis_kelamin": "L",
        "agama": 2,
        "status": "kawin",
        "pekerjaan": 2,
    },
    "3": {
        "nik": "12333",
        "nama": "Rusdi",
        "jenis_kelamin": "L",
        "agama": 1,
        "status": "kawin",
        "pekerjaan": 4,
    },
    "4": {
        "nik": "12334",
        "nama": "Fuad",
        "jenis_kelamin": "L",
        "agama": 1,
        "status": "kawin",
        "pekerjaan": 6,
    },
    "5": {
        "nik": "12335",
        "nama": "Fira",
        "jenis_kelamin": "P",
        "agama": 1,
        "status": "kawin",
        "pekerjaan": 5,
    },
    "6": {
        "nik": "12336",
        "nama": "Faiz",
        "jenis_kelamin": "L",
        "agama": 1,
        "status": "kawin",
        "pekerjaan": 1,
    },
    "7": {
        "nik": "12337",
        "nama": "Slamet",
        "jenis_kelamin": "L",
        "agama": 1,
        "status": "belum kawin",
        "pekerjaan": 1,
    },
    "8": {
        "nik": "12338",
        "nama": "Novi",
        "jenis_kelamin": "P",
        "agama": 2,
        "status": "belum kawin",
        "pekerjaan": 1,
    },
    "9": {
        "nik": "12339",
        "nama": "Angga",
        "jenis_kelamin": "L",
        "agama": 1,
        "status": "belum kawin",
        "pekerjaan": 3,
    },
    "10": {
        "nik": "12340",
        "nama": "Argian",
        "jenis_kelamin": "L",
        "agama": 1,
        "status": "kawin",
        "pekerjaan": 5,
    },
    "11": {
        "nik": "12341",
        "nama": "Okta",
        "jenis_kelamin": "P",
        "agama": 5,
        "status": "kawin",
        "pekerjaan": 3,
    },
    "12": {
        "nik": "12342",
        "nama": "Ahmad",
        "jenis_kelamin": "L",
        "agama": 1,
        "status": "kawin",
        "pekerjaan": 6,
    },
    "13": {
        "nik": "12343",
        "nama": "Sylvi",
        "jenis_kelamin": "P",
        "agama": 3,
        "status": "kawin",
        "pekerjaan": 1,
    },
    "14": {
        "nik": "12344",
        "nama": "Rofi",
        "jenis_kelamin": "L",
        "agama": 1,
        "status": "kawin",
        "pekerjaan": 2,
    },
    "15": {
        "nik": "12345",
        "nama": "Ayu",
        "jenis_kelamin": "P",
        "agama": 4,
        "status": "belum kawin",
        "pekerjaan": 1,
    },
}

def menu_awal():
    clear_screen()
    print("="*32, "DATA KEPENDUDUKAN", "="*32)
    print("|| 1. Tampilkan jumlah penduduk perempuan yang belum kawin                       ||")
    print("|| 2. Tampilkan jumlah penduduk perempuan yang tidak beragama Islam              ||")
    print("|| 3. Tampilkan jumlah penduduk laki-laki yang perkerjaannya PNS                 ||")
    print("|| 4. Tampilkan jumlah penduduk laki-laki yang perkerjaannya petani atau nelayan ||")
    print("|| 5. Keluar                                                                     ||")
    print("="*83)

def penduduk_perempuan_yang_belum_kawin():
    counter = 0
    for item in data.values():
        if item.get("jenis_kelamin") == "P" and item.get("status") == "belum kawin":
            counter += 1
            print("||","="*67)
            print("|| NIK :", item['nik'])
            print("|| Nama :", item['nama'])
            print("|| Jenis Kelamin :", item['jenis_kelamin'])
            print("|| Agama :", item['agama'])
            print("|| Status :", item['status'])
            print("|| Pekerjaan :", item['pekerjaan'])
    return counter

def penduduk_perempuan_yang_tidak_beragama_Islam():
    counter = 0
    for item in data.values():
        if item.get("jenis_kelamin") == "P" and item.get("agama") != 1:
            counter += 1
            print("||","="*67)
            print("|| NIK :", item['nik'])
            print("|| Nama :", item['nama'])
            print("|| Jenis Kelamin :", item['jenis_kelamin'])
            print("|| Agama :", item['agama'])
            print("|| Status :", item['status'])
            print("|| Pekerjaan :", item['pekerjaan'])
    return counter

def penduduk_laki2_yang_pekerjaanya_PNS():
    counter = 0
    for item in data.values():
        if item.get("jenis_kelamin") == "L" and item.get("pekerjaan") == 1:
            counter += 1
            print("||","="*67)
            print("|| NIK :", item['nik'])
            print("|| Nama :", item['nama'])
            print("|| Jenis Kelamin :", item['jenis_kelamin'])
            print("|| Agama :", item['agama'])
            print("|| Status :", item['status'])
            print("|| Pekerjaan :", item['pekerjaan'])
    return counter

def penduduk_laki2_pekerjaan_petani_atau_nelayan():
    counter = 0
    for item in data.values():
        if item.get("jenis_kelamin") == "L" and (item.get("pekerjaan") == 4 or item.get("pekerjaan") == 5):
            counter += 1
            print("||","="*67)
            print("|| NIK :", item['nik'])
            print("|| Nama :", item['nama'])
            print("|| Jenis Kelamin :", item['jenis_kelamin'])
            print("|| Agama :", item['agama'])
            print("|| Status :", item['status'])
            print("|| Pekerjaan :", item['pekerjaan'])
    return counter

def print_penduduk_perempuan_yang_belum_kawin(count):
    clear_screen()
    penduduk_perempuan_yang_belum_kawin()
    print("||","="*67)
    print(f"|| jumlah penduduk perempuan yang belum kawin: [{count}]")
    print("||","="*67)

def print_penduduk_perempuan_yang_tidak_beragama_Islam(count):
    clear_screen()
    penduduk_perempuan_yang_tidak_beragama_Islam()
    print("||","="*67)
    print(f"|| jumlah penduduk perempuan yang tidak beragama islam: [{count}]")
    print("||","="*67)

def print_penduduk_laki2_yang_pekerjaanya_PNS(count):
    clear_screen()
    penduduk_laki2_yang_pekerjaanya_PNS()
    print("||","="*67)
    print(f"|| jumlah penduduk laki-laki yang perkerjaannya PNS: [{count}]")
    print("||","="*67)

def print_penduduk_laki2_pekerjaan_petani_atau_nelayan(count):
    clear_screen()
    penduduk_laki2_pekerjaan_petani_atau_nelayan()
    print("||","="*67)
    print(f"|| jumlah penduduk laki-laki yang perkerjaannya petani atau nelayan: [{count}]")
    print("||","="*67)

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

while True:
    menu_awal()
    menu = input("Silahkan Pilih Menu [1-5]: ")

    if menu == "1":
        count = penduduk_perempuan_yang_belum_kawin()
        print_penduduk_perempuan_yang_belum_kawin(count)
        coba_lagi = input("Pilih Menu lagi [Y/T] : ")
        if coba_lagi == 't' or coba_lagi =="T":
            break
        
    elif menu == "2":
        count = penduduk_perempuan_yang_tidak_beragama_Islam()
        print_penduduk_perempuan_yang_tidak_beragama_Islam(count)
        coba_lagi = input("Pilih Menu lagi [Y/T] : ")
        if coba_lagi == 't' or coba_lagi =="T":
            break

    elif menu == "3":
        count = penduduk_laki2_yang_pekerjaanya_PNS()
        print_penduduk_laki2_yang_pekerjaanya_PNS(count)
        coba_lagi = input("Pilih Menu lagi [Y/T] : ")
        if coba_lagi == 't' or coba_lagi =="T":
            break

    elif menu == "4":
        count = penduduk_laki2_pekerjaan_petani_atau_nelayan()
        print_penduduk_laki2_pekerjaan_petani_atau_nelayan(count)
        coba_lagi = input("Pilih Menu lagi [Y/T] : ")
        if coba_lagi == 't' or coba_lagi =="T":
            break

    elif menu == "5":
        break

    else:
        clear_screen()
        print("="*83)
        print("Pilihan Menu Tidak Valid")
        print("="*83)
        break
    
print("="*83)
print("Keluar")
print("="*83)