#========Module imports==========
# Displays output in a table. Execute "pip install tabulate" to run this code
from tabulate import tabulate
headers = ["\033[1m\033[94mCountry\033[0m", "\033[1m\033[94mCode\033[0m", \
           "\033[1m\033[94mProduct\033[0m", "\033[1m\033[94mCost\033[0m", \
           "\033[1m\033[94mQuantity\033[0m"]

#========The beginning of the class==========
class Shoe:
    # Initialise attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return quantity

    # Returns string representation of Shoe class
    def __str__(self):
        return (
            f"Country:          {self.country}\n"
            f"Code:             {self.code}\n"
            f"Product:          {self.product}\n"
            f"Cost:             {self.cost}\n"
            f"Quantity:         {self.quantity}\n"
        )

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    with open("inventory.txt", "r") as file:
        file = file.read().splitlines()
        
        # For each shoe, split attributes into list elements, then append to
        # shoe_list list. Defensive programming against IndexError in case
        # item in inventory.txt is formatted incorrectly
        for each_shoe in file[1:]:
            try:
                var = each_shoe.strip().split(",")
                shoe = Shoe(var[0], var[1], var[2], var[3], var[4])
                shoe_list.append(shoe)
            except IndexError:
                pass
        return shoe_list

def capture_shoes():
    # Ask user input for each attribute, & validate for each, ensuring appropriate
    # data type is being accepted
    while True:
        country = input("Enter country: ").strip().title()
        if country.isdigit() or country == "" or not country.isalnum():
            print("Invalid input. Please try again.")
            continue

        while True:
            code = input("Enter product code: ").strip().upper()
            if code.isdigit() or code == "" or not code.isalnum():
                print("Invalid input. Please try again.")
                continue
                
            while True:
                try:
                    product = input("Enter product name: ").strip().title()
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue

                while True:
                    try:
                        cost = int(input("Enter product cost: "))
                    except ValueError:
                        print("Invalid input. Please try again.")
                        continue
                    else:
                        break
                
                while True:
                    try:
                        quantity = int(input("Enter product quantity: "))
                    except ValueError:
                        print("Invalid input. Please try again.")
                        continue
                    else:
                        break
                break
            break
        break
        
    # Create shoe object, then append to list, & print success prompt
    add_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(add_shoe)
    print("\nSuccessfully added product.\n")           

def view_all():
    # Organise table data to pass as argument in tabulate()
    table_data = [[shoe.country, shoe.code, shoe.product, shoe.cost, 
    shoe.quantity] for shoe in shoe_list]

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

def re_stock(shoe_list):
    # Determine which shoe product has the lowest quantity
    quant_list = []
    for each_shoe in shoe_list:
        quant_list.append(int(each_shoe.quantity))
        minimum = min(quant_list)

    # Display shoe product
    for each_shoe in shoe_list:
        if minimum == int(each_shoe.quantity):
            table_data = [each_shoe.country, each_shoe.code, each_shoe.product, 
                          each_shoe.cost, each_shoe.quantity]
            print(f"\nProduct with the lowest quantity in stock:")
            print(tabulate([table_data], headers=headers, tablefmt="fancy_grid"))
            print()
            break

    while True:
        # Ask user input if they'd like to add to quantity, then validate input
        choice = input("Restock & add to quantity? (Y/N): ").strip().upper()
        if choice == "Y":
            while True:
                try:
                    add = int(input("Enter amount being added: "))
                except ValueError:
                    print("Invalid amount. Please try again.")
                    continue
                else:
                    break

            for each_shoe in shoe_list:
                if minimum == int(each_shoe.quantity):
                    each_shoe.quantity = int(each_shoe.quantity) + add
            
            # Read inventory.txt file and split into list elements
            with open("inventory.txt", "r") as file:
                updated = []
                file = file.read().splitlines()
                for each_shoe in file:
                    try:
                        shoe_list = each_shoe.strip().split(",")
                    except IndexError:
                        pass
                    
                    # Updates quantity for lowest quantity product, join list
                    # elements together, then appends to updated list
                    if table_data == shoe_list:
                        restocked = int(shoe_list[4]) + add
                        shoe_list[4] = str(restocked)
                        shoe_list = ",".join(shoe_list)
                        updated.append(shoe_list)
                    
                    else:
                        shoe_list = ",".join(shoe_list)
                        updated.append(shoe_list)
                
                # Write to file, & format correctly
                with open("inventory.txt", "w") as file:
                    final = ""
                    for each_shoe in updated:
                        final += (f"{each_shoe},")
                        final = final.rstrip(",")
                        final += "\n"
                    file.write(final)
                    print("\nSuccessfully updated quantity.\n")
            
            # Updates shoe_list variable
            if table_data == shoe_list:
                shoe_list[4] = int(shoe_list[4]) + add
                return shoe_list
                
            break

        elif choice == "N":
            break

        else:
            print("Invalid option. Please try again.")
            continue

