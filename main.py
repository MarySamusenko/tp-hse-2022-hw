class Person:
    def __init__(self):
        self.surname = None
        self.name = None
        self.fathername = None
        self.phone = None
        self.email = None
        self.line = None

    def GetData(self, line):
        line = line.strip('\n')
        PersonData = line.split(",")
        name = PersonData[0].split()
        phone = PersonData[1].strip()
        email = PersonData[-1].strip()
        if len(name) == 3:
            self.surname = name[0]
            self.name = name[1]
            self.fathername = name[2]
        elif len(name) == 2:
            self.surname = name[0]
            self.name = name[1]
        elif len(name) == 1:
            self.name = name[0]
        if len(phone) != 0:
            self.phone = phone[1:]
        if len(email) != 0:
            self.email = email[1:]

    def ReadData(self):
        data = [self.surname, self.name, self.fathername, self.phone, self.email]
        return data


class Contact:
    def __init__(self):
        self.persons = []
        self.personfind = []
        self.file = None

    def EditFile(self):
        with open(self.file, mode="w", encoding='utf-8') as file:
            for line in self.persons:
                name = " ".join(x for x in (line.surname, line.name, line.fathername) if x)
                phone = line.phone
                email = line.email
                file.write(", ".join((x if x else "" for x in (name, phone, email))) + "\n")

    def GetPersonFind(self):
        return self.personfind

    def ReadFile(self, file=str()):
        self.file = file
        count = 0
        with open(file, encoding='utf-8') as text:
            for line in text:
                person = Person()
                person.line = count
                count += 1
                person.GetData(line)
                self.persons.append(person)

    def ReadPersonFind(self):
        for i in range(len(self.personfind)):
            person = self.personfind[i]
            for i in person.ReadData():
                if i is not None:
                    print(i, end=" ")
            print()

    def SearchByPhone(self, phone=str()):
        self.personfind = []
        WasThereNumber = False
        for i in range(len(self.persons)):
            if self.persons[i].phone == phone:
                self.personfind.append(self.persons[i])
                WasThereNumber = True
        if WasThereNumber is False:
            print("В ваших контактах нет такого номера")

    def SearchByEmail(self, email=str()):
        self.personfind = []
        WasThereEmail = False
        for i in range(len(self.persons)):
            if self.persons[i].email == email:
                self.personfind.append(self.persons[i])
                WasThereEmail = True
        if WasThereEmail is False:
            print("В ваших контактах нет человека с такой электронной почтой")

    def SearchByName(self, name):
        self.personfind = []
        WasThereName = False
        name = name.split()

        for i in self.persons:
            if all(map(lambda x: x in [i.name, i.surname, i.fathername], name)):
                self.personfind.append(i)
                WasThereName = True

        if not WasThereName:
            print("В ваших контактах нет человека с таким именем")

    def SearchPersonWithEmptyNumberOrEmail(self):
        self.personfind = []
        WasThereEmptyPhoneOrEmail = False
        for i in range(len(self.persons)):
            if self.persons[i].phone is None or self.persons[i].email is None:
                self.personfind.append(self.persons[i])
                WasThereEmptyPhoneOrEmail = True
        if WasThereEmptyPhoneOrEmail is False:
            print("В ваших контактах нет такого номера")
        else:
            print()

    def Edit(self):
        if len(self.personfind) == 1:
            operation = int(input("Что вы хотите отредактировать:\n 1)имя\n 2)телефон\n 3)адрес электронной почты: "))
            if operation == 1:
                name = input("Введите правильное имя: ")
                name = name.split()
                if len(name) == 1:
                    line = self.personfind[0].line
                    self.persons[line].name = name[0]
                    self.persons[line].surname = None
                    self.persons[line].farthername = None
                elif len(name) == 2:
                    line = self.personfind[0].line
                    self.persons[line].surname = name[0]
                    self.persons[line].name = name[1]
                    self.persons[line].farthername = None
                elif len(name) == 3:
                    line = self.personfind[0].line
                    self.persons[line].surname = name[0]
                    self.persons[line].name = name[1]
                    self.persons[line].farthername = name[2]
            elif operation == 2:
                phone = input("Введите правильный телефон")
                line = self.personfind[0].line
                self.persons[line].phone = phone
            elif operation == 3:
                email = input("Введите правильный адрес электронной почты: ")
                line = self.personfind[0].line
                self.persons[line].email = email
        elif len(self.personfind) > 1:
            print("Какой по счету контакт вы хотите отредактировать: ")
            for i in range(len(self.personfind)):
                person = self.personfind[i]
                print(str(i + 1) + ')', end=" ")
                for j in person.ReadData():
                    if j is not None:
                        print(j, end=" ")
                print()
            index = int(input())
            operation = int(input("Что вы хотите отредактировать:\n 1)имя\n 2)телефон\n 3)адрес электронной почты: "))
            if operation == 1:
                name = input("Введите правильное имя (фамилия имя отчество): ")
                name = name.split()
                if len(name) == 1:
                    line = self.personfind[index - 1].line
                    self.persons[line].name = name[0]
                    self.persons[line].surname = None
                    self.persons[line].fathername = None
                elif len(name) == 2:
                    line = self.personfind[index - 1].line
                    self.persons[line].surname = name[0]
                    self.persons[line].name = name[1]
                    self.persons[line].fathername = None
                elif len(name) == 3:
                    line = self.personfind[index - 1].line
                    self.persons[line].surname = name[0]
                    self.persons[line].name = name[1]
                    self.persons[line].fathername = name[2]
            elif operation == 2:
                phone = input("Введите правильный телефон: ")
                line = self.personfind[index - 1].line
                self.persons[line].phone = phone
            elif operation == 3:
                email = input("Введите правильный адрес электронной почты: ")
                line = self.personfind[index - 1].line
                self.persons[line].email = email

