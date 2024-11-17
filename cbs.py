#!/usr/bin/env python3
import os
import shutil
import subprocess
import argparse
try:
    from git import Repo
except ImportError:
    subprocess.check_call(["pip", "install", "gitpython"])
    from git import Repo
import sys
import time
from fitur.cmdlist import DaftarFitur

red = '\033[31m'       
green = '\033[32m'     
yellow = '\033[33m'    
blue = '\033[34m'      
magenta = '\033[35m'   
cyan = '\033[36m'      
white = '\033[37m'     
black = '\033[30m'
bg_black = '\033[40m'    
bg_red = '\033[41m'      
bg_green = '\033[42m'    
bg_yellow = '\033[43m'   
bg_blue = '\033[44m'     
bg_magenta = '\033[45m'  
bg_cyan = '\033[46m'     
bg_white = '\033[47m'
reset = '\033[0m'

ingfo = f"""\n{red}Disclaimer{reset}: {yellow}Jika anda mengubah nama atau rename ini atau recode tanpa izin
dari pembuat saya tidak akan membagikan atau share tools lagi terima kasih{reset}

Ketik {green}cmd{reset} untuk melihat fitur
{green}Ctrl + C{reset} atau ketik {green}0{reset} untuk keluar \n"""

def Banner():
    banner = """ ██████    ██████     ███████ 
██         ██   ██    ██      
██         ██████     ███████ 
██         ██   ██         ██ 
 ██████ ██ ██████  ██ ███████ 
@teamcbs"""
    width, _ = shutil.get_terminal_size()
    lines = banner.split('\n')
    
    red_start, green_start, blue_start = 128, 0, 128 
    red_end, green_end, blue_end = 255, 0, 0      
    num_steps = len(lines)
    
    for i, line in enumerate(lines):
        r = int(red_start + (red_end - red_start) * (i / (num_steps - 1)))
        g = int(green_start + (green_end - green_start) * (i / (num_steps - 1)))
        b = int(blue_start + (blue_end - blue_start) * (i / (num_steps - 1)))
        color = Uwu(r, g, b)
        spaces = (width - len(line)) // 2
        print(color + ' ' * spaces + line + reset)

def Uwu(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def FindFolderNames(base_path: str):
    counter = 1
    new_path = base_path
    while os.path.exists(new_path):
        new_path = f"{base_path}_{counter}"
        counter += 1
    return new_path

def copy_folder_contents(src: str, dest: str):
    try:
        if os.path.exists(src):
            shutil.copytree(src, dest, dirs_exist_ok=True)
            print(f"Semua file dan folder dari {src} telah disalin ke {dest}")
        else:
            print(f"Folder {src} tidak ditemukan.")
    except Exception as e:
        print(f"Error saat menyalin {src} ke {dest}: {e}")

def clone_github_repo(url: str, destination: str):
    try:
        if os.path.exists(destination):
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            destination = f"{destination}_{timestamp}"
        
        Repo.clone_from(url, destination)
        print(f"Repositori dari {url} telah berhasil dikloning ke {destination}")
    except Exception as e:
        print(f"Error saat mengkloning repositori dari {url}: {e}")

def LoadPayloads(path_or_url: str, folder_name: str = None):
    """Memuat payloads baik dari folder lokal atau URL repositori GitHub."""
    payloads_path = f"payloads/{folder_name}" if folder_name else "payloads"

    if path_or_url.startswith("http"):
        clone_github_repo(path_or_url, payloads_path)
    
    elif os.path.exists(path_or_url):
        if not os.path.exists(payloads_path):
            os.makedirs(payloads_path, exist_ok=True)
        copy_folder_contents(path_or_url, payloads_path)
    
    else:
        print(f"Path atau URL {path_or_url} tidak valid.")

def run_payload(command: str):
    """
    Menjalankan payload berdasarkan nama perintah dari daftar fitur
    """
    try:
        args = command.split(' ', 1)
        cmd_name = args[0]
        cmd_args = args[1] if len(args) > 1 else None
        DaftarFitur.JalankanPerintahFeature(cmd_name, args=cmd_args)
    except Exception as e:
        print(f"[ERROR] {e}")

def wizard():
    clear()
    Banner()
    print(ingfo)
    while True:
        try:
            shell = input(f'{bg_red}localhost@cbs~#{reset} ').strip()
            
            if shell.lower() == 'load':
                Pathnya = input('Path atau URL repositori GitHub >> ').strip()
                namaFolder = input('Nama folder untuk payloads >> ').strip()
                LoadPayloads(Pathnya, namaFolder)
            
            elif shell.lower() in ['exit', '0', 'quit']:
                print('Keluar dari aplikasi...')
                sys.exit(1)
            
            elif shell.lower() in ['cmd', 'help']:
                print(DaftarFitur.Fiturnya())
            elif shell.lower() in ['clear', 'cls']:
                clear()
                Banner()
                print(ingfo)
            else:
                run_payload(shell)

        except KeyboardInterrupt:
            print('\n[KELUAR] Program dihentikan oleh pengguna.')
            sys.exit(1)
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan: {e}")

def main():
    parser = argparse.ArgumentParser(description="Skrip untuk memuat dan menjalankan payloads")
    parser.add_argument("--load", type=str, help="Path folder atau URL repo GitHub untuk memuat payloads")
    parser.add_argument("--folder", type=str, help="Nama folder untuk payloads (opsional, digunakan dengan --load)")
    parser.add_argument("--run", type=str, nargs='+', help="Perintah untuk menjalankan payload, bisa lebih dari satu argumen")
    parser.add_argument("--wizard", action="store_true", help="Jalankan wizard UI")
    parser.add_argument("--version", "-v", action="store_true", help="Lihat versi")

    args = parser.parse_args()

    if args.load:
        folder_name = args.folder if args.folder else None
        print(f"Memulai proses impor payloads dari: {args.load}")
        LoadPayloads(args.load, folder_name)
    
    elif args.run:
        command = " ".join(args.run)
        print(f"Menjalankan perintah: {command}")
        run_payload(command)
    
    elif args.wizard:
        wizard()

    elif args.version:
        print('1.0.1 first release by @adjidev')
    
    else:
        print("Error! Harap masukkan salah satu opsi: --load atau --run.\nGunakan --help untuk bantuan lebih lanjut.")

if __name__ == "__main__":
    main()