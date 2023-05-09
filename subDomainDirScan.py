# 當有多個子域名需要進行目錄爆破時，使用該腳本透過gobuster完成目錄爆破
# 將所有結果分別存入DirScan目錄

# command example
# gobuster dir -u "dwvwdv.tk" -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt  -o DirScan/dwv.txt
# gobuster dir -u "info.*.com.tw" -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt  -o DirScan/infotest.txt
# -s -b 黑白名單處理

import re
import os

def read_file(file):
    with open(file, 'r', encoding='u8') as f:
        lines = f.read()
        return lines

def dir_brute(domains,dict_file = '/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt'):
    domain_list = domains.split('\n')
    if domain_list == None:
        return 
    for domain in domain_list:
        name = domain.split('.')[0]
        if(name != ''):
            print(f'gobuster dir -u "{domain}" -w {dict_file} -o DirScan/{name}.txt')
            os.system(f'gobuster dir -u http://"{domain}" -w {dict_file} -o DirScan/{name}.txt')

    

if __name__ == '__main__':
    domain_dict = read_file('./domain.txt')
    # attack_dict = '/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt'

    dir_brute(domain_dict)
    # dir_brute(domain, attack_dict)
