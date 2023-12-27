import os
# peringatan aja sih hehehe
print("install menggunakan bahasa python (masih belum mahir sih hehehe)")
print("install dulu yang di butuhkan (bagi yang belum pernah install yang bagian ini)")

# setup variabel dulu biar ga gagal install 
sudo = "sudo apt update"
sudo2 = "sudo apt install openjdk-17-jre-headless -y"
sudo3 = "sudo apt install screen -y"
sudo4 = "sudo install ufw -y"
sudo5 = "sudo ufw allow 25565"
down_jar = "wget https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar"

# tinggal jalan aja kode variabel nya 
os.system(sudo)

os.system(sudo2)

os.system(sudo3)

os.system(sudo4)

os.system(sudo5)

os.system(down_jar)

print("kerja bagus install selesai")
