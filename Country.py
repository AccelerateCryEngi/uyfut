class Country:
    global collector, colDict
    collector = []
    colDict = {}
    def __init__(self, country, capital, population, area):
        self.country = country
        self.capital = capital
        self.population = population
        self.area = area
        collector.append(self)
        colDict[country] = capital
        colDict[capital] = country

    def __str__(self, prioriteted='страна'):
        return 'Страна: {:25} Столица: {:30} Население: {:30} Площадь: {:30}'.format(self.country, self.capital,
                                                                                     self.population, self.area)
if __name__ == '__main__':
    with open('данные.txt') as infile:
        a = infile.readlines()
    f = open('страны.txt', 'a')
    for item in a:
        try:
            print(Country(*item.split()), file=f)
        except TypeError:
            print(Country(*([' '.join(item.split()[:2])] + item.split()[2:])), file=f)
    print('-' * 80)

    import sys
    if '-d' in sys.argv:
        while True:
            print(colDict[input('Название страны или столицы: ')])

    collector.sort(key=lambda x: int(x.population), reverse=True)
    f = open('население.txt', 'a')
    for item in collector:
        print('Население: {:>10} Страна: {:20} Столица: {:20} Площадь: {:15}'.format(item.population, item.country, item.capital, item.area), file=f)
    f.close()
    print('-' * 80)

    f = open("площадь.txt", 'a')
    for item in sorted(collector, key=lambda x: int(x.area)):
        print('Площадь: {:>10} Страна: {:20} Столица: {:20} Население: {:15} '.format(item.area, item.country, item.capital, item.population), file=f)
    f.close()