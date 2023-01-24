class School:
    __schools = []

    def __init__(self, name, address, specialized, number):
        self.name = name
        self.address = address
        self.specialized = specialized
        self.number = int(number)
        School.__schools.append(self)

    @classmethod
    def address_chilonzor(cls, name, specialized, number):
        obj = cls(name, "Chilonzor", specialized, number)
        return obj

    @classmethod
    def president_school(cls, name, address, number):
        obj = cls(name, address, "president school", number)
        return obj

    @staticmethod
    def get_schools(count):
        schools = []
        count = int(count)
        if len(School.__schools) >= count:
            j = 0
            for i in School.__schools:
                schools.append(i)
                j+=1
                if j == count:
                    break
        else:
            schools = School.__schools
        return schools

    def __str__(self):
        return f"Name: {self.name}\naddress: {self.address}\nspecialized: {self.specialized}\nnumber: {self.number}\n"


school = School("Islom Karimov", "Toshkent", "matematika", 11)
president_school_1 = School.president_school("Al Xorazmiy", "Xorazm", 1)
president_school_2 = School.president_school("Beruniy", "Toshkent", 2)
president_school_3 = School.president_school("Farobiy", "Namangan", 3)
president_school_4 = School.president_school("Amir Temur", "Qarshi", 4)
# print(president_school_1)
# print(president_school_2)

for i in school.get_schools(3):
    print(i)


