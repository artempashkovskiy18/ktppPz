class Excursion:
    __excursions = list()
    lastId = 0

    def __init__(self, date, time, phone, peopleAmount):
        self.id = Excursion.lastId
        self.date = date
        self.time = time
        self.phone = phone
        self.peopleAmount = peopleAmount
        Excursion.lastId += 1

    @staticmethod
    def addExcursion(excursion):
        Excursion.__excursions.append(excursion)

    @staticmethod
    def excursions():
        return Excursion.__excursions

    @staticmethod
    def excursionsToString():
        str = ""
        for e in Excursion.__excursions:
            str += e.toString()
        return str

    def toString(self):
        return "id = {0} date = {1}, time = {2}, phone = {3}, peopleAmount = {4} \n"\
            .format(self.id, self.date, self.time, self.phone, self.peopleAmount)
