#Tanishka Sahni - s4175835
#Part 1/2/3 Complete

#                     Part-1
#Option 1 : Make a booking
#Professionally, I learnt how to create a booking flow from beginning to end, 
# including input validation, reward point logic, and capacity checks. 
# This was on top of what I already knew about loops and dictionaries.  
# I started by drawing the design in small pieces, like "booking," "guests," and "extras." 
# Then, I put them all together one by one until they worked as a whole.  H
# andling the number of guests vs. the number of extra beds in a reasonable way was hard. 
# I solved the problem by checking the conditions again after the user entered them to stop bookings that were not valid.

def make_booking():  #    # Using a dictionary for apartments ensures easy lookup of rates and capacities by ID.
    # This reduces hard-coding and allows scalable updates.
    Guest_name = input("Enter the Guest Name(Main Guest): ")
    num_of_Guests = int(input("Enter the number of Guests : "))
    print("Names of all guests: ")
    for i in range(num_of_Guests):
        name = input(f"Enter the name of guest {i + 1}: ")
    # Store each guest's name in a list or print it directly
        print(f"Guest {i + 1}: {name}")

# Get check-in and check-out dates and length of stay
    check_in_date = input("Enter the check-in date (DD/MM/YYYY): ")
    check_out_date = input("Enter the check-out date (DD/MM/YYYY): ")
    length_of_stay = int(input("Enter the length of stay in days: "))


    booking_date = input("Enter the booking date (DD/MM/YYYY)(current date in which the booking is made): ")

#ask which apartment the guest wants to book
    appartments = {
        "U12swan": 95.0,
        "U209duck": 106.7,
        "U49goose": 145.2
    }
    print("Available apartments: ", list(appartments.keys()))
    print("Rate of each apartment: ", list(appartments.values()))
    appartment_choice = input ("Enter the appartment you want to book: ")

#Get its rate from the dictionary
    if appartment_choice in appartments:
        rate = appartments[appartment_choice]
        total_cost = rate * length_of_stay
        print("Total cost of stay is: ", total_cost, "$")
    else:
        print("Invalid apartment choice! Please select from the available apartments.")


# Calculate reward points based on total cost   
    reward_points = round(total_cost) 
    print("Reward points earned: ", reward_points)

#Existing data
    guests = {
        "Alyssa" : 20,
        "Luigi" : 32
    }
# Function to add a new guest
    def add_guest(name, points):
    # Check if the guest already exists
        if name in guests:
            guests[name] += points
            print(f"Guest {name} already exists. Update reward points: {guests[name]}")
        else:
            guests[name] = points
            print(f"Guest {name} added with {points} reward points.")

#Function to show all guest profile
    print("Guest List:", list(guests.keys()))
    add_guest(Guest_name, reward_points)
    print("\nUpdated Guest List and Profiles:")
    for guest , reward in guests.items():
        print(f"-{guest} : {reward} reward points")

# #display the booking details

    print("="*60)
    print("Debuggers Hut Serviced Apartments - Booking Receipt")
    print("="*60)
    print(f"Guest Name: {Guest_name}")
    print(f"Number of Guests: {num_of_Guests}")
    print(f"Apartment ID: {appartment_choice}")
    print(f"Check-in Date: {check_in_date}")
    print(f"Check-out Date: {check_out_date}")
    print(f"Length of Stay: {length_of_stay} days")
    print(f"Booking Date: {booking_date}")
    print("-"*50)
    print(f"Total Cost: (AUD){total_cost:.2f}")
    print(f"Reward Points Earned: {reward_points}")
    print()
    print(f"Thank you for booking! we hope you will have an enjoyable stay.")
    print("="*60)




#                     Part-2 & 3 
# Function to display supplementary items and their prices
    supplementary_items = {
        "car_park":{"price": 25.0, "unit": "per_night"},
        "breakfast":{"price": 21.0, "unit": "per_person"},
        "toothpaste":{"price": 5.0, "unit": "per_tube"},
        "extra_bed":{"price":50.0, "unit": "per_item_per_night"}
    }
    apartment_capacity = {
            "U12swan": 2,
            "U209duck": 3,
            "U49goose": 4
            } 
    base_capacity = apartment_capacity.get(appartment_choice, 0)
