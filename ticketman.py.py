import csv
import os

FILENAME = 'train_tickets.csv'

# Create CSV file with headers if not already present
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Source', 'Destination', 'Train Number', 'Date', 'No. of Passengers'])

def buy_ticket():
    name = input("Enter passenger name: ")
    source = input("Enter source: ")
    destination = input("Enter destination: ")
    train_number = input("Enter train number: ")
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        num_passengers = int(input("Enter number of passengers: "))
    except ValueError:
        print("Invalid number. Ticket not saved.")
        return

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, source, destination, train_number, date, num_passengers])
    print("✅ Ticket booked successfully!")

def view_tickets():
    if not os.path.exists(FILENAME):
        print("No ticket records found.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        tickets = list(reader)
        if len(tickets) <= 1:
            print("No tickets available.")
            return

        print("\n🎫 Booked Tickets:")
        for row in tickets[1:]:
            print(f"Name: {row[0]}, Source: {row[1]}, Destination: {row[2]}, Train No: {row[3]}, Date: {row[4]}, Passengers: {row[5]}")

def total_collection():
    total_passengers = 0
    if not os.path.exists(FILENAME):
        print("No ticket records to calculate.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            try:
                total_passengers += int(row[5])
            except (ValueError, IndexError):
                continue

    print(f"\n👥 Total passengers booked: {total_passengers}")

def menu():
    while True:
        print("\n--- Train Management System ---")
        print("1. Buy a Ticket")
        print("2. View Tickets")
        print("3. Total Collection")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            buy_ticket()
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            total_collection()
        elif choice == '4':
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 4.")

# Start the program
if __name__ == "__main__":
    menu()
