import os

def show_wifi_pass(wifi_name):
	os.system('netsh wlan show profiles name ="' + wifi_name +'" key=clear | find "Key Content"')                                                                                      

os.system("netsh wlan show profiles")
wifi_name = input("Please Enter Wifiname :")
show_wifi_pass(wifi_name)