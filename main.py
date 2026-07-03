from tkinter import *
from tkinter import ttk, messagebox

from gym_manager import GymManager
from gym_manager import Member
from gym_manager import BMICalculator


class FitZoneApp:

    def __init__(self, root):

        self.root = root

        self.root.title("FitZone Gym Management System")

        try:
            self.root.state("zoomed")
        except:
            self.root.geometry(
                f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0"
            )

        self.root.configure(bg="#F5F7FA")

        self.manager = GymManager()

        self.login_screen()

    
    # Clear Window
    
    def clear_window(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    
    # Login Screen
    
    def login_screen(self):

        self.clear_window()

        Label(
            self.root,
            text="FITZONE",
            font=("Segoe UI", 30, "bold"),
            bg="#F5F7FA",
            fg="#2C3E50"
        ).pack(pady=20)

        Label(
            self.root,
            text="Your Fitness Management Partner",
            font=("Segoe UI", 12),
            bg="#F5F7FA",
            fg="#7F8C8D"
        ).pack()

        login_frame = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        login_frame.pack(pady=40)

        Label(
            login_frame,
            text="Admin Login",
            font=("Segoe UI", 18, "bold"),
            bg="white"
        ).grid(row=0, column=0, columnspan=2, pady=20)

        Label(
            login_frame,
            text="Username",
            font=("Segoe UI", 12),
            bg="white"
        ).grid(row=1, column=0, padx=20, pady=10)

        self.username_entry = Entry(
            login_frame,
            font=("Segoe UI", 12),
            width=25
        )

        self.username_entry.grid(
            row=1,
            column=1,
            padx=20
        )

        Label(
            login_frame,
            text="Password",
            font=("Segoe UI", 12),
            bg="white"
        ).grid(row=2, column=0, padx=20, pady=10)

        self.password_entry = Entry(
            login_frame,
            show="*",
            font=("Segoe UI", 12),
            width=25
        )

        self.password_entry.grid(
            row=2,
            column=1,
            padx=20
        )

        Button(
            login_frame,
            text="Login",
            width=15,
            font=("Segoe UI", 12, "bold"),
            bg="#3498DB",
            fg="white",
            command=self.check_login
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20
        )

    
    # Login Validation
    
    def check_login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin123":

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            self.dashboard()

        else:

            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )

    
    # Dashboard
    
    def dashboard(self):

        self.clear_window()

        total_members = self.manager.total_members()

        Label(
            self.root,
            text="FITZONE DASHBOARD",
            font=("Segoe UI", 26, "bold"),
            bg="#F5F7FA",
            fg="#2C3E50"
        ).pack(pady=20)

        stats_frame = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        stats_frame.pack(pady=20)

        Label(
            stats_frame,
            text=f"Total Members : {total_members}",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#27AE60"
        ).pack(pady=10)

        Label(
            stats_frame,
            text="Monthly ₹500 | Quarterly ₹1200 | Yearly ₹4500",
            font=("Segoe UI", 11),
            bg="white",
            fg="#34495E"
        ).pack(pady=5)

        btn_frame = Frame(
            self.root,
            bg="#F5F7FA"
        )

        btn_frame.pack(pady=40)

        Button(
            btn_frame,
            text="➕ Add Member",
            width=20,
            height=2,
            font=("Segoe UI", 13, "bold"),
            bg="#3498DB",
            fg="white",
            command=self.add_member_screen
        ).grid(row=0, column=0, padx=20, pady=20)

        Button(
            btn_frame,
            text="👀 View Members",
            width=20,
            height=2,
            font=("Segoe UI", 13, "bold"),
            bg="#2ECC71",
            fg="white",
            command=self.view_members
        ).grid(row=0, column=1, padx=20, pady=20)

        Button(
            btn_frame,
            text="📊 BMI Calculator",
            width=20,
            height=2,
            font=("Segoe UI", 13, "bold"),
            bg="#9B59B6",
            fg="white",
            command=self.bmi_screen
        ).grid(row=1, column=0, padx=20, pady=20)

        Button(
            btn_frame,
            text="📁 Export Report",
            width=20,
            height=2,
            font=("Segoe UI", 13, "bold"),
            bg="#F39C12",
            fg="white",
            command=self.export_report
        ).grid(row=1, column=1, padx=20, pady=20)

        Button(
            btn_frame,
            text="🚪 Logout",
            width=20,
            height=2,
            font=("Segoe UI", 13, "bold"),
            bg="#E74C3C",
            fg="white",
            command=self.login_screen
        ).grid(row=2, column=0, columnspan=2, pady=20)

    
    # Add Member Screen
    
    def add_member_screen(self):

        self.clear_window()

        Label(
            self.root,
            text="Add New Member",
            font=("Segoe UI", 22, "bold"),
            bg="#F5F7FA"
        ).pack(pady=20)

        form = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        form.pack(pady=20)

        labels = [
            "Member ID",
            "Name",
            "Age",
            "Gender",
            "Phone",
            "Goal",
            "Plan",
            "Payment Status"
        ]

        self.entries = {}

        for i, text in enumerate(labels):

            Label(
                form,
                text=text,
                font=("Segoe UI", 12),
                bg="white"
            ).grid(row=i, column=0, padx=15, pady=10)

            # Goal Dropdown
            if text == "Goal":

                combo = ttk.Combobox(
                    form,
                    values=[
                        "Weight Loss",
                        "Muscle Gain",
                        "Athlete Training",
                        "General Fitness"
                    ],
                    width=27,
                    state="readonly"
                )

                combo.grid(row=i, column=1, padx=15)

                self.entries[text] = combo

            # Plan Dropdown
            elif text == "Plan":

                combo = ttk.Combobox(
                    form,
                    values=[
                        "Monthly",
                        "Quarterly",
                        "Yearly"
                    ],
                    width=27,
                    state="readonly"
                )

                combo.grid(row=i, column=1, padx=15)

                self.entries[text] = combo

            # Payment Status Dropdown
            elif text == "Payment Status":

                combo = ttk.Combobox(
                    form,
                    values=[
                        "Paid",
                        "Pending"
                    ],
                    width=27,
                    state="readonly"
                )

                combo.grid(row=i, column=1, padx=15)

                self.entries[text] = combo

            else:

                entry = Entry(
                    form,
                    width=30,
                    font=("Segoe UI", 11)
                )

                entry.grid(row=i, column=1, padx=15)

                self.entries[text] = entry

        Button(
            self.root,
            text="Save Member",
            font=("Segoe UI", 12, "bold"),
            bg="#27AE60",
            fg="white",
            command=self.save_member
        ).pack(pady=10)

        Button(
            self.root,
            text="Back",
            font=("Segoe UI", 11),
            command=self.dashboard
        ).pack()

    # 
    # Save Member
    # 
    def save_member(self):

        try:

            member_id = self.entries["Member ID"].get()
            name = self.entries["Name"].get()
            age = self.entries["Age"].get()
            gender = self.entries["Gender"].get()
            phone = self.entries["Phone"].get()

            goal = self.entries["Goal"].get()
            plan = self.entries["Plan"].get()
            payment_status = self.entries["Payment Status"].get()

            # Validation
            if (
                member_id == "" or
                name == "" or
                age == "" or
                gender == "" or
                phone == "" or
                goal == "" or
                plan == "" or
                payment_status == ""
            ):
                raise ValueError(
                    "All fields are required"
                )

            age = int(age)

            if len(phone) != 10:
                raise ValueError(
                    "Phone number must be 10 digits"
                )

            # Fee Calculation
            fees = {
                "Monthly": 500,
                "Quarterly": 1200,
                "Yearly": 4500
            }

            fee = fees.get(plan, 0)

            member = Member(
                member_id,
                name,
                age,
                gender,
                phone,
                goal,
                plan,
                fee,
                payment_status
            )

            self.manager.add_member(member)

            messagebox.showinfo(
                "Success",
                f"Member Added Successfully\n\nFee: ₹{fee}"
            )

            self.dashboard()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )
    
    # View Members
    
    def view_members(self):

        self.clear_window()

        Label(
            self.root,
            text="Member Records",
            font=("Segoe UI", 22, "bold"),
            bg="#F5F7FA"
        ).pack(pady=15)

        search_frame = Frame(
            self.root,
            bg="#F5F7FA"
        )

        search_frame.pack(pady=10)

        Label(
            search_frame,
            text="Member ID:",
            font=("Segoe UI", 11),
            bg="#F5F7FA"
        ).pack(side=LEFT)

        self.search_entry = Entry(
            search_frame,
            font=("Segoe UI", 11)
        )

        self.search_entry.pack(
            side=LEFT,
            padx=10
        )

        Button(
            search_frame,
            text="Search",
            bg="#3498DB",
            fg="white",
            command=self.search_member
        ).pack(side=LEFT)

        columns = (
            "ID",
            "Name",
            "Age",
            "Gender",
            "Phone",
            "Goal",
            "Plan",
            "Fee",
            "Payment"
        )

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:

            self.tree.heading(
                col,
                text=col
            )

            self.tree.column(
                col,
                width=120
            )

        self.tree.pack(
            pady=20,
            fill=BOTH,
            expand=True
        )

        members = self.manager.get_all_members()

        for member in members:
            self.tree.insert(
                "",
                END,
                values=member
            )

        button_frame = Frame(
            self.root,
            bg="#F5F7FA"
        )

        button_frame.pack(pady=10)

        Button(
            button_frame,
            text="Delete Member",
            bg="#E74C3C",
            fg="white",
            width=15,
            command=self.delete_member
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        Button(
            button_frame,
            text="Refresh",
            bg="#2ECC71",
            fg="white",
            width=15,
            command=self.view_members
        ).grid(
            row=0,
            column=1,
            padx=10
        )

        Button(
            button_frame,
            text="Back",
            width=15,
            command=self.dashboard
        ).grid(
            row=0,
            column=2,
            padx=10
        )

    
    # Search Member
    
    def search_member(self):

        member_id = self.search_entry.get()

        member = self.manager.search_member(
            member_id
        )

        self.tree.delete(
            *self.tree.get_children()
        )

        if member:

            self.tree.insert(
                "",
                END,
                values=member
            )

        else:

            messagebox.showinfo(
                "Not Found",
                "Member not found"
            )

    
    # Delete Member
    
    def delete_member(self):

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a member"
            )

            return

        values = self.tree.item(
            selected[0]
        )["values"]

        member_id = str(values[0])

        confirm = messagebox.askyesno(
            "Confirm",
            "Delete this member?"
        )

        if confirm:

            deleted = self.manager.delete_member(
                member_id
            )

            if deleted:

                messagebox.showinfo(
                    "Success",
                    "Member deleted successfully"
                )

                self.view_members()

    
    # Export Report
    
    def export_report(self):

        self.manager.export_report()

        messagebox.showinfo(
            "Success",
            "Report exported successfully!\nSaved as report.txt"
        )

    
    # BMI Calculator Screen
    
    def bmi_screen(self):

        self.clear_window()

        Label(
            self.root,
            text="BMI Calculator",
            font=("Segoe UI", 22, "bold"),
            bg="#F5F7FA"
        ).pack(pady=20)

        frame = Frame(
            self.root,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        frame.pack(pady=20)

        Label(
            frame,
            text="Weight (kg)",
            font=("Segoe UI", 12),
            bg="white"
        ).grid(row=0, column=0, padx=20, pady=15)

        self.weight_entry = Entry(
            frame,
            font=("Segoe UI", 12),
            width=25
        )

        self.weight_entry.grid(
            row=0,
            column=1,
            padx=20
        )

        Label(
            frame,
            text="Height (cm)",
            font=("Segoe UI", 12),
            bg="white"
        ).grid(row=1, column=0, padx=20, pady=15)

        self.height_entry = Entry(
            frame,
            font=("Segoe UI", 12),
            width=25
        )

        self.height_entry.grid(
            row=1,
            column=1,
            padx=20
        )

        Button(
            self.root,
            text="Calculate BMI",
            font=("Segoe UI", 12, "bold"),
            bg="#9B59B6",
            fg="white",
            command=self.calculate_bmi
        ).pack(pady=10)

        self.bmi_result = Label(
            self.root,
            text="",
            font=("Segoe UI", 14, "bold"),
            bg="#F5F7FA"
        )

        self.bmi_result.pack(pady=20)

        Button(
            self.root,
            text="Back",
            font=("Segoe UI", 11),
            command=self.dashboard
        ).pack()

    
    # Calculate BMI
    
    def calculate_bmi(self):

        try:

            weight = float(
                self.weight_entry.get()
            )

            height = float(
                self.height_entry.get()
            )

            bmi, status = BMICalculator.calculate(
                weight,
                height
            )

            self.bmi_result.config(
                text=f"BMI : {bmi}    |    Status : {status}"
            )

        except:

            messagebox.showerror(
                "Error",
                "Please enter valid numbers"
            )


# Run Application


if __name__ == "__main__":

    root = Tk()

    app = FitZoneApp(root)

    root.mainloop()
