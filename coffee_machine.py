class CoffeeMachine:
    actions = {
        'buy': 'buy',
        'fill': 'refill',
        'take': 'take',
        'remaining': 'print_status'
        # 'exit': self.quit
    }

    def __init__(self, water=400, milk=540, coffee=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.power_on = True

    def action(self, user_input):
        if user_input == 'buy':
            self.buy()
        elif user_input == 'fill':
            self.fill()
        elif user_input == 'take':
            self.take()
        elif user_input == 'remaining':
            self.print_status()
        elif user_input == 'exit':
            self.quit()
        return None

    def buy(self):
        coffee_options = {
            1: (250, 0, 16, 4),  # espresso
            2: (350, 75, 20, 7),  # latte
            3: (200, 100, 12, 6)  # cappuccino
        }
        print('What do you want ot buy? 1 - espresso, 2 - latte, 3 - cappuccino:, '
              'back - to main menu:')
        user_input = input()
        if user_input == 'back':
            return
        choice = coffee_options.get(int(user_input))
        if machine.water < choice[0]:
            print('Sorry, not enough water!')
        elif machine.milk < choice[1]:
            print('Sorry, not enough milk!')
        elif machine.coffee < choice[2]:
            print('Sorry, not enough coffee beans!')
        elif machine.cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            machine.water -= choice[0]
            machine.milk -= choice[1]
            machine.coffee -= choice[2]
            machine.money += choice[3]
            machine.cups -= 1

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee += int(input())
        print('Write how many cups of coffee do you want to add:')
        self.cups += int(input())

    def take(self):
        print('I gave you ', self.money)
        self.money = 0

    def print_status(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffee, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.money, 'of money')

    def quit(self):
        self.power_on = False


machine = CoffeeMachine()

while machine.power_on:
    print('Write action (buy, fill, take, remaining, exit):')
    machine.action(input())
