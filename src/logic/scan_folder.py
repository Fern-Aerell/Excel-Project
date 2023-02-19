import os
import shutil

def ScanFolder(folder_asal, read_file, copy_folder, detect_epub, change_name_file):
    os.system('cls' if os.name == 'nt' else 'clear')
    content = []
    print("Scan Folder Is Running...")
    try:

        folder_asal_split = folder_asal.split(sep="/")
        folder_asal_split = folder_asal.split(sep="\\")

        if copy_folder:
            #2. Membuat Folder Baru Sesuai Nama Folder Asli Pada Folder Hasil
            try:
                print("Membuat Folder " + folder_asal_split[-1])
                os.makedirs("Hasil\\" + folder_asal_split[-1])
                folder_hasil = "Hasil\\" + folder_asal_split[-1]
            except:
                print("Error : Gagal Membuat Folder " + folder_asal_split[-1])

            # 3. Mengcopy Semua File Pada Folder Asli Ke Folder Hasil
            try:
                print("Mengcopy semua file pada folder " + folder_asal + " ke " + folder_hasil)
                daftar_file_pada_folder_asal = os.listdir(folder_asal)
                for file in daftar_file_pada_folder_asal:
                    file_path = os.path.join(folder_asal, file)
                    if os.path.isfile(file_path):
                        shutil.copy(file_path, folder_hasil)
            except:
                print("Error : Gagal mengcopy semua file pada folder " + folder_asal + " ke " + folder_hasil)
        else:
            folder_hasil = folder_asal

        # Ketika Ada File Epub
        #4. Membaca Semua File Pada Folder Hasil
        try:
            print("Membaca file yang ada di folder " + folder_hasil)
            daftar_file_pada_folder_hasil = os.listdir(folder_hasil)
        except:
            print("Error : Gagal file yang ada di folder " + folder_hasil)

        if detect_epub:
            #5. Mendeteksi File Epub Pada Folder Hasil
            try:
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
            except:
                print("Error : Gagal mendeteksi file epub")

        # Lanjutan
        #9. Membaca Semua File Pada Folder Hasil
        try:
            print("Membaca file yang ada di folder " + folder_hasil)
            daftar_file_pada_folder_hasil = os.listdir(folder_hasil)
        except:
            print("Error : Gagal membaca file yang ada di folder " + folder_hasil)

        if read_file:
            #10. Menyimpan Hasil Bacaan Pada Folder Hasil dengan nama file "Nama File Pdf.txt"
            try:
                print("Menyimpan hasil nya pada file Nama" + folder_hasil + "\File PDF.txt")
                for file in daftar_file_pada_folder_hasil:
                    file_path = os.path.join(folder_hasil, file)
                    if os.path.isfile(file_path):
                        content.append(file + "\n")
                file_nama = "Nama File PDF.txt"
                with open(folder_hasil + "\\" + file_nama, 'w') as f:
                    f.write("".join(content))
                    print("File written: " + file_nama)
            except:
                print("Error : Gagal menyimpan hasil nya pada file Nama" + folder_hasil + "\File PDF.txt")

        if change_name_file:
            #11. Mengubah Semua Nama File Pada Folder Hasil Menjadi Ada Angka Nya Sebelum Nama File nya, Contoh "1_Buku guru.pdf"
            try:
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
            except:
                print("Error : Gagal mengubah semua nama file pada folder " + folder_hasil)

        #12. Membaca Lagi Semua File Pada Folder Hasil
        try:
            print("Membaca file yang ada di folder " + folder_hasil)
            daftar_file_pada_folder_hasil = os.listdir(folder_hasil)
        except:
            print("Error : Gagal membaca file yang ada di folder " + folder_hasil)
            
        #13. Program Selesai
        print("Scan Folder Selesai...")
        content.clear()
    except:
        print("Scan Folder Selesai...")
        content.clear()