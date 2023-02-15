import os
import shutil

def read_folder(folder, depth, folder_nama):
    list_of_files = os.listdir(folder)
    print(list_of_files)
    for file in list_of_files:
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            print(file)
            content.append(file + "\n")
        elif os.path.isdir(file_path):
            print("\n" + folder_nama + ", " + file)
            content.append("\n" + folder_nama + ", " + file + "\n")
            read_folder(file_path, depth + 1, folder_nama + ", " + file)

def write_file(file_name):
    with open(file_name, 'w') as f:
        f.write("".join(content))
        print("File written: " + file_name)

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("= Excel Project : Create By AerellDev =")
    print("= Version       : 2.0.0 Release       =")
    print("=======================================")
    print("")
    print("1. Scan Folder (New)")
    print("2. Scan Folder")
    print("3. Exit")
    input_ = input("")
    if input_ == "1":
        try:
            #Cara Kerja
            #
            #Console View
            print("NOTE       : Fitur ini adalah perubahan pada fitur sebelumnya.")
            print("")
            print("Cara kerja : 1. Mengcopy semua file pada folder yang di berikan ke folder hasil.")
            print("             2. Memisahkan File Pdf Dengan File Epub.")
            print("             3. Membaca semua nama file dan menyimpan ke dalam File PDF.txt.")
            print("             4. Menambahkan nomor pada semua nama file.")
            print("")
            folder_asal = input("Masukkan Lokasi Folder : ")
            folder_asal_split = folder_asal.split(sep="\\")
            #1. Membuat Folder Hasil Jika Tidak Ada
            folder_nama = "Hasil"
            if not os.path.exists(folder_nama):
                os.makedirs(folder_nama)
                print("Membuat folder Hasil...")
            #2. Membuat Folder Baru Sesuai Nama Folder Asli Pada Folder Hasil
            print("Membuat Folder " + folder_asal_split[-1])
            os.makedirs("Hasil\\" + folder_asal_split[-1])
            folder_hasil = "Hasil\\" + folder_asal_split[-1]
            #3. Mengcopy Semua File Pada Folder Asli Ke Folder Hasil
            print("Mengcopy semua file pada folder " + folder_asal + " ke " + folder_hasil)
            daftar_file_pada_folder_asal = os.listdir(folder_asal)
            for file in daftar_file_pada_folder_asal:
                file_path = os.path.join(folder_asal, file)
                if os.path.isfile(file_path):
                    shutil.copy(file_path, folder_hasil)
            # Ketika Ada File Epub
            #4. Membaca Semua File Pada Folder Hasil
            print("Membaca file yang ada di folder " + folder_hasil)
            daftar_file_pada_folder_hasil = os.listdir(folder_hasil)
            #5. Mendeteksi File Epub Pada Folder Hasil
            ada_file_epub = False
            print("Mendeteksi file epub")
            for file in daftar_file_pada_folder_hasil:
                if '.epub' in file:
                    ada_file_epub = True
                    print("Ada file epub : " + file)
                    break
                else:
                    print("Tidak ada file epub")
                    ada_file_epub = False
            if ada_file_epub:
                #6. Memindahkan file epub ke folder terpisah
                #7. Membuat Folder Epub
                os.makedirs(folder_hasil + "\\epub")
                #8. Memindahkan File Epub Ke Folder Epub
                for file in daftar_file_pada_folder_hasil:
                    if '.epub' in file:
                        shutil.move(folder_hasil + "\\" + file, folder_hasil + "\\epub\\" + file)
            # Lanjutan
            #9. Membaca Semua File Pada Folder Hasil
            print("Membaca file yang ada di folder " + folder_hasil)
            daftar_file_pada_folder_hasil = os.listdir(folder_hasil)
            #10. Menyimpan Hasil Bacaan Pada Folder Hasil dengan nama file "Nama File Pdf.txt"
            print("Menyimpan hasil nya pada file Nama" + folder_hasil + "\File PDF.txt")
            for file in daftar_file_pada_folder_hasil:
                file_path = os.path.join(folder_hasil, file)
                if os.path.isfile(file_path):
                    content.append(file + "\n")
            file_nama = "Nama File PDF.txt"
            with open(folder_hasil + "\\" + file_nama, 'w') as f:
                f.write("".join(content))
                print("File written: " + file_nama)
            #11. Mengubah Semua Nama File Pada Folder Hasil Menjadi Ada Angka Nya Sebelum Nama File nya, Contoh "1_Buku guru.pdf"
            print("Mengubah semua nama file pada folder " + folder_hasil)
            start_num = 0
            for i, file_name in enumerate(daftar_file_pada_folder_hasil):
                file_path = os.path.join(folder_hasil, file_name)
                if os.path.isfile(file_path):
                    old_path = os.path.join(folder_hasil, file_name)
                    new_name = f"{start_num + 1}_{file_name}"
                    new_path = os.path.join(folder_hasil, new_name)
                    os.rename(old_path, new_path)
                    start_num += 1
            #12. Membaca Lagi Semua File Pada Folder Hasil
            print("Membaca file yang ada di folder " + folder_hasil)
            daftar_file_pada_folder_hasil = os.listdir(folder_hasil)
            #13. Program Selesai
            print("Program Selesai...")
            content.clear()
            main_menu()
        except:
            content.clear()
            main_menu()
    if input_ == "2":
        print("Cara kerja : Program ini akan membaca semua nama nama file yang ada dalam lokasi folder yang di berikan, dan akan menyimpan hasil nya pada `hasil.txt`.")
        print("NOTE       : Nama nama file yang terbaca kadang teracak dan urutan nya berbeda dari yang ada di folder, pastikan untuk memeriksa nya terlebih dahulu.")
        print("")
        folder_asal = input("Masukkan Lokasi Folder : ")
        scan_folder_and_file_tree(folder_asal)
    elif input_ == "3":
        return
    else:
        main_menu()

def scan_folder_and_file_tree(folder_asal):
    try:
        content.clear()
        read_folder(folder_asal, 0, folder_asal)
        write_file("hasil.txt")
        main_menu()
    except:
        main_menu()

content = []
main_menu()