def add_product(name, price, quantity):
    product = {
        "name": name,
        "price": price,
        "qty": quantity
    }
    products.append(product)
    print("✔ Đã thêm sản phẩm vào kho!")
elif choice == "1":
