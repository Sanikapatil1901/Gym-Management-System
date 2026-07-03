# gym_manager.py

import os


class Member:

    def __init__(
            self,
            member_id,
            name,
            age,
            gender,
            phone,
            goal,
            plan,
            fee,
            payment_status
    ):

        self.member_id = member_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.goal = goal
        self.plan = plan
        self.fee = fee
        self.payment_status = payment_status

    def to_string(self):

        return (
            f"{self.member_id},"
            f"{self.name},"
            f"{self.age},"
            f"{self.gender},"
            f"{self.phone},"
            f"{self.goal},"
            f"{self.plan},"
            f"{self.fee},"
            f"{self.payment_status}\n"
        )


class GymManager:

    FILE_NAME = "members.txt"

    def __init__(self):

        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, "w").close()

    
    # Add Member
    
    def add_member(self, member):

        with open(self.FILE_NAME, "a") as file:
            file.write(member.to_string())

    
    # Get All Members
    
    def get_all_members(self):

        members = []

        with open(self.FILE_NAME, "r") as file:

            for line in file:

                line = line.strip()

                if line:

                    data = line.split(",")

                    members.append(data)

        return members

    
    # Search Member
    
    def search_member(self, member_id):

        with open(self.FILE_NAME, "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[0] == member_id:
                    return data

        return None

    
    # Delete Member
    
    def delete_member(self, member_id):

        deleted = False

        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()

        with open(self.FILE_NAME, "w") as file:

            for record in records:

                data = record.strip().split(",")

                if data[0] != member_id:

                    file.write(record)

                else:

                    deleted = True

        return deleted

    
    # Total Members
    
    def total_members(self):

        return len(self.get_all_members())

    
    # Export Report
    
    def export_report(self):

        members = self.get_all_members()

        monthly = 0
        quarterly = 0
        yearly = 0

        paid = 0
        pending = 0

        total_revenue = 0

        for member in members:

            plan = member[6]
            fee = int(member[7])
            payment = member[8]

            total_revenue += fee

            if plan == "Monthly":
                monthly += 1

            elif plan == "Quarterly":
                quarterly += 1

            elif plan == "Yearly":
                yearly += 1

            if payment == "Paid":
                paid += 1

            else:
                pending += 1

        with open("report.txt", "w") as report:

            report.write("FITZONE GYM REPORT\n")
            report.write("=" * 40 + "\n\n")

            report.write(
                f"Total Members : {len(members)}\n"
            )

            report.write(
                f"Monthly Plans : {monthly}\n"
            )

            report.write(
                f"Quarterly Plans : {quarterly}\n"
            )

            report.write(
                f"Yearly Plans : {yearly}\n"
            )

            report.write(
                f"Paid Members : {paid}\n"
            )

            report.write(
                f"Pending Members : {pending}\n"
            )

            report.write(
                f"Expected Revenue : Rs{total_revenue}\n"
            )

        return True


class BMICalculator:

    @staticmethod
    def calculate(weight, height):

        height_m = height / 100

        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            status = "Underweight"

        elif bmi < 25:
            status = "Normal"

        elif bmi < 30:
            status = "Overweight"

        else:
            status = "Obese"

        return round(bmi, 2), status

