import sys

# Data structure to store purchases
purchases = []

def add_purchase():
    website = input("Enter the website (e.g., Amazon, eBay): ")
    category = input("Enter the category (e.g., Electronics, Books): ")
    item = input("Enter the item name: ")
    price = float(input("Enter the price: $"))
    purchases.append({'website': website, 'category': category, 'item': item, 'price': price})
    print(f"Added purchase: {item} for ${price} under {category} from {website}.\n")

def view_purchases():
    print("All Purchases:")
    for purchase in purchases:
        print(f"{purchase['item']} from {purchase['website']} in {purchase['category']} - ${purchase['price']}")
    print()

def total_spending():
    total = sum(purchase['price'] for purchase in purchases)
    print(f"Total Spending: ${total}\n")

def spending_by_category():
    from collections import defaultdict
    category_totals = defaultdict(float)
    for purchase in purchases:
        category_totals[purchase['category']] += purchase['price']
    
    print("Spending by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total}")
    print()

def main_menu():
    while True:
        print("Amazon Spending Tracker Main Menu")
        print("1. Add a purchase")
        print("2. View all purchases")
        print("3. View total spending")
        print("4. View spending by category")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_purchase()
        elif choice == '2':
            view_purchases()
        elif choice == '3':
            total_spending()
        elif choice == '4':
            spending_by_category()
        elif choice == '5':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