class Command:
    def __init__(self):
        self.command = None
        self.contact = None

    def GetCommand(self, command):
        self.command = command

    def GetContact(self, contact=Contact()):
        self.contact = contact

    def DoCommand(self, operation):
        if operation == 1:
            operation = int(input(
                "Найти человека по:\n 1) телефону\n 2) электронной почте\n 3) имени\n"
                " 4) незаполненной почте и (или) телефону: "))
            if operation == 1:
                phone = input("Введите номер телефона: ")
                self.contact.SearchByPhone(phone)
                self.contact.ReadPersonFind()
            elif operation == 2:
                email = input("Введите адрес электронной почты: ")
                self.contact.SearchByEmail(email)
                self.contact.ReadPersonFind()
            elif operation == 3:
                name = input("Введите имя (фамилия, имя, отчество): ")
                self.contact.SearchByName(name)
                self.contact.ReadPersonFind()
            elif operation == 4:
                self.contact.SearchPersonWithEmptyNumberOrEmail()
                self.contact.ReadPersonFind()
        elif operation == 2:
            operation = int(input("Найти человека по:\n 1) имени\n 2) адресу электронной почты\n 3) телефону: "))
            if operation == 1:
                self.contact.SearchByName(input("Введите имя: "))
                self.contact.Edit()
            elif operation == 2:
                self.contact.SearchByEmail(input("Введите адрес электронной почты: "))
                self.contact.Edit()
            elif operation == 3:
                self.contact.SearchByPhone(input("Введите номер телефона: "))
                self.contact.Edit()


file = input("Введите название файла: ")
MyContact = Contact()
MyContact.ReadFile(file)
command = Command()
command.GetContact(MyContact)
operation = str()
while operation != "нет":
    operation = int(
        input("Вы хотите 1) найти человека, 2) отредактировать контакт, 0) выйти из программы (введите цифру): "))
    if operation == 0:
        break
    else:
        command.DoCommand(operation)
    operation = input("хотите продолжить (да/нет): ")

MyContact.EditFile()
