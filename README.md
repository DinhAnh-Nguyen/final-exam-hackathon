# final-exam-hackathon
**Smart Parking Allocation System**
***Project Description***
- With this application, you can find beforehand whichever parking lot is available and most suits to you, and you can assigning and reserve your vehicle to that parking spot.

***Programming language Choice and Justification***
- We choose Python because it is the language that we are most comfortable with

***System Design Overview***
- Class:
  - Vehicle
  - ParkingSpot
  - ParkingLot
  - User
- ParkingSpot belongs to ParkingLot. It is the spots inside each lot.
- License plate number is the reference data, used to view registrations and release spots.
- The main() function holds the UI and leads the users on what to do next, followed by standalone functions and classes

***Description of parallel component***
- With the intention of applying ThreadPoolExecution, users can use the application simultaneously and data will update corresponding with multiple requests at once.

***Exception handling strategy***
- KeyboardInterrupt, EOFError: On my laptop, I keep having the KeyboardInteruppt problem, so I add these exception handles to return to main menu when it happens again.
- Invalid match case input handling (e.g. I have 4 options for 4 different functions on the UI, but I click "a".)

***Instructions to run the program***
- Create a virtual environment: python -m venv .venv
- Run: .venv\Scripts\activate (Windows) or source .venv/bin/activate (macOS/Linux)
- Instal dependencies: pip install -r requirements.txt
- Run the program: python main.py
