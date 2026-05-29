
# Input:
# - Danh sách sản phẩm product_list (list chứa dictionary)
# - Người dùng nhập:
#     + Lựa chọn menu (int)
#     + Mã sản phẩm (str)
#     + Số lượng mua / nhập thêm (int)
# Output:
# - Hiển thị danh sách sản phẩm
# - Hiển thị trạng thái tồn kho
# - Bán sản phẩm thành công
# - Nhập thêm hàng thành công
# - Báo cáo doanh thu
# - Tổng doanh thu
# - Sản phẩm có doanh thu cao nhất
# Chức năng 1:
# - Dùng vòng lặp for + enumerate() để duyệt danh sách
# - Kiểm tra số lượng tồn kho:
#     + quantity == 0 -> Hết hàng
#     + quantity <= 5 -> Sắp hết hàng
#     + còn ại -> Còn hàng
# Chức năng 2:
# - Nhập mã sản phẩm khách muốn mua
# - Tìm sản phẩm trong product_list
# - Kiểm tra số lượng mua hợp lệ
# - Trừ tồn kho và cộng số lượng đã bán
# Chức năng 3:
# - Nhập mã sản phẩm cần nhập thêm
# - Cộng thêm số lượng vào kho
# Chức năng 4:
# - Tính doanh thu từng sản phẩm:
#       revenue = price * sold
# - Tính tổng doanh thu
# - Tìm sản phẩm có doanh thu cao nhất
# Chức năng 5:
# - Thoát chương trình bằng break
# Khởi tạo danh sách product_list
# Lặp vô hạn:
#     Hiển thị menu
#     Nhập lựa chọn
#     Kiểm tra lựa chọn hợp lệ
#     Nếu chọn 1:
#         Duyệt danh sách sản phẩm
#         Kiểm tra tồn kho
#         In thông tin sản phẩm
#     Nếu chọn 2:
#         Kiểm tra danh sách rỗng
#         Nhập mã sản phẩm
#         Tìm sản phẩm
#         Nếu tìm thấy:
#             Nhập số lượng mua
#             Kiểm tra hợp lệ
#             Nếu hợp lệ:
#                 Giảm tồn kho
#                 Tăng số lượng đã bán
#         Nếu không tìm thấy:
#             Báo lỗi
#     Nếu chọn 3:
#         Nhập mã


product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]


while True:
    print('''
        ===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====
        1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho
        2. Bán sản phẩm cho khách hàng
        3. Nhập thêm hàng vào kho
        4. Xem báo cáo doanh thu
        5. Thoát chương trình
    ''')
    while True:
        try:
            choice = int(input('Nhập lựa chọn:'))
            if choice < 0 or choice > 5:
                print('Lựa chọn không hợp lệ - Xin vui lòng nhập lại')
            else:
                break
        except:
            print('Bạn phải nhập số nguyên dương')
    match choice:
        case 1:
            print('Danh sách sản phẩm hiện tại:')
            for index , values in enumerate(product_list , start = 1 ):
                if values['quantity'] == 0:
                    values['status'] = 'Hết hàng'
                elif values['quantity'] <= 5:
                    values['status'] = 'Sắp hết hàng'
                else:
                    values['status'] = 'Còn hàng'
                print(f'{index}. Mã SP: {values['product_id']} | Tên: {values['product_name']} | Giá: {values['price']} | Tồn kho: {values['quantity']} | Đã bán: {values['sold']} | Trạng thái: {values['status']} ')
        case 2:
            if not product_list:
                print('Danh sách sản phẩm hiện đang rỗng')
            else:
                while True:
                    found = False
                    id_input = input('Nhập mã sản phẩm khách muốn mua:').strip().upper()
                    for values in product_list:
                        if id_input == values['product_id']:
                            while True:
                                try:
                                    quantity_input = int(input('Nhập số lượng khách mua:'))
                                    if quantity_input <= 0:
                                        print('Yêu cầu quý khách không hợp lệ - Xin vui lòng nhập lại số lượng mua')
                                    elif quantity_input > values['quantity']:
                                        print('Trong kho không đủ số lượng yêu cầu của bạn - Xin vui lòng nhập lại')
                                    else:
                                        print(f'Bạn muốn mua {quantity_input} sản phẩm')
                                        break
                                except:
                                    print('Bạn phải nhập số nguyên lơn hơn 0')
                            values['quantity'] -= quantity_input
                            values['sold'] += quantity_input
                            found = True
                            break
                    if found == True:
                        break
                    elif found == False:
                        print('Mã sản phẩm không hợp lệ - Xin vui lòng nhập lại mã sản phẩm')
        case 3:
            while True:
                id_add = input('Nhập mã sản phẩm cần nhập thêm:').strip().upper()
                for values in product_list:
                    if id_add == values['product_id']:
                        while True:
                            try:
                                quantity_input = int(input('Nhập số lượng cần thêm: ')).strip().upper()
                                if quantity_input < 0:
                                    print('Bạn phải nhập số nguyên dương lớn hơn 0')
                                else:
                                    values['quantity'] += quantity_input
                                    print(f'Bạn đã thêm {quantity_input} sản phẩm')
                                    break
                            except:
                                print('Bạn không được nhập chữ - Xin vui lòng nhập lại')
        case 4:
            print('===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====')
            total_revenue = 0
            max_revenue = 0
            best_product = ''
            for index, values in enumerate( product_list, start=1 ):

                values['revenue'] = values['price'] * values['sold']
                total_revenue += values['revenue']

                if values['revenue'] > max_revenue:
                    max_revenue = values['revenue']
                    best_product = values['product_name']

                print(f"{index}. {values['product_name']} | Đã bán: {values['sold']} | Doanh thu: {values['revenue']}")

            print(f'Tổng doanh thu: {total_revenue}')
            print(f'Sản phẩm có doanh thu cao nhất: {best_product}')
        case 5:
            print('Thoát chương trình')
            break
        case _:
            print('Bạn nhập sai lựa chọn - Xin vui lòng nhập lại')
        