#function to get  valid yes/no input
    def get_yes_no_input(prompt):    # A helper function makes sure that only proper "y" or "n" input is accepted, which 
        # stops crashes and keeps user interaction predictable.
        while True:
            answer = input(prompt).strip().lower()
            if answer in ['y', 'n']:
                return answer
            else:
                print("Invalid input! Please enter 'y' or 'n'.")

#function to get a valid positive quantity
    def get_positive_quantity(prompt):
        while True:
            try:
                quantity = int(input(prompt))
                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be a positive integer. Please try again.")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

    def calc_item_cost(item_id, qty, nights):  ## This helper takes care of figuring out costs based on the type of unit. 
        # It keeps the thinking consistent by not repeating if/else in the main code.
        info = supplementary_items[item_id]
        price = info['price']
        unit = info['unit']  # e.g., 'per_item_per_night', 'per_night', 'per_person', 'per_tube'
        if unit in ("per_item_per_night", "per_night"):
            return price * qty * nights          # charges per night
        else:
            return price * qty                   # one-off


     # NEW: update/add item in selected_items cleanly
    def add_or_update_selected_item(selected_items, item_id, add_qty):
        updated = False
        new_list = []
        for it, qty in selected_items:
            if it == item_id:
                new_list.append((it, qty + add_qty))
                updated = True
            else:
                new_list.append((it, qty))
        if not updated:
            new_list.append((item_id, add_qty))
        return new_list

    answer = input("Do you want to add any supplementary items? (y/n)")

    selected_items = []          # FIX: define before both branches
    total_supplementary_cost = 0.0
    extra_bed_qty = 0 
    
    if answer == 'y':
        print("Available supplementary items:")
        for item, details in supplementary_items.items():
            print(f"{item.capitalize()}: ${details['price']} {details['unit']}")
        while True:
            item_choice = input("Enter the name of the supplementary item you want to add (or type 'done' to finish): ").lower()
            if item_choice == 'done':
                break
            if item_choice not in supplementary_items:
                print("Invalid item choice! Please try again.")
                continue

            show_item_price(item_choice)
            quantity = int(input(f"How many {item_choice} do you want to add? "))
            
            confirm_item = get_yes_no_input(f"Confirm order: {quantity} x {item_choice}? (y/n): ")
            if confirm_item != "y":
                print(f"{item_choice} not added.")
                continue

            price = supplementary_items[item_choice]["price"]
            cost = calc_item_cost(item_choice, quantity, length_of_stay)   # FIX
            total_supplementary_cost += cost                                # FIX
            selected_items.append((item_choice, quantity))
            if item_choice == "extra_bed":
                extra_bed_qty += quantity
                total_supplementary_cost += price * quantity * length_of_stay  # FIX: multiply by nights
            else:
                total_supplementary_cost += price * quantity    

        # ---- AFTER 'done': capacity re-check if user didn't add enough extra beds ----
        effective_capacity = base_capacity + 2 * extra_bed_qty
        if num_of_Guests > effective_capacity:
            print("Warning: your guest count exceeds the apartment capacity.")
            print(f"Current capacity (beds): {effective_capacity} (base {base_capacity} + {2*extra_bed_qty} via extra beds)")

            remaining_beds_allowed = 2 - extra_bed_qty
            if remaining_beds_allowed <= 0:
                print("You already reached the maximum of 2 extra beds. Booking cannot proceed.")
                return

            want_more = get_yes_no_input(f"Do you want to add up to {remaining_beds_allowed} more extra bed(s)? (y/n): ")
            if want_more == 'y':
                add_qty = get_positive_quantity(f"How many extra beds to add (max {remaining_beds_allowed}): ")
                if add_qty > remaining_beds_allowed:
                    print(f"Error: You can add at most {remaining_beds_allowed} more extra bed(s). Booking cannot proceed.")
                    return

                show_item_price("extra_bed")
                if get_yes_no_input(f"Confirm order: {add_qty} x extra_bed? (y/n): ") != 'y':
                    print("Extra beds not added. Booking cannot proceed.")
                    return

                # Add the extra beds & cost delta
                delta_cost = calc_item_cost("extra_bed", add_qty, length_of_stay)
                total_supplementary_cost += delta_cost
                extra_bed_qty += add_qty
                selected_items = add_or_update_selected_item(selected_items, "extra_bed", add_qty)

                # Recheck capacity
                effective_capacity = base_capacity + 2 * extra_bed_qty
                if num_of_Guests > effective_capacity:
                    print("Guests still exceed capacity even after adding extra beds. Booking cannot proceed.")
                    return
            else:
                print("Guests exceed capacity and no extra beds selected. Booking cannot proceed.")
                return
            
    elif answer == 'n':
        base_capacity = apartment_capacity.get(appartment_choice, 0)
        if num_of_Guests > base_capacity:
            print("Warning: please consider ordering an extra bed.")
            print(f"Current capacity (beds): {base_capacity}, Guests: {num_of_Guests}")
        # Ask for extra beds (max 2)
            extra_bed_info = supplementary_items["extra_bed"]
            print(f"Each 'extra_bed' adds 2 to capacity. Unit price: ${extra_bed_info['price']:.2f} ({extra_bed_info['unit']})")
            confirm = get_yes_no_input("Do you want to order extra beds? (y/n): ")
            if confirm == "y":
                extra_bed_qty = get_positive_quantity("Enter quantity of extra beds (max 2): ")
                if extra_bed_qty > 2:
                    print("Error: Maximum of 2 extra beds allowed. Booking cannot proceed. Returning to main menu.")
                    return
                # Confirm order
                show_item_price("extra_bed")
                confirm2 = get_yes_no_input(f"Confirm order: {extra_bed_qty} x extra_bed? (y/n): ")
                if confirm2 != "y":
                    print("Extra bed not added. Booking cannot proceed.")
                    return
                    # extra_bed_qty = 0  # canceled
                effective_capacity = base_capacity + (2 * extra_bed_qty)
                if num_of_Guests > effective_capacity:
                    print("Guests still exceed the capacity even after extra beds. Booking cannot proceed.")
                    return
                
                price_eb = supplementary_items["extra_bed"]["price"]
                eb_cost = calc_item_cost("extra_bed", extra_bed_qty, length_of_stay)   # FIX
                total_supplementary_cost += eb_cost   
                selected_items.append(("extra_bed", extra_bed_qty))

            else:
                # No extra beds ordered, capacity still insufficient -> cannot proceed
                print("Guests exceed capacity and extra beds not ordered. Booking cannot proceed.")
                return
        else:
            print("Capacity is sufficient. Proceeding without supplementary items.")
    else:
        print("Invalid choice, please enter 'y' or 'n'. ")
        return



    pre_deduction_total = total_cost + total_supplementary_cost
    print(f"Total cost for supplementary items: ${total_supplementary_cost:.2f}")   
    print(f"Pre-Deduction Total: (AUD){pre_deduction_total:.2f}") 
        
