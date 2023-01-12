import math

DecreChar = 0.03 #Уменьшение характеристик каждый ход
DecreType = 0.05 #Уменьшение в зависимости от типа питомца

#Объявление класс Tpet
def GameStart():
    class Tpet():
        def __init__(self, type, name):
            self.type = type
            self.name = name
            self.photo = ''
            self.thirst = 0.8 + DecreChar
            self.weight = 0.8 + DecreChar
            self.happiness = 0.8 + DecreChar
            self.year = 1
            self.game = True

        def food(self):
            if (pet.weigth < 10.00) and (pet.weigth > 0):
                if 10 - pet.weigth < 9.85 :
                    pet.weigth = pet.weigth + 0.25
                    pet.thirst = pet.thirst - 0.06
            else: print('Не хочет кушать')

        def water(self):
            if (pet.thirst < 10.00) and (pet.thirst > 0):
                if (10 - pet.weigth) < 9.85 :
                    pet.thirst = pet.thirst + 0.25
                    pet.weigth = pet.weigth - 0.07
                else:
                    (pet.thirst) = (10-pet.thirst)
            else: print('Не хочет пить')

        def play(self):
            if (pet.happiness < 10.00) and (pet.happiness > 0):
                if (10 - pet.happiness) < 9.85 :
                    pet.happiness = pet.happiness + 0.25
                    pet.thirst = pet.thirst - 0.07
                    pet.weigth = pet.weigth - 0.06
                else:
                    pet.happiness = (10 - pet.happiness)
            else:
                print(pet.name, 'Не хочет играть')

        def ignore(self):
            pet.weigth = pet.weigth
            pet.thirst = pet.thirst
            pet.happiness = pet.happiness

        def LeaveGame(self):
            print('')
            print('Вывод: Не заводи питомца')
            print('')
            pet.game = False

    def ChooseAction(action):
        if action == '1':
            pet.food()
        elif action == '2':
            pet.water()
        elif action == '3':
            pet.play()
        elif action == '4':
            pet.ignore()
        elif action == '5':
            pet.LeaveGame()
        else:
            print('Недопустимое действие')

    print('Выберите имя питомцу:')
    name = input()
    print('')
    check = False

    while check == False:
        print('Выберите тип питомца 1:собака 2:кошка 3:крыса')
        type = input()
        pet = Tpet(type,name)
        if type == '1':
            photo = '(V._.V)'
            check = True
        elif type == '2':
            photo = '(^._.^)'
            check = True
        elif type == '3':
            photo = '<:З )~'
            check = True
        else: print('Тип недоступен.')
        print('')

    pet = Tpet(type,name)
    pet.photo = photo

    pet.year = 1
    pet.thirst = 8.00 + DecreChar
    pet.weight = 8.00 + DecreChar
    pet.happiness = 8.00 + DecreChar

    while (pet.game == True) and ((pet.weight > 0) and (pet.thirst > 0) and (pet.happiness > 0) and (pet.year < 13)):
        age = pet.year + 0.05
        pet.year = math.trunc(age)
        pet.weight = pet.weight - DecreChar
        pet.thirst = pet.thirst - DecreChar
        pet.happiness = pet.happiness - DecreChar
        if pet.type == '1':
            pet.happiness = pet.happiness - DecreType
        elif pet.type == '2':
            pet.thirst = pet.thirst - DecreType
        else: pet.weight = pet.weight - DecreType

        print('------------------------------------')
        print('')
        print(pet.photo)
        print('')
        print('------------------------------------')
        print('| Возвраст | Вес | Жажда | Счастье |')
        print('------------------------------------')
        print('| ', round(pet.year,2),'| ', round(pet.weight,2), ' | ', round(pet.thirst,2), ' | ', round(pet.happiness,2),' |')
        print('------------------------------------')
        print('Выберите действие : 1: Есть 2: Пить воду 3: Играть с ',pet.name,' 4: Игонрировать 5: Остановить игру. ')
        print('')
        action = input()
        ChooseAction(action)
        print('')

        if (pet.weight <= 0) or (pet.thirst <= 0) or (pet.happiness <= 0) or (pet.year >= 13):
            print(pet.name, 'Погиб...')

        print('')

def Instuctions():
    print()
    print()
    print('Инструкция: ')
    print()
    print('КОНЕЦ ИНСТРУКЦИИ')

def MenuStart():
    print('')
    print('Добро пожаловать')
    menu = False
    while not menu:
        print('Выберите один вариант 1: Играть 2: Инструкция 3: Выйти')
        option = input()
        if option == '1':
            GameStart()
        elif option == '2':
            Instuctions()
        elif option == '3':
            menu = True
        else: print('Введите доступный вариант')

MenuStart()

