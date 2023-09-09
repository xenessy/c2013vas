import random


class Human:
    def __init__(self, name="Vasya", job=None, car=None, home=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel <20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print('delicacies!!!')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 15
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strenght += 100
        self.money -= 50

    def day_indexes(self, day):
        day = f"Today is {day} of {self.name}`s life"
        print(f'{day:=^50}', "\n")
        human_indexes = self.name + "`s indexes"
        print(f'{human_indexes:^50}', "\n")
        print(f"Money - {self.money}")
        print(f'Satitety - {self.satiety}')
        print(f"Gladness- {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f'Mess - {self.home.mess}')
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strenght - {self.car.strenght}")


    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety < 0:
            print("Dead")
            return False
        if self.money < -500:
            print('Bankrupt')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()
        self.day_indexes(day)
        dice = random.randint(1, 4)
        if dice == 1:
            print('Time to chill')
            self.chill()
            if dice == 2:
                print('Time to work')
                self.work()
        if dice == 3:
            print('Time to clean')
            self.clean_home()
        if dice == 4:
            print('Time to tread')
            self.shopping(manage="delicacies")

class Auto:
     def __init__(self, brand_list):
         self.brand = random.choice(list(brand_list))
         self.fuel = brand_list[self.brand]["fuel"]
         self.strenght = brand_list[self.brand]["strenght"]
         self.consumption= brand_list[self.brand]["consumption"]

     def drive(self):
         if self.strenght > 0 and self.fuel>=self.consumption:
             self.fuel -= self.consumption
             self.strenght -= 1
             return True
         else:
             print("The car cannot move")
             return False

brands_of_car = {
    "BMW": {"fuel": 90, "strenght": 130, "consumption": 6},
    "Lada": {"fuel": 50, "strenght": 40, "consumption": 10},
    "Mercedes": {"fuel": 70, "strenght": 150, "consumption": 8},
    "Ferarri": {"fuel": 80, "strenght": 160, "consumption": 14}
}

class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

job_list = {
    "Java dev": {"salary": 50, "gladness_less": 10},
    "Python dev": {"salary": 40, "gladness_less": 3},
    "C++ dev": {"salary": 45, "gladness_less": 25},
    "Rust dev": {"salary": 70, "gladness_less": 1}
}

hum = Human(name='Vasya')

for day in range(1, 8):
    if hum.live(day) == False:
        break