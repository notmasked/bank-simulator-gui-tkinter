from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import hashlib

#ACCOUNTS
account_data = "data/accounts.txt"
accounts = []

class User():
    def __init__(self, name, number, pin, balance):
        self.name = name
        self.number = number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance = int(self.balance)
        self.balance += amount
        updatedata()

    def withdraw(self, amount):
        self.balance = int(self.balance)
        self.balance -= amount
        updatedata()

    def transfer(self, amount, payee):
        self.balance = int(self.balance)
        payee.balance = int(payee.balance)
        self.balance -= amount
        payee.balance += amount
        updatedata()

def limit(num):
    if num == "" or (len(num) <= 4 and num.isdigit()):
        return True
    else:
        return False

def updatedata():
    with open(account_data, "w") as f:
        for acc in accounts:
            f.write(f"{acc.name},{acc.number},{acc.pin},{acc.balance}\n")

def hashpin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

def refreshdata():
    accounts.clear()
    with open(account_data) as f:
        for line in f:
            line = line.strip()
            data = line.split(",")
            account = User(data[0],data[1],data[2],data[3])
            accounts.append(account)
refreshdata()

def updateinfo():
    global user
    showBalance.config(text=f"Your available balance is {user.balance}$")

def showframe(frame):
    screens = [homeScreen, loginScreen, registerScreen, depositScreen, withdrawScreen, transferScreen]
    for screen in screens:
        screen.pack_forget()
    frame.pack(fill='both', expand=True)
#WINDOW
window = Tk()
window.title("Local Bank")
window.resizable(False, False)
window.geometry("360x360")
icon = PhotoImage(file="assets/icon.png")
window.iconphoto(True, icon)

#REGISTER
def namelimit(name):
    if name == "" or (name.isalpha() and len(name)<=10):
        return True
    else:
        return False

registerScreen = Frame(window)

def register():
    if len(pinEntry.get()) < 4 or len(confirmPinEntry.get()) < 4:
        regError.config(text="PIN must be 4 digit.")
    elif pinEntry.get() == confirmPinEntry.get():
        name = userEntry.get()
        pin = hashpin(pinEntry.get())
        if len(accounts) == 0:
            number = 1000
        else:
            number = int((accounts[-1]).number) + 1
        with open(account_data, 'a') as f:
            f.write(f"{name},{str(number)},{pin},0\n")
        refreshdata()
        showframe(loginScreen)
        userEntry.delete(0, END)
        pinEntry.delete(0, END)
        confirmPinEntry.delete(0, END)
        logAccNumDisplay.config(text=f"Your account number is {number}.")
    else:
        regError.config(text="Both PINs do not match. Try again.")

    

regPin_cmd = registerScreen.register(limit)
regName_cmd = registerScreen.register(namelimit)

registerTitle = Label(registerScreen,
                      text="Register",
                      font=('segoe ui', 15, 'bold'),
                      padx=10,
                      pady=10)
userPrompt = Label(registerScreen,
                   text="Name",
                   font=('segoe ui', 12))
userEntry = Entry(registerScreen,
                  width=11,
                  validate='key', validatecommand=(regName_cmd, "%P"))
pinPrompt = Label(registerScreen,
                  text="Set PIN",
                  font=('segoe ui', 12))
pinEntry = Entry(registerScreen,
                 width=11, show="*", validate='key', validatecommand=(regPin_cmd, "%P"))
confirmPinPrompt = Label(registerScreen,
                  text="Confirm PIN",
                  font=('segoe ui', 12))
confirmPinEntry = Entry(registerScreen, width=11, show="*", validate='key', validatecommand=(regPin_cmd, "%P"))
regButton = Button(registerScreen, text="Register", command=register)
regError = Label(registerScreen, text="", font=('segoe ui', 8), fg='red')

registerTitle.place(relx=0.5, y=5, anchor='n')
userPrompt.place(relx=0.2, y=79, anchor='w')
userEntry.place(relx=0.75, y=71, anchor='n')
pinPrompt.place(relx=0.2, y=139, anchor='w')
pinEntry.place(relx=0.75, y=131, anchor='n')
confirmPinPrompt.place(relx=0.2, y=199, anchor='w')
confirmPinEntry.place(relx=0.75, y=191, anchor='n')
regButton.place(relx=0.5, y=240, anchor='n')
regError.place(relx=0.5, y=225, anchor='center')

