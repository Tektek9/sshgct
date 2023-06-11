import subprocess
import sys

print("=====KuliOnline0011=====")
print("= SSH Connector&Tester =")
print("========================")
print("1. Create ssh pub")
print("2. Send ssh pub to target")
print("3. Test ssh connection to target")
aa = int(input("Silahkan pilih menu diatas: "))

perintah = "ssh-keygen -t rsa -b 2048"
perintah2 = "ssh-copy-id -i ~/.ssh/id_rsa.pub {username}@{ip}"
perintah3 = "ssh -i ~/.ssh/id_rsa {username}@{ip}"

if aa == 1:
   proses = subprocess.call(perintah, shell=True)
   print("SSH Pub Key created")
elif aa == 2:
   username = str(input("Username Target: "))
   ip = str(input("Ip Target: "))   
   perintah2 = perintah2.format(username=username, ip=ip)
   proses = subprocess.call(perintah, shell=True)
   proses2 = subprocess.call(perintah2, shell=True)
   print("SSH Pub Key sended")
elif aa == 3:
   username = str(input("Username Target: "))
   ip = str(input("Ip Target: "))   
   perintah3 = perintah3.format(username=username, ip=ip)
   proses3 = subprocess.call(perintah3, shell=True)
else:
   sys.exit()
