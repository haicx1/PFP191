import operator
from collections import OrderedDict

from cophieu import VIC, FLC, HSG

data_path = r'C:\Users\haich\Downloads\Documents\file\data.txt'
VIC1 = list()
FLC1 = list()
HSG1 = list()
trungbinh = dict()
tang = dict()

def get_data(path):
    with open(path, 'r') as fh:
        for line in fh:
            if line.startswith('VIC'):
                words = line.split()
                vic = VIC(float(words[1]), float(words[2]))
                VIC1.append(vic)
            elif line.startswith('FLC'):
                words = line.split()
                flc = FLC(float(words[1]), float(words[2]))
                FLC1.append(flc)
            elif line.startswith('HSG'):
                words = line.split()
                hsg = HSG(float(words[1]), float(words[2]))
                HSG1.append(hsg)
        fh.close()


def sort_dict(dict):
    list_keys = list(dict.keys())
    list_keys.sort()
    new_dict = {i: dict[i] for i in list_keys}
    return new_dict


def read_file(path):
    get_data(path)
    sum_vic = 0
    sum_flc = 0
    sum_hsg = 0

    for i in VIC1:
        sum_vic = i.sub() + sum_vic
    trungbinh['VIC'] = sum_vic / len(VIC1)
    for i in FLC1:
        sum_flc = i.sub() + sum_flc
    trungbinh['FLC'] = round(sum_flc / len(FLC1), 3)
    for i in HSG1:
        sum_hsg = i.sub() + sum_hsg
    trungbinh['HSG'] = sum_hsg / len(HSG1)
    trungbinh1 = sort_dict(trungbinh)
    for i, j in trungbinh1.items():
        print(f'{i}: {j}')


def search(path):
    search_list_dau = list()
    search_list_cuoi = list()
    get_data(path)
    s = input('Nhap vao ma co phieu:')
    if s == VIC.name_vic:
        for i in VIC1:
            search_list_dau.append(i.dau)
            search_list_cuoi.append(i.cuoi)
        print(f'{s} : {max(search_list_dau)}, {max(search_list_cuoi)}')
    elif s == FLC.name_flc:
        for i in FLC1:
            search_list_dau.append(i.dau)
            search_list_cuoi.append(i.cuoi)
        print(f'{s} : {max(search_list_dau)}, {max(search_list_cuoi)}')
    elif s == HSG.name_hsg:
        for i in HSG1:
            search_list_dau.append(i.dau)
            search_list_cuoi.append(i.cuoi)
        print(f'{s} : {max(search_list_dau)}, {max(search_list_cuoi)}')
    else:
        print('Not Found')
def search_up(path):
    get_data(path)
    for i in range(len(VIC1), 2):
        if VIC1[i].sub() > 0 and VIC1[i + 1].sub() > 0:
            print(VIC1[i].display())
            print(VIC1[i+1].display())
    for i in range(len(FLC1), 2):
        if FLC1[i].sub() > 0 and FLC1[i + 1].sub() > 0:
            print('tang')
    for i in range(len(HSG1), 2):
        if HSG1[i].sub() > 0 and HSG1[i + 1].sub() > 0:
            print('tang')

def search_up1(path):
    get_data(path)
    for i in range(0, len(VIC1),2):
        if VIC1[i].sub() > 0 and VIC1[i + 1].sub() > 0:
            tang['VIC'] = tang.get('VIC',0) + 1
    for i in range(0, len(FLC1), 2):
        if FLC1[i].sub() > 0 and FLC1[i + 1].sub() > 0:
            tang['FLC'] = tang.get('FLC',0) + 1
    for i in range(0, len(HSG1), 2):
        if HSG1[i].sub() > 0 and HSG1[i + 1].sub() > 0:
            tang['HSG'] = tang.get('HSG',0) + 1
    max_tang = max(tang, key=tang.get)
    print(max_tang,tang[max_tang])

def menu():
    print('Menu')
    print('1.Doc file')
    print('2.Ma so chung khoan')
    print('3.Xu huong tang')
    print('4.Ma co so ngay tang lon nhat')
    print('5.Thoat')

while True:
    menu()
    choice = int(input('Enter choice:'))
    if choice == 1:
        read_file(data_path)
        continue
    elif choice == 2:
        search(data_path)
    elif choice == 3:
        search_up(data_path)
    elif choice == 4:
        search_up1(data_path)
    elif choice == 5:
        print('Exit')
        break


