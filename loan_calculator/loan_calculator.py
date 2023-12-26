from tkinter import *

class LoanCalculator:

    def __init__(self):
        # Start tkinter
        root = Tk()
        # Set window side
        root.geometry('500x300')
        # Set window name
        root.title('Loan Calculator')
        # Set window color
        root.config(bg='#a39ea0')
        # Set location, font style and explaining text for annual interest rate 
        Label(root,text='Annual rate, %',font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=10)
        # Set location, font style and explaining text for loan's period of time
        Label(root,text='Period, years',font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=50)
        # Set location, font style and explaining text for loan's amount
        Label(root,text='Loan amount',font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=90)
        # Set location, font style and explaining text for the monthly payment
        Label(root,text='Monthly payment:',font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=150)
        # Set location, font style and explaining text for the total amount of money
        Label(root,text='The total amount of the payment:',font=('Arial,15,bold'),bg='#a39ea0').place(x=10,y=190)

        # Add place for writing a annual year rate
        self.annualinterestVar=StringVar()
        Entry(root, textvariable=self.annualinterestVar,font=('Arial,15,bold')).place(x=220,y=10) 
        # Add place for writing a period of time
        self.numberofyearsVar=StringVar()
        Entry(root, textvariable=self.numberofyearsVar,font=('Arial,15,bold')).place(x=220,y=50) 
        # Add place for writing a loan amount
        self.loanamountVar=StringVar()
        Entry(root, textvariable=self.loanamountVar,font=('Arial,15,bold')).place(x=220,y=90) 
        # Add place for output a monthly payment
        self.monthlypaymentVar=StringVar()
        Label(root, textvariable=self.monthlypaymentVar,font=('Arial,15,bold')).place(x=220,y=150) 
        # Add place for output a total amount of loan 
        self.totalpaymentVar=StringVar()
        Label(root, textvariable=self.totalpaymentVar,font=('Arial,15,bold')).place(x=220,y=190) 

        # Create a button
        Button(root, text='Calculate', font=('Arial,15,bold'),command=self.calculateloan).place(x=180,y=240)

        # Starting a window
        root.mainloop()

    # Define the function for calculating all payment amount
    def calculateloan(self):
        # Define the formula for calculating montly payment
        monthlypayment=self.getmonthlypayment(float(self.loanamountVar.get()),float(self.annualinterestVar.get()) / 1200, int(self.numberofyearsVar.get()))
        self.monthlypaymentVar.set(format(monthlypayment, '10.2f'))
        # Define the formula for calculating all amount of payment
        totalpayment=float(self.monthlypaymentVar.get()) * 12 * int(self.numberofyearsVar.get())
        self.totalpaymentVar.set(format(totalpayment, '10.2f'))

    # Define the function for monthly payment
    def getmonthlypayment(self,loanamount,monthlyinterestrate,numberofyears):
        # Define the formula for calculating monthly payment
        monthlypayment=loanamount * monthlyinterestrate / (1-1 / (1 + monthlyinterestrate) ** (numberofyears * 12))
        return monthlypayment

# Call class to start the programm
LoanCalculator()
