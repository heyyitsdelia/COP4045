##Python Assignment question No.2

#Problem 2.a-creating ParkingPermit class
class ParkingPermit:
    """
    a) Create a ParkingPermit class whose constructor stores an owner’s name, the number of
    months purchased and a fee schedule given as a dictionary.  
    """

    def __init__(self, owner_name: str, num_months: int, fees_sch: dict[str, int]) -> None:
        """
        stores an owner’s name, the number of
        months purchased and a fee schedule given as a dictionary.
        """
        self.owner_name = owner_name
        self.num_months = num_months
        self.fees_sch = fees_sch

    #Problem 2.d-creating _str_ and _repr_ functions part 1
    def __str__(self) -> str:
        """description/information of parking permit."""
        return "Owner's Name: " + self.owner_name + ", # of Months: " + str(self.num_months)

    def __repr__(self) -> str:
        """more detailed description/information of parking permit."""
        return "Parking Permit info. - " + repr(self.owner_name) + ", " + str(self.num_months) + ", " + repr(self.fees_sch) + ")"
    

#Problem 2.b- creating StudentPermit subclass part 1
class StudentPermit(ParkingPermit):
    """
    b) Derive the StudentPermit class, which also stores the number of vehicles registered, and
    the FacultyPermit class, which stores whether garage access is included.
    """
    def __init__(self, owner_name: str, num_months: int, fees_sch: dict[str, int], vehicles: int) -> None:
        """stores the number of vehicles registere."""

        ParkingPermit.__init__(self, owner_name, num_months, fees_sch)
        self.vehicles = vehicles

    #Problem 2.d-creating _str_ and _repr_ functions part 2
    def __str__(self) -> str:
        """description/information of student permit."""
        return "Owner's name: " + self.owner_name + ", Months: " + str(self.num_months) + ", Vehicles: " + str(self.vehicles)

    def __repr__(self) -> str:
        """more detailed description/information of student permit."""
        return "Student Permit info. - " + repr(self.owner_name) + ", " + str(self.num_months) + ", " + repr(self.fees_sch) + ", " + str(self.vehicles) + ")"

    #Problem 2.c-Creating Student permit cost part 1
    def cost(self) -> int:
        """
       c) Override cost() in both subclasses. A student permit costs $25 per month plus a one-time $10
        fee for each vehicle after the first. A faculty permit costs $40 per month, plus $15 per month for
        garage access.
        """
        total_cost = self.num_months * self.fees_sch["student_monthly_amount"]

        if self.vehicles > 1:
            total_cost += (self.vehicles - 1) * self.fees_sch["extra_vehicle_amount"]

        return total_cost

#Problem 2.b- creating faculty permit part 2
class FacultyPermit(ParkingPermit):
    """stores whether garage access is included"""
    def __init__(self, owner_name: str, num_months: int, fees_sch: dict[str, int], garage: bool) -> None:

        ParkingPermit.__init__(self, owner_name, num_months, fees_sch)
        self.garage = garage

    #Problem 2.c -Faculty permit cost part 2
    def cost(self) -> int:
        """
        Override cost() in both subclasses. A faculty permit costs $40 per month, plus $15 per month for
        garage access.
        """
        total_cost = self.num_months * self.fees_sch["faculty_monthly_amount"]

        if self.garage:
            total_cost += self.num_months * self.fees_sch["garage_monthly_amount"]

        return total_cost

    #Problem 2.d-creating _str_ and _repr_ functions part 3
    def __str__(self) -> str:
        """description/information of faculty permit."""
        return "Owner: " + self.owner_name + ", Months: " + str(self.num_months) + ", Garage: " + str(self.garage)

    def __repr__(self) -> str:
        """more detailed description/information of faculty permit."""
        return "Faculty Permit info. - " + repr(self.owner_name) + ", " + str(self.num_months) + ", " + repr(self.fees_sch) + ", " + str(self.garage) + ")"

#Problem 2.e-summarizing the parking permits
def summarize_list(permits: list[ParkingPermit]) -> int:
    """
    Write a function called summarize_list() that prints each owner’s name and permit cost,
    then returns the total revenue from a mixed list of permits given as parameter. Use the methods
    from part d).
    """
    total_revenue = 0

    #loop to iterste through list to collect the cost of each permit and print the information
    for p in permits:
        print(str(p), "Cost: $", p.cost())

        total_revenue += p.cost()

    return total_revenue

#Problem 2.f-create main function
def main() -> None:
    """
    f) Write a main function that illustrates how the classes and the function are used. It should print
    the objects involved and the computation output.    
    """

    fees = {
        "student_monthly_amount": 25,
        "extra_vehicle_amount": 10,
        "faculty_monthly_amount": 40,
        "garage_monthly_amount": 15
    }

    student_num1 = StudentPermit("timmy", 3, fees, 2)
    faculty_num1 = FacultyPermit("sarah", 3, fees, True)

    print(student_num1)
    print(repr(student_num1))

    print(faculty_num1)
    print(repr(faculty_num1))

    permits = [student_num1, faculty_num1]

    total = summarize_list(permits)

    print("Total Revenue: $", total)


if __name__ == "__main__":
    main()