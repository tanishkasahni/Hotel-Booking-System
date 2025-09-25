Apartment Booking System 🏠

Overview
This project is a Python-based apartment booking system, developed as part of my Programming Fundamentals assignment.
The system simulates a real-world booking process by allowing guests to select apartments, enter stay details, and confirm their booking.
I approached this project by first breaking the requirements into small modules such as guest details, booking dates, apartment selection, and reward handling. After carefully designing each part, I combined them to create a smooth end-to-end booking flow.

⚙️ Features
Guest Management: Collects details of the main guest and additional guests.
Booking Details: Takes check-in and check-out dates, along with stay duration.
Apartment Selection: Provides a list of apartments with rates and validates the choice.
Input Validation: Prevents invalid bookings by checking guest numbers, dates, and room selections.
Scalable Design: Uses data structures that make updating apartment details easy.
Reward Logic (if extended): Tracks customer reward points for repeated bookings.

🧑‍💻 How It Works
The system first asks for the main guest name and the number of guests.
It records each guest’s name to maintain booking records.
The user provides stay dates, length of stay, and booking date.
A list of available apartments with their rates is displayed.
The guest selects an apartment, and the booking is confirmed with validation checks.

📖 What I Learned
Through this project, I learned to:
Break a large problem into smaller manageable steps and functions.
Use loops and dictionaries to store and process booking data.
Apply input validation to prevent invalid or unrealistic entries.
Solve real-world challenges like handling guest capacity vs. extra beds.
Build a structured program where each part works independently but integrates smoothly.

✅ Future Improvements
Introduce persistent storage to save booking records for later retrieval.
Add advanced validation for dates using Python’s datetime module.
Expand the reward system with discounts or loyalty benefits.
Improve the user interface for a smoother booking experience.
