from location import Location
import datetime


class ManageAddress:
    datas = list()
    path = 'log.txt'

    def read_data(self):
        with open(self.path, 'r') as fh:
            for line in fh.readlines():
                data = line.split()
                address = Location(data[0], data[1], data[2])
                self.datas.append(address)
            fh.close()
            return self.datas

    def menu(self):
        print('=========================')
        print('CHUONG TRINH TRUY VET COVID 19')
        print('1.Nap file log lịch sử di chuyển')
        print('2.In ra lịch sử di chuyển')
        print('3.Tìm kiếm lịch sử địa điểm')
        print('4.Tìm kiếm lịch sử thời gian')
        print('5.Kiểm tra truy vết mới nhất')
        print('6.Thoát')

    def print_history(self):
        dia_diem = 'Địa điểm'
        gio = 'Giờ'
        phut = 'Phút'

        print("{: <41} {: <11} {: <11}".format(dia_diem, gio, phut))
        self.read_data()
        for address in self.datas:
            print("{: <41} {: <11} {: <11}".format(address.name, address.hr, address.mins))

    def search(self):
        name = input('Nhap vao dia diem:')
        self.read_data()
        list_search = [x for x in self.datas if x.name == name]
        if list_search is None:
            print('Ban chua toi dia diem do')
        else:
            for address in list_search:
                print(f'{address.hr}:{address.mins}', end=', ')

    def search_by_time(self):
        self.read_data()
        while True:
            try:
                hour = int(input('Nhap vao gio:'))
                if hour in range(0, 25):
                    break
                else:
                    continue
            except:
                print('Vui long nhap lai')
        while True:
            try:
                minutes = int(input('Nhap vao gio:'))
                if minutes in range(0, 61):
                    break
                else:
                    continue
            except:
                print('Vui long nhap lai')
        list_search = [x for x in self.datas if (x.hr == hour and x.mins == minutes)]
        if list_search is None:
            print('KHONG tim thay lich su di chuyen!')
        else:
            for address in list_search:
                print(f'{address.name}')

    def if_f1_or_not(self):
        isF1 = False
        self.read_data()
        while True:
            try:
                covid = input('Nhap vao noi xuat hien benh nhan covid:').split()
                address_covid = Location(covid[0], covid[1], covid[2])
                time_covid = datetime.time(hour=int(address_covid.hr), minute=int(address_covid.mins))
                break
            except:
                print('Error, Vui long nhap lai')
        list_search = [x for x in self.datas if x.name == address_covid.name]
        if list_search is None:
            print('Lich su di chuyen cua ban OK')
        else:
            for address in list_search:
                time_user = datetime.time(hour=int(address.hr), minute=int(address.mins))
                if time_user > time_covid:
                    isF1 = True
                    break
                else:
                    pass
        if isF1:
            print('Ban co kha nang bi lay Covid, can phai khai bao y te ngay lap tuc!')
        elif not isF1:
            print('Lich su di chuyen cua ban OK')

    def menu_covid(self):
        self.read_data()
        while True:
            self.menu()
            try:
                choice = int(input('Enter choice(1 -> 6):'))
            except:
                print('vui long nhap so tu 1 -> 6')
            if choice not in range(1, 8):
                print('vui long nhap so tu 1 -> 6')
                continue
            if choice == 1:
                self.read_data()
                print('da doc xong file!')
                continue
            elif choice == 2:
                self.print_history()
                continue
            elif choice == 3:
                self.search()
                continue
            elif choice == 4:
                self.search_by_time()
                continue
            elif choice == 5:
                self.if_f1_or_not()
                continue
            elif choice == 6:
                print('Exit program')
                break



