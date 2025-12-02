products = []

def main():
    while True:
        print("\n=== INVENTORY MANAGER ===")
        print("1. Nhập hàng (Thêm sản phẩm)")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng (< 5)")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Chức năng chưa được triển khai!")

if __name__ == "__main__":
    main()