from person import Person
from criteriasingle import CriteriaSingle
from criteriafemale import CriteriaFemale
from criteriamale import CriteriaMale
from andcriteria import AndCriteria
from orcriteria import OrCriteria


def print_persons(persons: list):
    for person in persons:
        print("Person: [ Name:", person.get_name(), ", Gender:", person.get_gender(), ", Marital Status:", person.get_marital_status(), "]")


if __name__ == "__main__":
    persons = list()
    persons.append(Person("Robert","Male", "Single"));
    persons.append(Person("John","Male", "Married"));
    persons.append(Person("Laura","Female", "Married"));
    persons.append(Person("Diana","Female", "Single"));
    persons.append(Person("Mike","Male", "Single"));
    persons.append(Person("Bobby","Male", "Single"));

    male = CriteriaMale()
    female = CriteriaFemale()
    single = CriteriaSingle()

    print("Males:")
    print_persons(male.meet_criteria(persons))

    print("Females:")
    print_persons(female.meet_criteria(persons))

    print("Single Males:")
    print_persons(AndCriteria(single, male).meet_criteria(persons))

    print("Single or Female")
    print_persons(OrCriteria(single, female).meet_criteria(persons))