# HomyHub 🏡  
HomyHub is a property management system that allows users to list, browse, and review places. It features a command-line interface (CLI) for easy management and a structured data storage system.

## 📌 Features
- ✅ Object-Oriented Programming (OOP) with Python
- ✅ Command-line interface for managing properties and users
- ✅ JSON-based storage system
- ✅ User authentication and session management
- ✅ CRUD operations for places, amenities, users, and reviews

## 📂 Project Structure
bash
Copy
Edit
HomyHub/
- │── models/              # Data models for users, places, reviews, etc.
- │   ├── base_model.py    # Base class for all models
- │   ├── user.py          # User model
- │   ├── state.py         # State model
- │   ├── city.py          # City model
- │   ├── amenity.py       # Amenity model
- │   ├── place.py         # Place model
- │   ├── review.py        # Review model
- │── console.py           # Command-line interface for managing the app
- │── tests/               # Unit tests
- │── README.md            # Project documentation
- │── requirements.txt     # Python dependencies
- └── setup.py             # Setup script
## ⚙️ Installation & Setup
- 1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/ngush67/HomyHub.git
cd HomyHub
- 2️⃣ Create a virtual environment (Recommended)
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
- 3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
- 4️⃣ Run the console
bash
Copy
Edit
./console.py
or

bash
Copy
Edit
python3 console.py
## 🛠 Usage
The console allows you to interact with the models using commands:

Start the Console
bash
Copy
Edit
./console.py
Available Commands
Command	Description
help	Show available commands
create <ModelName>	Create a new object
show <ModelName> <id>	Show object details
update <ModelName> <id>	Update object attributes
destroy <ModelName> <id>	Delete an object
all <ModelName>	Show all objects of a model
quit or EOF	Exit the console
## 🧪 Running Tests
To run unit tests, use:

bash
Copy
Edit
python3 -m unittest discover tests
## 🚀 Contributing
Fork the repo
Create a new branch (git checkout -b feature-branch)
Make your changes
Commit your changes (git commit -m "Added new feature")
Push to the branch (git push origin feature-branch)
Open a Pull Request
