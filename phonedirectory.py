import re

class Phonebook(object):
    def __init__(self):
        self.people = []


    def add_person(self, person):
        # print("Adding person: {} : {} to phonebook".format(person.name,person.phone))
        self.people.append(person)

    def __iter__(self):
        for elem in self.people:
            # print(elem.show())
            yield elem

    def find_phone(self, phone ):
        found = []
        for person in self.people:
            # print("{} - {}".format(person.phone,phone))
            if str(person.phone) == str(phone):
                found.append(person)
        return found



class Person(object):
    def __init__(self, name,
                 mobile_phone=None, office_phone=None,
                 private_phone=None, email=None, phone=None, address=None):
        self.name = name
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email
        self.phone = phone
        self.address = address

    def add_mobile_phone(self, number):
        self.mobile = number

    def add_office_phone(self, number):
        self.office = number

    def add_phone(self, number):
        self.phone = number

    def add_private_phone(self, number):
        self.private = number

    def add_email(self, address):
        self.email = address

    def add_address(self, address):
        self.address = address

    def show(self):
        print("Data:")
        s = 'name: %s \n' % self.name
        if self.mobile is not None:
            s += 'mobile phone:   %s\n' % self.mobile
        if self.office is not None:
            s += 'office phone:   %s\n' % self.office
        if self.phone is not None:
            s += 'general phone:   %s\n' % self.phone
        if self.private is not None:
            s += 'private phone:  %s\n' % self.private
        if self.email is not None:
            s += 'email address:  %s\n' % self.email
        if self.address is not None:
            s += 'address address:  %s\n' % self.address
        print (s)




def phone(strng, num):
    # num is not yet implemented.
    phonebook = Phonebook()
    datas = strng.split("\n")
    datas = [data for data in datas if data]

    for data in datas:
        tel = re.findall("([1-9]*[1-9]-[0-9]\d{2}-[0-9]\d{2}-[0-9]\d{3})", data)[0]
        name = re.findall("(?<=\<)(.*?)(?=\>)", data)[0]
        address = data.replace(tel,"")
        address = address.replace("<" + name + ">", "")
        address = re.sub('[^A-Za-z0-9-" ."]+', ' ', address)
        address = " ".join(address.split())
        # print("Name => " + str(name) + ", Phone => " + str(tel) + ", Address => " + str(address))
        person = Person(name=name, phone=tel, address=address)
        # person.show()
        phonebook.add_person(person)
        # print("Phone => {}, Name => {}, Address => {}".format(tel, name, address))
        # input()

    # for person in phonebook:
    #     print("Tel:{}.".format(person.phone))

    results = phonebook.find_phone(num)
    # print(len(results))
    if len(results) == 1:
        return ("Phone => {}, Name => {}, Address => {}".format(results[0].phone, results[0].name, results[0].address))
    if len(results) > 1:
        return "Error => Too many people: {}".format(num)
    if len(results) == 0:
        return "Error => Not found: {}".format(num)


dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n")


print(phone(dr,"1-098-512-2222")) # 2
print(phone(dr, "5-555-555-5555")) # 0
print(phone(dr, "1-498-512-2222")) # 1
print(phone(dr, "48-421-674-8974"))
print(phone(dr, "1-541-754-3010"))