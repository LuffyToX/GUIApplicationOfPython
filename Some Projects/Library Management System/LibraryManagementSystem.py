class Book:
    def __init__(self, name, author, state, book_position):
        self.name = name
        self.author = author
        self.state = state   # 判断书的状态0：借出 1：未借出
        self.book_position = book_position
    # 打印对象时自动调用str（对象）
    def __str__(self):
        return f"书名：《{self.name}》，作者：<{self.author}>,状态：<{self.state}>,位置：<{self.book_position}>"


class Book_Manag:
    books = []

    def start(self):
        "对图书信息进行初始化"
        b1 = Book("三体", "刘慈欣", 1, "SN700")
        b2 = Book("白夜行", "东野圭吾", 1, "SN705")
        b3 = Book("C语言程序设计", "谭浩强", 1, "SN711")
        b4 = Book("放学后", "东野圭吾", 1, "SN706")
        b5 = Book("秘密", "东野圭吾", 1, "SN755")
        b6 = Book("解忧杂货店", "东野圭吾", 1, "SN752")
        b7 = Book("超新星纪元", "刘慈欣", 1, "SN857")

        self.books.append(b1)
        self.books.append(b2)
        self.books.append(b3)
        self.books.append(b4)
        self.books.append(b5)
        self.books.append(b6)
        self.books.append(b7)

    def directory(self):
        self.start()
        while True:
            print("""小钟图书管理系统：
                1. 查询
                2. 增加
                3. 借阅
                4. 归还
                5. 退出
            """)

            chioce = int(input("输入你想要的操作:"))
            if chioce == 1:
                name = input("你想查询书籍的书名：")
                self.checkBook(name)
            elif chioce == 2:
                self.addBook()
            elif chioce == 3:
                self.borrowBook()
            elif chioce == 4:
                self.return_book()
            elif chioce == 5:
                print("退出系统！")
                break
            else:
                print("您的输入有误，请重新输入！")

    # 添加书籍
    def addBook(self):
        name = input("需要添加书籍的书名：")
        self.books.append(Book(name,input("作者："),1,input("位置：")))
        print(f"图书{name}添加成功！")

    # 借书
    def borrowBook(self):
        name = input("借阅书籍名称：")
        Books = self.checkBook(name)
        # 判断书的状态
        if Books !=None:
            if Books.state == 0:
                print(f"书籍《{name}》已经借出！")
            elif Books.state == 1:
                print(f"书籍《{name}》借阅成功！")
                Books.state = 0
        else:
            print(f"书籍《{name}》不存在！")

    # 归还书籍
    def return_book(self):
        name = input("归还书籍名称：")
        Books = self.checkBook(name)
        if Books != None :
            if Books.state == 1:
                print(f"书籍《{name}》已经借出！")
            elif Books.state == 0:
                print(f"书籍《{name}》归还成功！")
                Books.state = 1
        else:
            print(f"书籍《{name}》与借出的不一致！")

    def checkBook(self,name):
        "查找书籍是否存在"
        for book in self.books:
            # book：Book类创建的对象
            if book.name == name:
                print(book)
                return book
        else:
            return print(f"你查询的书籍《{name}》不在系统中！请重新输入！")

book_Manag = Book_Manag()
book_Manag.directory()