def search_shoe():
    while True:
        search_code = input("Enter product code: ")

        # Searches for code in shoe_list. If a match, print & display product
        for each_shoe in shoe_list:
            if search_code == each_shoe.code:
                table_data = [each_shoe.country, each_shoe.code, each_shoe.product, 
                              each_shoe.cost, each_shoe.quantity]
                print()
                print(tabulate([table_data], headers=headers, tablefmt="fancy_grid"))
                print()
                break
        else:
            print("Product code not registered. Please try again.")
            continue
        break

def value_per_item():
    # Establish new headers to include Total Value column
    header = [
            "\033[1m\033[94mCountry\033[0m", 
            "\033[1m\033[94mCode\033[0m", 
            "\033[1m\033[94mProduct\033[0m", 
            "\033[1m\033[94mCost\033[0m", 
            "\033[1m\033[94mQuantity\033[0m", 
            "\033[1m\033[94mTotal Value\033[0m"
        ]

    # Create new list variable for table data
    table_data = []

    # For each shoe in shoe_list, calculate total value for each, then append
    # relevant attributes to table_data
    for each_shoe in shoe_list:
        multiplication = int(each_shoe.cost) * int(each_shoe.quantity)
    
        table_data.append([each_shoe.country, each_shoe.code, each_shoe.product, 
                   each_shoe.cost, each_shoe.quantity, (f"£{multiplication:,.2f}")])

    print()
    print(tabulate(table_data, headers=header, tablefmt="fancy_grid"))
    print()

def highest_qty():
    # Determine which shoe product has the highest quantity
    quant_list = []
    for each_shoe in shoe_list:
        quant_list.append(int(each_shoe.quantity))
        maximum = max(quant_list)

    # Display shoe product
    for each_shoe in shoe_list:
        if maximum == int(each_shoe.quantity):
            table_data = [each_shoe.country, each_shoe.code, each_shoe.product, 
                          each_shoe.cost, each_shoe.quantity]
            print(f"\nProduct with the highest quantity in stock:")
            print(tabulate([table_data], headers=headers, tablefmt="fancy_grid"))
            print("This product is for sale.\n")

#==========Main Menu=============
read_shoes_data()

while True:

    menu = input(
        "\nPlease select from the following options:"
        "\n"
        "\ncs - Enter new shoe product data"
        "\nva - Display all shoe products in stock"
        "\nrs - Display product with lowest quantity (restock)"
        "\nss - Search product by code"
        "\nvp - Display total value per product"
        "\nhq - Display product with highest quantity (sale)"
        "\ne  - Exit "
        "\n: "
    ).strip().lower()

    if menu == "cs":
        capture_shoes()

    elif menu == "va":
        view_all()

    elif menu == "rs":
        re_stock(shoe_list)

    elif menu == "ss":
        search_shoe()

    elif menu == "vp":
        value_per_item()

    elif menu == "hq":
        highest_qty()

    elif menu == "e":
        print("Goodbye")
        exit()

    else:
        print("\nInvalid option. Please try again.")
        continue