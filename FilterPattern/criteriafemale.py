from criteria import Criteria


class CriteriaFemale(Criteria):
    def meet_criteria(self, persons: list):
        male_persons = list()
        for person in persons:
            if person.get_gender().lower() == "female":
                male_persons.append(person)
        return male_persons


if __name__ == "__main__":
    from person import Person

    persons = list()
    persons.append(Person("Robert","Male", "Single"));
    persons.append(Person("John","Male", "Married"));
    persons.append(Person("Laura","Female", "Married"));
    persons.append(Person("Diana","Female", "Single"));
    persons.append(Person("Mike","Male", "Single"));
    persons.append(Person("Bobby","Male", "Single"));

    criteria = CriteriaFemale()
    ans = criteria.meet_criteria(persons)
    for person in ans:
        print(person.get_gender())