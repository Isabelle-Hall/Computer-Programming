# The comparison operations that can be performed are subset, proper subset, superset, and proper superset.
# These return a True or False result.

staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}


# < or issubset() === checks if all elements of managers set are within the staff set
# <= === proper subset, same check but also ensures that the sets are not exactly equal
# > or issuperset() === superset, does opposite of subset
# >= === proper superset, does opposite of proper subset

if managers.issubset(staff):
    print("All managers are staff members")

if staff.issuperset(managers):
    print("All managers are staff members")