#LOGIN
user = None
def login():
    global user
    number = accNumEntry.get()
    for i in accounts:
        if number == i.number:
            if hashpin(accPinEntry.get()) == i.pin:
                user = i
                welcome.config(text=f"Welcome {i.name}!")
                showBalance.config(text=f"Your available balance is {i.balance}$")
                showframe(homeScreen)
                break
            else:
                loginError.config(text="Entered PIN is incorrect. Please try again.")
                break
    else:
        loginError.config(text="Account number is invalid.")

loginScreen = Frame(window)

logPin_cmd = loginScreen.register(limit)
logAcc_cmd = loginScreen.register(limit)

loginTitle = Label(loginScreen,
                   text="Welcome to Local Bank",
                   relief=RIDGE,
                   bd=2,
                   font=('segoe ui', 15, 'bold'),
                   padx=10,
                   pady=10)
accNumEntry = Entry(loginScreen, width=8, font=('segoe ui', 12),
                    validate='key', validatecommand=(logAcc_cmd, "%P"))
accPinEntry = Entry(loginScreen, width=8, show="*", font=('segoe ui', 12),
                     validate='key', validatecommand=(logPin_cmd, "%P"))
loginButton = Button(loginScreen,
                     text="Login",
                     command=login)
enterAccNum = Label(loginScreen,
                    text="Account number",
                    font=('segoe ui', 12))
enterAccPin = Label(loginScreen,
                    text="PIN",
                    font=('segoe ui', 12))
loginError = Label(loginScreen,
                   text="",
                   font=('segoe ui', 9),
                   fg='red')
registerPrompt = Label(loginScreen,
                       text="Don't have an account?",
                       font=('segoe ui', 10))
logRegbutton = Button(loginScreen,
                        text="Register",
                        command=lambda: showframe(registerScreen))
logAccNumDisplay = Label(loginScreen, text="", font=('segoe ui', 9), fg='green')

loginTitle.place(relx=0.5, y=5, anchor='n')
enterAccNum.place(relx=0.15, y=90)
accNumEntry.place(relx=0.625, y=90)
enterAccPin.place(relx=0.15, y=150)
accPinEntry.place(relx=0.625, y=150)
loginButton.place(relx=0.5, y=210, anchor='n')
loginError.place(relx=0.5, y=65, anchor='n')
registerPrompt.place(relx=0.5, y=240, anchor='n')
logRegbutton.place(relx=0.5, y=265, anchor='n')
logAccNumDisplay.place(relx=0.5, y= 180, anchor='n')

#DEPOSIT
def validateamount(amount):
    if (amount.isdigit() and len(amount) <= 8) or amount == "":
        return True
    else:
        return False

depositScreen = Frame(window)

def deposit():
    global user
    amount = depAmountEntry.get()
    if amount == "":
        depositMessage.config(text="Please enter an amount to deposit.", fg='red')
    else:
        amount = int(depAmountEntry.get())
        if amount == 0:
            depositMessage.config(text="Please enter a valid amount.", fg='red')
        else:
            user.deposit(amount)
            depAmountEntry.delete(0, END)
            depositMessage.config(text=f"Amount of ${amount} has successfully been deposited to your account {user.number}.\nYour current balance is ${user.balance}", fg='green')
            updateinfo()

dep_amt_cmd = depositScreen.register(validateamount)

def depHomeBut():
    showframe(homeScreen)
    depositMessage.config(text="")
    depAmountEntry.delete(0, END)

depositTitle = Label(depositScreen,
                      text="Deposit",
                      font=('segoe ui', 15, 'bold'),
                      padx=10,
                      pady=10)
depAmountPrompt = Label(depositScreen,
                     text="Deposit Amount",
                     font=('segoe ui', 12))
depAmountEntry = Entry(depositScreen, width=9, validate='key', validatecommand=(dep_amt_cmd, "%P"))
depDollarSign = Label(depositScreen,
                   text="$")
depositButton = Button(depositScreen, text="Deposit", command=deposit)
depositMessage = Label(depositScreen,
                       text="", font=('segoe ui', 10), wraplength=300, fg='green')
