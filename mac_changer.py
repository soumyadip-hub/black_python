# type: ignore
import subprocess
# ---------method2-----------------
interface = input("interface > ")
new_mac = input("new Mac > ")

print("[+] Changing your mac adress for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface +" down ", shell=True)
subprocess.call("ifconfig " + interface +" hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface +" up ", shell=True)



# -------------------------------------method1--------
# subprocess.call("ifconfig", shell=True) 
# subprocess.call("ifconfig wlan0 down", shell=True)
# subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55:66", shell=True)
# subprocess.call("ifconfig wlan0 up", shell=True)