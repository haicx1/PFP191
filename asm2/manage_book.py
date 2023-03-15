from book import Book


class ManageBook:
    list_write = list()
    list_book = list()

    def write_book(self):
        with open('book.txt', 'w') as fh:
            while True:
                try:
                    n = int(input('So cuon sach muon ghi:'))
                    break
                except:
                    print('invalid input')
            fh.write(str(n))
            fh.write('\n')
            for i in range(n):
                book = Book(input('Nhap ten sach'), input('Nhap ten tac gia'), input('nhap ten nxb'), input('nam xb'),
                            input('gia'))
                self.list_write.append(
                    [book.Ten_sach, book.Ten_tac_gia, book.Nha_xuat_ban, book.Nam_XB, book.Gia_ban, ''])
            for line in self.list_write:
                for i in line:
                    fh.write(i)
                    fh.write('\n')
            fh.close()

    def read_book(self):
        with open('book.txt', 'r') as fh:
            lines = fh.readlines()
            for i in range(1, len(lines), 6):
                self.list_book.append(Book(lines[i].rstrip('\n'), lines[i + 1].rstrip('\n'), lines[i + 2].rstrip('\n'),
                                           lines[i + 3].rstrip('\n'), lines[i + 4].rstrip('\n')))
            fh.close()

    def sort_book(self):
        self.read_book()
        self.list_book.sort(key=lambda x: x.Nam_XB, reverse=True)
        for book in self.list_book:
            book.display()

    def search_book(self):
        name = input('Tim ten sach:')
        self.read_book()
        list_name = [x for x in self.list_book if x.Ten_sach == name]
        if not list_name:
            print('Khong tim thay ten sach')
        else:
            for nam in list_name:
                nam.display()

    def search_book_1(self):
        name = input('Tim ten tac gia:')
        self.read_book()
        list_name = [x for x in self.list_book if x.Ten_tac_gia == name]
        if not list_name:
            print('Khong tim thay ten tac gia')
        else:
            for nam in list_name:
                nam.display()

    def menu(self):
        while True:
            print(''.rjust(50,'='))
            print('1.Nhap thong tin n cuon sach cua FU')
            print('2.In ra man hinh thong tin vua nhap')
            print('3.Sap xep thong tin giam dan theo nam xuat ban va hien thi')
            print('4.Tim kiem theo ten sach')
            print('5.Tim kiem theo ten tac gia')
            print('6.Thoat')
            print(''.rjust(50,'='))
            try:
                choice = int(input('Nhap lua chon tu 1 -> 6:'))
            except:
                print('vui long nhap lai')
            if choice == 1:
                self.write_book()
                continue
            elif choice == 2:
                self.read_book()
                for book in self.list_book:
                    book.display()
                continue
            elif choice == 3:
                self.sort_book()
                continue
            elif choice == 4:
                self.search_book()
                continue
            elif choice == 5:
                self.search_book_1()
                continue
            elif choice == 6:
                print('Exit')
                break

