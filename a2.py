//Q1
class BookStore:
    NoOfBooks = 0
    def __init__(self, name, author):
        self.name = name
        self.author = author 
    
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.name} by {self.author}. No of books : {BookStore.NoOfBooks}")
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display() 
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()  




//Q2
class BookStore:
    NoOfBooks = 0
    def __init__(self, name, author):
        self.name = name
        self.author = author 
    
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.name} by {self.author}. No of books : {BookStore.NoOfBooks}")
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display() 
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()  

//Q3
class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0         
        self.Area = 0.0           
        self.Circumference = 0.0  
    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))
    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
    def Display(self):
        print(f"Radius: {self.Radius}")
        print(f"Area: {self.Area}")
        print(f"Circumference: {self.Circumference}")

circle1 = Circle()
circle1.Accept()  
circle1.CalculateArea()  
circle1.CalculateCircumference()  
circle1.Display() 

print()

circle2 = Circle()
circle2.Accept()  
circle2.CalculateArea()  
circle2.CalculateCircumference()  
circle2.Display() 




//Q4
class BankAccount:
    ROI = 10.5
    def __init__(self):
        self.Name = input("Enter the account holder's name: ")
        self.Amount = float(input("Enter the initial amount in the account: "))

    def Deposit(self):
        deposit_amount = float(input("Enter the amount to deposit: "))
        self.Amount += deposit_amount
        print(f"Amount deposited: {deposit_amount}")
        print(f"Updated balance: {self.Amount}")
    def Withdraw(self):
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print(f"Amount withdrawn: {withdraw_amount}")
            print(f"Updated balance: {self.Amount}")
        else:
            print("Insufficient funds to withdraw.")
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest calculated at {BankAccount.ROI}%: {interest}")
        return interest
    def Display(self):
        print(f"Account holder: {self.Name}")
        print(f"Current balance: {self.Amount}")
account1 = BankAccount()  

account1.Display()
account1.Deposit()
account1.Withdraw()
account1.CalculateInterest()
account1.Display()

print()  

account2 = BankAccount()  
account2.Display()
account2.Deposit()
account2.Withdraw()
account2.CalculateInterest()
account2.Display()




//Q5
class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: ")) 
    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True
    def ChkPerfect(self):
        sum_factors = self.SumFactors()
        return sum_factors == self.Value
    def SumFactors(self):
        factors = self.Factors()
        return sum(factors)
    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        print(f"Factors of {self.Value}: {factors}")
        return factors
num1 = Numbers()
print(f"Is {num1.Value} prime? {num1.ChkPrime()}")
print(f"Is {num1.Value} perfect? {num1.ChkPerfect()}")
num1.Factors()
print(f"Sum of factors of {num1.Value}: {num1.SumFactors()}")
print()
num2 = Numbers()
print(f"Is {num2.Value} prime? {num2.ChkPrime()}")
print(f"Is {num2.Value} perfect? {num2.ChkPerfect()}")
num2.Factors()
print(f"Sum of factors of {num2.Value}: {num2.SumFactors()}")




//Q6
class Numbers:
    def __init__(self):
        self.Value1 = 0 
        self.Value2 = 0  
    def Accept(self):
        self.Value1 = float(input("Enter the first number (Value1): "))
        self.Value2 = float(input("Enter the second number (Value2): "))
    def Addition(self):
        return self.Value1 + self.Value2
    def Subtraction(self):
        return self.Value1 - self.Value2
    def Multiplication(self):
        return self.Value1 * self.Value2
    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Error: Division by zero is not allowed."
num1 = Numbers()
num1.Accept()
print(f"Addition of {num1.Value1} and {num1.Value2}: {num1.Addition()}")
print(f"Subtraction of {num1.Value1} and {num1.Value2}: {num1.Subtraction()}")
print(f"Multiplication of {num1.Value1} and {num1.Value2}: {num1.Multiplication()}")
print(f"Division of {num1.Value1} by {num1.Value2}: {num1.Division()}")

print()
num2 = Numbers()
num2.Accept()
print(f"Addition of {num2.Value1} and {num2.Value2}: {num2.Addition()}")
print(f"Subtraction of {num2.Value1} and {num2.Value2}: {num2.Subtraction()}")
print(f"Multiplication of {num2.Value1} and {num2.Value2}: {num2.Multiplication()}")
print(f"Division of {num2.Value1} by {num2.Value2}: {num2.Division()}")