depHomeButton = Button(depositScreen, text="Home", command=depHomeBut)

depositTitle.place(relx=0.5, y=5, anchor='n')
depAmountPrompt.place(relx=0.5, y=90, anchor='n')
depAmountEntry.place(relx=0.503, y=140, anchor='n')
depDollarSign.place(relx=0.403, y=139, anchor='n')
depositButton.place(relx=0.5, y=180, anchor='n')
depositMessage.place(relx=0.5, y=220, anchor='n')
depHomeButton.place(relx=0.1, y=5, anchor='n')

#WITHDRAW
withdrawScreen = Frame(window)

with_amt_cmd = withdrawScreen.register(validateamount)

def withdraw():
    amount = withAmountEntry.get()
    if amount == "":
        withdrawMessage.config(text="Please enter an amount to withdraw", fg='red')
    else:
        amount = int(amount)
        if amount > int(user.balance):
            withdrawMessage.config(text="Insufficient funds.", fg='red')
        elif amount == 0:
            withdrawMessage.config(text="Please enter a valid amount.", fg='red')
        else:
            user.withdraw(amount)
            withAmountEntry.delete(0, END)
            withdrawMessage.config(text=f"Amount of ${amount} has successfully been withdrawn from your account {user.number}.\nYour current balance is ${user.balance}", fg='green')
            updateinfo()

def withHomeBut():
    showframe(homeScreen)
    withdrawMessage.config(text="")
    withAmountEntry.delete(0, END)

withdrawTitle = Label(withdrawScreen,
                      text="Withdraw",
                      font=('segoe ui', 15, 'bold'),
                      padx=10,
                      pady=10)
withAmountPrompt = Label(withdrawScreen,
                     text="Withraw Amount",
                     font=('segoe ui', 12))
withAmountEntry = Entry(withdrawScreen, width=9, validate='key', validatecommand=(with_amt_cmd, "%P"))
withDollarSign = Label(withdrawScreen,
                   text="$")
withdrawButton = Button(withdrawScreen, text="Withdraw", command=withdraw)
withdrawMessage = Label(withdrawScreen,
                       text="", font=('segoe ui', 10), wraplength=300)
withHomeButton = Button(withdrawScreen, text="Home", command=withHomeBut)

withdrawTitle.place(relx=0.5, y=5, anchor='n')
withAmountPrompt.place(relx=0.5, y=90, anchor='n')
withAmountEntry.place(relx=0.503, y=140, anchor='n')
withDollarSign.place(relx=0.403, y=139, anchor='n')
withdrawButton.place(relx=0.5, y=180, anchor='n')
withdrawMessage.place(relx=0.5, y=220, anchor='n')
withHomeButton.place(relx=0.1, y=5, anchor='n')

#TRANSFER

transferScreen = Frame(window)

def searchPayee():
    global user
    payeeNum = transPayeeEntry.get()
    if payeeNum == user.number:
        transSearchResult.config(text="You can't transfer money to yourself, try deposit instead.", fg='red')
    else:
        for acc in accounts:
            if payeeNum == acc.number:
                transferMessage.place_forget()
                transSearchResult.config(text=f"You are transfering money to {acc.name}.", fg='black')
                transAmountEntry.place(relx=0.65, y=200, anchor='n')
                transAmountPrompt.place(relx=0.325, y=199, anchor='n')
                transDollarSign.place(relx=0.5259, y=199)
                transferButton.place(relx=0.5, y=235, anchor='n')
                break
        else:
            transAmountEntry.place_forget()
            transAmountPrompt.place_forget()
            transDollarSign.place_forget()
            transferButton.place_forget()
            transferMessage.place_forget()
            transSearchResult.config(text="Payee not found. Check account number.", fg='red')

