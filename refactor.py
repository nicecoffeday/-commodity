import os # operating system 


# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = int(input('請輸入商品價格'))
        products.append([name, price])
    print(products)
    return products

#列印出購買紀錄
def print_produsts(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')



#主要執行程式
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#請求系統 檢查這個檔案有沒有在這個路徑下
        print('yeah 有的')
        produsts = read_file(filename)
    else:
        print('沒有')

    products = user_input(products)
    print_produsts(products)
    write_file('products.csv', products)


main()