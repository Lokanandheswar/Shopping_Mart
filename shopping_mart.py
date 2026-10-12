# lists Creation
product_list = []
user_list = []
cart_list = []
order_list = []

# Roles
while True:
    print("Welcome to our shopping mart")
    print("1.Admin")
    print("2.User")
    print("3.Exit")

    choice = int(input("Enter your choice: "))

    # Admin Menu
    if choice == 1:
        print("Welcome to Admin Menu")
        while True:
            print("1.Add Products")
            print("2.Update Product")
            print("3.Remove Product")
            print("4.View Products")
            print("5.View Users")
            print("6.Exit")

            admin_choice = int(input("Enter your choice: "))
# Add Products
            if admin_choice == 1:
                product_id = input("Enter Product ID: ")
                product_name = input("Enter the Product Name: ")
                product_price = input("Enter the Product Price: ")

                product = [product_id, product_name, product_price]
                product_list.append(product)
                print("Product Added Successfully")
# Update Products
            elif admin_choice == 2:
                product_id = input("Enter product ID to update: ")
                for product in product_list:
                    if product[0] == product_id:
                        new_name = input("Enter the New Product Name: ")
                        new_price = input("Enter the New Product Price: ")

                        product[1] = new_name
                        product[2] = new_price

                        print("Product Updated")
                        break
                else:
                    print("Product not found")
# Remove Product
            elif admin_choice == 3:
                product_id = input("Enter the Product ID to remove: ")
                for product in product_list:
                    if product[0] == product_id:
                        product_list.remove(product)
                        print("Product Removed")
                        break
                else:
                    print("Product not found")
# View Product
            elif admin_choice == 4:
                if len(product_list) == 0:
                    print("No products available")
                else:
                    for product in product_list:
                        print("-" * 30)
                        print("Product ID:", product[0])
                        print("Product Name:", product[1])
                        print("Product Price:", product[2])
                        print("-" * 30)
# view Users
            elif admin_choice == 5:
                if len(user_list) == 0:
                    print("No users found")
                else:
                    for user in user_list:
                        print("-" * 30)
                        print("User ID:", user[0])
                        print("User Name:", user[1])
                        print("User Email:", user[2])
                        print("-" * 30)
# Exit from the admin
            elif admin_choice == 6:
                print("Exiting Admin")
                break
# Invalid choice
            else:
                print("Invalid Choice. Please Try again.")

    # User Menu
    elif choice == 2:
        print("Welcome to User Menu")

        # User Registration
        user_id = input("Enter User ID: ")

        found = False
        for user in user_list:
            if user[0] == user_id:
                found = True
                break

        if found:
            print("User already exists")
        else:
            user_name = input("Enter User Name: ")
            user_email = input("Enter User Email: ")

            user = [user_id, user_name, user_email]
            user_list.append(user)
            print("User added successfully")

        # User Menu Loop
        while True:
            print("1.View Products")
            print("2.Add to Cart")
            print("3.Remove from Cart")
            print("4.View Cart")
            print("5.Checkout")
            print("6.Exit")

            user_choice = int(input("Enter your choice: "))

            # View Products
            if user_choice == 1:
                if len(product_list) == 0:
                    print("No products available")
                else:
                    for product in product_list:
                        print("-" * 30)
                        print("Product ID:", product[0])
                        print("Product Name:", product[1])
                        print("Product Price:", product[2])
                        print("-" * 30)

            # Add to Cart
            elif user_choice == 2:
                if len(product_list) == 0:
                    print("No products available")
                else:
                    while True:
                        product_id = input("Enter the Product ID to add to cart: ")
                        found = False

                        for product in product_list:
                            if product[0] == product_id:
                                cart_list.append(product)
                                print("Product is added to cart successfully")
                                found = True
                                break

                        if found == False:
                            print("Product not found")

                        another_product = input(
                            "Do you want to add another Product to Cart (yes/no): "
                        )
                        if another_product.lower() == "no":
                            break

            # Remove from Cart
            elif user_choice == 3:
                if len(cart_list) == 0:
                    print("Cart is empty")
                else:
                    while True:
                        product_id = input(
                            "Enter the Product ID to remove from the cart: "
                        )
                        found = False

                        for product in cart_list:
                            if product[0] == product_id:
                                cart_list.remove(product)
                                print(
                                    "Product is removed from the cart successfully"
                                )
                                found = True
                                break

                        if found == False:
                            print("Product not found in cart")

                        another_product = input(
                            "Do you want to remove another Product from the cart (yes/no): "
                        )
                        if another_product.lower() == "no":
                            break

            # View Cart
            elif user_choice == 4:
                if len(cart_list) == 0:
                    print("Cart is empty")
                else:
                    total = 0
                    for product in cart_list:
                        print("-" * 30)
                        print("Product ID:", product[0])
                        print("Product Name:", product[1])
                        print("Product Price:", product[2])
                        print("-" * 30)
                        total = total + int(product[2])
                    print("Total Amount:", total)

            # Checkout
            elif user_choice == 5:
                if len(cart_list) == 0:
                    print("Cart is empty")
                else:
                    total = 0
                    print("=" * 40)
                    print("           SHOPPING MART")
                    print("=" * 40)

                    for product in cart_list:
                        product_id = product[0]
                        product_name = product[1]
                        product_price = int(product[2])
                        print("Product ID:", product_id)
                        print("Product Name:", product_name)
                        print("Product Price:", product_price)
                        print("-" * 40)
                        total = total + product_price

                    print("Total Amount:", total)
                    confirm = input("Do you want to place the order? (yes/no): ")
                    if confirm.lower() == "yes":
                        order_list.append(cart_list.copy())
                        print("Order placed successfully")
                        cart_list.clear()

            # User Exit
            elif user_choice == 6:
                print("Exiting from the User Menu")
                break

            # Invalid User Choice
            else:
                print("Invalid Choice. Please Try again.")

    # Exit Menu
    elif choice == 3:
        print("Thank you for visiting our shopping mart. Have a great day!")
        break

    # Invalid Choice
    else:
        print("Invalid Choice. Please Try again.")
