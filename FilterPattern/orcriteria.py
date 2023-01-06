from criteria import Criteria


class OrCriteria(Criteria):
    def __init__(self, criteria: "Criteria", other_criteria: "Criteria"):
        self._criteria = criteria
        self._other_criteria = other_criteria

    def meet_criteria(self, persons: list):
        first_criteria_persons = self._criteria.meet_criteria(persons)
        second_criteria_persons = self._other_criteria.meet_criteria(persons)

        for person in second_criteria_persons:
            if person not in first_criteria_persons:
                first_criteria_persons.append(person)

        return first_criteria_persons

if __name__ == "__main__":
    from person import Person
    from criteriasingle import CriteriaSingle
    from criteriafemale import CriteriaFemale

    persons = list()
    persons.append(Person("Robert","Male", "Single"));
    persons.append(Person("John","Male", "Married"));
    persons.append(Person("Laura","Female", "Married"));
    persons.append(Person("Diana","Female", "Single"));
    persons.append(Person("Mike","Male", "Single"));
    persons.append(Person("Bobby","Male", "Single"));

    criteria = CriteriaSingle()
    other_criteria = CriteriaFemale()
    ans = OrCriteria(criteria, other_criteria).meet_criteria(persons)
    for person in ans:
        print(person.get_marital_status(), person.get_gender())