def transfer():
    global user
    transferMessage.place(relx=0.5, y=270, anchor='n')
    payeeNum = transPayeeEntry.get()
    amount = transAmountEntry.get()
    if amount == "":
        transferMessage.config(text="Please enter an amount to transfer.", fg='red')
    else:
        user.balance = int(user.balance)
        amount = int(transAmountEntry.get())
        if amount > user.balance:
            transferMessage.config(text="Insufficient funds.", fg='red')
        elif amount == 0:
            transferMessage.config(text="Please enter a valid amount to transfer.", fg='red')
        else:
            for acc in accounts:
                if payeeNum == acc.number:
                    payee = acc
                    break
            user.transfer(amount, payee)
            updateinfo()
            transAmountEntry.delete(0, END)
            transPayeeEntry.delete(0, END)
            transSearchResult.place_forget()
            transAmountEntry.place_forget()
            transAmountPrompt.place_forget()
            transferButton.place_forget()
            transDollarSign.place_forget()
            transferMessage.config(text=f"Amount of ${amount} has been successfully transferred to {payee.name}.\nYour current balance is ${user.balance}", fg='green')

trans_acc_cmd = transferScreen.register(limit)
trans_amt_cmd = transferScreen.register(validateamount)

def transHomeBut():
    showframe(homeScreen)
    transferMessage.config(text="")

transferTitle = Label(transferScreen,
                      text="Transfer",
                      font=('segoe ui', 15, 'bold'),
                      padx=10,
                      pady=10)
transSearchPrompt = Label(transferScreen,
                          text="Search payee by account number",
                          font=('segoe ui', 10), wraplength=120)
transPayeeEntry = Entry(transferScreen,
                        width=8, validate='key', validatecommand=(trans_acc_cmd, "%P"))
transSearchButton = Button(transferScreen,
                           text="Search", command=searchPayee)
transSearchResult = Label(transferScreen,
                          text="",
                          font=('segoe ui', 10), wraplength=250)
transAmountEntry = Entry(transferScreen, width=9, validate='key', validatecommand=(trans_amt_cmd, "%P"))
transAmountPrompt = Label(transferScreen, text="Transfer amount",
                          font=('segoe ui', 10))
transDollarSign = Label(transferScreen,
                   text="$")
transferButton = Button(transferScreen, text="Transfer", command=transfer)
transferMessage = Label(transferScreen,
                        text="",
                        font=('segoe ui', 10), wraplength=250, fg='green')
transHomeButton = Button(transferScreen, text="Home", command=transHomeBut)

transferTitle.place(relx=0.5, y=5, anchor='n')
transSearchPrompt.place(relx=0.2, y=70)
transPayeeEntry.place(relx=0.6, y=80)
transSearchButton.place(relx=0.5, y= 120, anchor='n')
transSearchResult.place(relx=0.5, y=160, anchor='n')
transHomeButton.place(relx=0.1, y=5, anchor='n')

#LOGOUT
def logout():
    global user
    user = None
    accNumEntry.delete(0, END)
    accPinEntry.delete(0, END)
    logAccNumDisplay.config(text="")
    showframe(loginScreen)

#HOMESCREEN

homeScreen = Frame(window)
logo = Image.open("assets/icon.png")
logo = logo.resize((25,25))
logo = ImageTk.PhotoImage(logo)
title = Label(homeScreen,
              font=('times new roman', 20),
              text=" Local Bank",
              image=logo,
              compound='left',
              relief=RIDGE,
              bd=2,
              padx=10,
              pady=10)
welcome = Label(homeScreen,
                font=('segoe ui', 14, 'bold'),
                text="")
showBalance = Label(homeScreen,
                    font=('segoe ui', 12),
                    text="")
homeDepButton = Button(homeScreen,
                       font=('segoe ui', 10), text="Deposit", command=lambda: showframe(depositScreen))
homeWithButton = Button(homeScreen,
                       font=('segoe ui', 10), text="Withdraw", command=lambda: showframe(withdrawScreen))
homeTransButton = Button(homeScreen,
                         font=('segoe ui', 10), text="Transfer", command=lambda: showframe(transferScreen))
homelogoutButton = Button(homeScreen,
                          font=('segoe ui', 10), text="Logout", command=logout)

title.place(relx=0.5, y=20, anchor='n')
welcome.place(relx=0.5, y=85, anchor='n')
showBalance.place(relx=0.5, y=120, anchor='n')
homeDepButton.place(relx=0.278, y=170, anchor='n')
homeWithButton.place(relx=0.7, y=170, anchor='n')
homeTransButton.place(relx=0.278, y=240, anchor='n')
homelogoutButton.place(relx=0.7, y=240, anchor='n')

showframe(loginScreen)
window.mainloop()