# Final total cost including supplementary items

    # --- Reward points redemption (based on current points BEFORE this booking) ---
    current_points = guests.get(Guest_name, 0)
    print(f"\nCurrent reward points for {Guest_name}: {current_points}")
    final_total_cost = pre_deduction_total
    points_spent = 0
    if current_points >= 100 and get_yes_no_input("Would you like to spend your reward points? (y/n): ")== "y":
            max_blocks_by_points = current_points // 100
            max_blocks_by_total = int(pre_deduction_total // 10)
            blocks = min(max_blocks_by_points, max_blocks_by_total)
            deduction = blocks * 10.0
            points_spent = blocks * 100
            final_total_cost = pre_deduction_total - deduction
            print(f"Applied ${deduction:.2f} discount using {points_spent} points.")
    else:
        print("No points spent.")

    print(f"Final total cost including supplementary items: ${final_total_cost:.2f}")


    # Earned reward points are based on pre-deduction total
    earned_reward_points = round(pre_deduction_total)
    new_points_balance = current_points - points_spent + earned_reward_points
    add_or_set_guest_points(Guest_name, new_points_balance)

    # --- Store order into history ---
    order_items_for_history = [(appartment_choice, length_of_stay)] + selected_items
    push_order_history(
        Guest_name,
        order_items_for_history,
        pre_deduction_total,
        earned_reward_points
    )

# Update guest profile with new reward points
    print("Guest List:", list(guests.keys()))
    new_reward_points = reward_points + round(total_supplementary_cost)
    add_guest(Guest_name, new_reward_points)
# Display updated guest profile
    print("\nUpdated Guest List and Profiles after adding supplementary items:")
    for guest, reward in guests.items():
        print(f"- {guest}: {reward} reward points")

# Display final booking receipt
    print("="*60)
    print("Debuggers Hut Serviced Apartments - Final Booking Receipt")
    print("="*60)
    print(f"Guest Name: {Guest_name}")
    print(f"Number of Guests: {num_of_Guests}")
    print(f"Apartment ID: {appartment_choice}")
    print(f"Check-in Date: {check_in_date}")
    print(f"Check-out Date: {check_out_date}")
    print(f"Length of Stay: {length_of_stay} days")
    print(f"Booking Date: {booking_date}")
    print("-"*50)
    print(f"Apartment Cost: (AUD){(rate * length_of_stay):.2f}")
    if extra_bed_qty > 0:
        print(f"Extra Beds Cost: (AUD){supplementary_items['extra_bed']['price'] * extra_bed_qty * length_of_stay:.2f}")
        print(f"Other Supplements Cost: (AUD){(total_supplementary_cost - (supplementary_items['extra_bed']['price'] * extra_bed_qty * length_of_stay) if extra_bed_qty>0 else total_supplementary_cost):.2f}")
        print(f"Pre-Deduction Total: (AUD){pre_deduction_total:.2f}")
        print()
    if 'selected_items' in locals() and selected_items:
        print("Supplementary items:")
        for item, quantity in selected_items:
            print(f"Item id: {item}")
            print(f"Quantity: {quantity}")
            print(f"Price: ${supplementary_items[item]['price']:.2f}")
            print(f"Cost: ${supplementary_items[item]['price'] * quantity:.2f}")
            print()
    else: 
            print("No supplementary items selected.")
    print("."*3)
    print()
    print(f"Sub-total : ", total_supplementary_cost)
    print(f"Earned Reward Points (based on pre-deduction): {earned_reward_points}")
    if points_spent > 0:
        print(f"Points Spent: {points_spent}")
        print(f"Total After Points Deduction: (AUD){final_total_cost:.2f}")
    else:
        print(f"Total (No Deduction): (AUD){final_total_cost:.2f}")
    print(f"New Points Balance: {new_points_balance}")
    print("-"*50)
    print(f"Total Cost: (AUD){final_total_cost:.2f}")
    print(f"Reward Points Earned: {new_reward_points}")
    print()
    print(f"Thank you for booking! we hope you will have an enjoyable stay.")
    print("="*60)
# End of the booking system code

#Option 2 : Add/Update Apartment
guests = {"Alyssa": 20, "Luigi": 32}                 # name -> points
appartments = {"U12swan": (95.0, 2),
              "U209duck": (106.7, 3),
              "U49goose": (145.2, 4)}                # id -> (rate, capacity)
apartment_capacity = {
    "U12swan": 2,
    "U209duck": 3,
    "U49goose": 4
} 
supplementary_items = {
    "car_park":   {"price": 25.0, "unit": "per_night"},
    "breakfast":  {"price": 21.0, "unit": "per_person"},
    "toothpaste": {"price": 5.0,  "unit": "per_tube"},
    "extra_bed":  {"price": 50.0, "unit": "per_item_per_night"}
}

order_history = {}

def valid_apartment_id(ap_id):
    """Apartment ID must start with 'U', followed by digits, then letters (e.g., U12swan)."""
    if not ap_id.startswith("U"):
        return False
    digits = ""
    letters = ""
    for ch in ap_id[1:]:
        if ch.isdigit() and not letters:
            digits += ch
        else:
            letters += ch
    return (digits.isdigit() and digits != "") and (letters.isalpha() and letters != "")


def add_update_apartment():  # Checks the shape of the apartment ID so that keys in the dictionary don't become confused.
    raw = input("Enter apartment info (apartment_id rate capacity): ")
    parts = raw.split()  # handles multiple spaces automatically
    if len(parts) != 3:
        print("Invalid input format! Example: U12swan 120.0 3")
        return
    ap_id, rate_str, cap_str = parts[0], parts[1], parts[2]

    if not valid_apartment_id(ap_id):
        print("Invalid apartment id format! Example: U12swan")
        return

    try:
        rate = float(rate_str)
        capacity = int(cap_str)
        appartments[ap_id] = (rate, capacity)
        print(f"Apartment {ap_id} saved with rate {rate} and capacity {capacity}.")
    except ValueError:
        print("Rate must be a number and capacity must be an integer. Change not saved.")

#Option 3 : Add/Update Supplementary Item
def add_update_supplementary_item():
    raw = input("Enter supplementary item info (id price), e.g., 'toothpaste   5.2': ").strip()
    parts = raw.split()  # allows multiple whitespaces
    if len(parts) != 2:
        print("Incorrect format. Change not saved; returning to main menu.")
        return

    item_id, price_str = parts[0].lower(), parts[1]
    try:
        price = float(price_str)
        if price <= 0:
            print("Price must be a positive number. Change not saved.")
            return
    except ValueError:
        print("Price must be a valid number. Change not saved.")
        return

    # If item exists, update price; else add new
    if item_id in supplementary_items:
        supplementary_items[item_id]["price"] = price
        print(f"Updated '{item_id}' price to ${price:.2f}.")
    else:
        supplementary_items[item_id] = {"price": price, "unit": "each"}
        print(f"Added new item '{item_id}' with price ${price:.2f}.")

#Option 4/5/6 : Display Guests/ Apartments/ Supplementary Items
def display_guests():
    if not guests:
        print("No guests found.")
        return
    print("\n--- Guests and Reward Points ---")
    for g, p in guests.items():
        print(f"{g}: {p} points")

def display_apartments():
    if not appartments:
        print("No apartments found.")
        return
    print("\n--- Apartment Units ---")
    for ap_id, (rate, cap) in appartments.items():
        print(f"{ap_id}: Rate ${rate} / night, Capacity {cap} beds")

def display_supp_items():
    if not supplementary_items:
        print("No supplementary items found.")
        return
    print("\n--- Supplementary Items ---")
    for it, info in supplementary_items.items():
        print(f"{it}: ${info['price']} ({info['unit']})")

def add_or_set_guest_points(name, new_points):
    """Set guest points (create if new)."""
    guests[name] = new_points

def ensure_guest_exists(name):
    if name not in guests:
        guests[name] = 0

def push_order_history(guest_name, items_list, total_cost, earned_points):   
    # To make it easy to find and expand later, order information is saved as a list of dicts for each guest.
    """Append an order to history."""
    if guest_name not in order_history:
        order_history[guest_name] = []
    order_history[guest_name].append({
        "list": items_list,  # list of tuples (item_id, qty)
        "total_cost": total_cost,
        "earned_rewards": earned_points
    })

def show_apartment_price(ap_id):
    """Auto-display apartment price when ID entered (if valid)."""
    rate = appartments.get(ap_id)
    if rate is not None:
        print(f"Rate per night for {ap_id}: ${rate:.2f}")

def show_item_price(item_id):
    """Auto-display supplementary item price when ID entered (if valid)."""
    info = supplementary_items.get(item_id)
    if info is not None:
        print(f"Price for {item_id}: ${info['price']:.2f} ({info['unit']})")

#Menu 
def menu():
    while True:    ## A while loop was used to keep the menu open until the user closed it.
         # This design avoids recursion or multiple calls, which keeps the flow simple and under control.
        print("\n===== Apartment Booking System Menu =====")
        print("1. Make a booking")
        print("2. Add/Update Apartment Information")
        print("3. Add/Update Supplementary Item")
        print("4. Display Existing Guests")
        print("5. Display Existing Apartments")
        print("6. Display Existing Supplementary Items")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            make_booking()
        elif choice == "2":
            add_update_apartment()
        elif choice == "3":
            add_update_supplementary_item()
        elif choice == "4":
            display_guests()
        elif choice == "5":
            display_apartments()
        elif choice == "6":
            display_supp_items()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

# Run
if __name__ == "__main__":
    menu()

