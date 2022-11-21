#!/usr/bin/env python


import os


proxy = "127.0.0.1"
port = 8080


def proxy_on():
    os.system("networksetup -setwebproxy Wi-Fi " + proxy + " " + str(port))
    os.system("networksetup -setsecurewebproxy Wi-Fi " + proxy + " " + str(port))


def proxy_off():
    os.system('networksetup -setwebproxystate "Wi-Fi" off')
    os.system('networksetup -setsecurewebproxystate "Wi-Fi" off')


if __name__ == "__main__":
    # proxy_on()
    proxy_off()
