# PART 31: Class Objects

# When creating a class object, we are defining a new datatype.
# Class objects allow us to bundle our data with functionality.

class Person:  # Declaring the class

    drinking_age = 21  # Class variable, shared by all instances

    def __init__(self, first_name, last_name, age):  # This function gets invoked automatically when creating instance
        # Instance variables unique to each instance:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_drinking_age(self):
        if self.age >= self.drinking_age:
            return True
        else:
            return False


# Creating new instances of Person:
person1 = Person('John', 'Doe', 23)
person2 = Person('Jane', 'Doe', 18)

print(type(Person))
print()

print(person1.first_name)
print(person1.is_drinking_age())
print()

print(person2.first_name)
print(person2.is_drinking_age())
