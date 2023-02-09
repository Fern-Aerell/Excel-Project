import os

def read_folder(folder, depth, folder_name):
    list_of_files = os.listdir(folder)
    for file in list_of_files:
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            print(file)
            content.append(file + "\n")
        elif os.path.isdir(file_path):
            print("\n" + folder_name + ", " + file)
            content.append("\n" + folder_name + ", " + file + "\n")
            read_folder(file_path, depth + 1, folder_name + ", " + file)

def write_file(file_name):
    with open(file_name, 'w') as f:
        f.write("".join(content))
        print("File written: " + file_name)

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("= Excel Project : Create By AerellDev =")
    print("=======================================")
    print("")
    print("1. Scan Folder")
    print("2. Exit")
    input_ = input("")
    if input_ == "1":
        print("NOTE : Pastikan folder yang ingin di scan berada di satu folder yang sama, agar hasilnya sesuai dengan yang di inginkan.")
        folder_path = input("Nama Folder : ")
        scan_folder_and_file_tree(folder_path)
    elif input_ == "2":
        return
    else:
        main_menu()

def scan_folder_and_file_tree(folder_path):
    try:
        content.clear()
        read_folder(folder_path, 0, folder_path)
        write_file("hasil.txt")
        main_menu()
    except:
        main_menu()

content = []
main_menu()