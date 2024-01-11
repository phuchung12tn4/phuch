Nhiet_do = input("Nhập nhiệt độ các ngày trong tuần theo thứ tự: ")
list_nhietdo = Nhiet_do.split(",")
Ngay_trong_tuan = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
b = -1
for a in list_nhietdo:
    b = b + 1 
    print(f'{Ngay_trong_tuan[b]} : {a}')