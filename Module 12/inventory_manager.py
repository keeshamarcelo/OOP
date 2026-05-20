def add_product(product):
    try:
        with open("products.txt", "a") as file:
            file.write(product.get_product_info() + "\n")
        print("Product added successfully.")
    except Exception as e:
        print(f"Error adding product: {e}")

def view_products():
    try:
        with open("products.txt", "r") as file:
            print("Product List:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No products found.")
#kscm