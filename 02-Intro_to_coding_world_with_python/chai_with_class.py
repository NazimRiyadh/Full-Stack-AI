class Chai:
    def __init__(self, sweetness, liqour, milk):
        self.sweetness = sweetness
        self.liqour = liqour
        self.milk = milk
    
    def make_chai(self):
        print('Boil the water')
        print(f'add  {self.liqour} of liqour')
        print(f'add  {self.milk}')
        print(f'add  {self.sweetness} of sweetness')
        print('Stir and serve')

first_cha=Chai("1tsp", "less", "without milk")
first_cha.make_chai()


