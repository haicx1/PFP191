from location import Location


class ManageAndress:
    datas = list()
    path = r'C:\Users\haich\Downloads\Documents\file\log.txt'

    def read_data(self, path):
        with open(path, 'r') as fh:
            for line in fh.readlines():
                data = line.split()
                andress = Location(data[0], data[1], data[2])
                self.datas.append(andress)
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
        dia_diem = 'Địa điểm(độ rộng 50)'
        gio = 'Giờ'
        phut = 'Phút'

        print("{: <41} {: <11} {: <11}".format(dia_diem, gio, phut))
        self.read_data(self.path)
        for address in self.datas:
            print("{: <41} {: <11} {: <11}".format(address.name, address.hr, address.mins))

    def search(self,path,name):
        self.read_data(path)


manage = ManageAndress()
manage.print_history()
