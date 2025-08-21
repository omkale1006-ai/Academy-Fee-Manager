class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, roll_no, course, total_fees):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course
        self.total_fees = total_fees
        self.installments = []  # list to store paid installments

    # Pay installment
    def pay_installment(self, amount):
        if sum(self.installments) + amount <= self.total_fees:
            self.installments.append(amount)
            pending = self.total_fees - sum(self.installments)
            print(f"💰 Installment Paid: {amount} | Pending: {pending}")

        else:
            print("❌ Payment exceeds total fees!")

    # Check pending fees
    def pending_fees(self):
        return self.total_fees - sum(self.installments)

    # __len__ → number of installments paid
    def __len__(self):
        return len(self.installments)

    # __str__ → student details
    def __str__(self):
        return (f"📊 Student Data:\n"
                f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Course: {self.course }\n"
                f"Total Fees: {self.total_fees}\n"
                f"Paid Installments: {self.installments}\n"
                f"Pending: {self.pending_fees()}\n")

    # Destructor
    def __del__(self):
        print(
            f"🗑️ Student record deleted for {self.name} (Roll No: {self.roll_no})"
        )


name = input("Enter your name: ")
age = int(input("Enter your age: "))
roll = (input("Enter your rool no: "))
course = input("Enter your coures: ").upper()
print("Courses available: AI&DS, CSE, ECE, EEE")
print("=" * 20 + "\n")
if course == "AI&DS":
    fees = 100000
elif course == "CSE":
    fees = 150000
elif course == "ECE":
    fees = 120000
elif course == "EEE":
    fees = 130000
else:
    print("Invalid course")

s = Student(name, age, roll, course, fees)

print("welcome to the student fees management system")
while True:
    print("1. Pay installment")
    print("2. Check pending fees")
    print("3. Check number of installments paid")
    print("4. Display student details")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = int(input("Enter installment amount: "))
        s.pay_installment(amount)
        print("Installment paid successfully")
        print(" ")
    if choice == 2:
        print("Pending fees: ", s.pending_fees())
        print(" ")
    if choice == 3:
        print("Number of installments paid: ", len(s))
        print(" ")
    if choice == 4:
        print(s)
        print(" ")
    if choice == 5:
        print("Thank you for using the student fees management system")
        print(" ")
        break
