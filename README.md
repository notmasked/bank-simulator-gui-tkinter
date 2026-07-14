# Local Bank

Local Bank is a Python desktop application built with Tkinter that simulates basic banking operations through a graphical user interface.

## Features

* User registration and login system
* Secure PIN hashing using SHA-256
* Deposit and withdraw money
* Transfer funds between accounts
* Persistent account data storage
* Input validation and error handling
* Multi-screen GUI navigation

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the source code.
3. Install the required dependency:

```bash
pip install Pillow
```

4. Open a terminal in the project folder.
5. Run:

```bash
python main.py
```

## Usage

* Register a new account or log in.
* Deposit, withdraw, or transfer funds.
* All account data is saved automatically.

## Project Structure

```text
local-bank/
│
├── main.py
├── README.md
├── LICENSE
│
├── assets/
│   └── icon.png
│
└── data/
    └── accounts.txt
```

## Files

* `main.py` – Application source code
* `assets/icon.png` – Application icon
* `data/accounts.txt` – Stores account information

## Author

**Harshad Sawant**

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
