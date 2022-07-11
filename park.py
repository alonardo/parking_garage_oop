import os

class Garage():   
    
    def __init__(self):     
        self.spot_taken = {
            1: False,
            2: False,
            3: False,
        }
        self.paid = {
            1: True,
            2: True,
            3: True
        }

    def assign_parking(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for spot, taken in self.spot_taken.items():
            if not taken:
                print('********************************************')
                print('')
                print(f"Please drive to parking spot number {spot}. Your ticket number is {spot}.")
                print('')
                print('********************************************')
                self.spot_taken[spot] = True
                self.paid[spot] = False

                print('Spots occupied:', self.spot_taken)
                print('Spots paid:', self.paid)
                print('')
                break
        else:
            print('********************')
            print('NO PARKING AVAILABLE')
            print('')
            print('********************************')
            print('')
            print('Spots occupied:', self.spot_taken)
            print('Spots paid:', self.paid)
            print('')
            print('********************************')
                        
    def pay_parking(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            try:
                spot = int(input("Please enter your ticket number and pay $1\n"))
                break
            except:
                print('Invalid ticket number, please enter your ticket number and pay $1')

        if spot not in self.spot_taken:
            print('Invalid ticket, try again.')
        else:
            print('********************************')
            print('')
            print('Please exit the garage, have a nice day.')
            print('')
            print('********************************')

            print(self.spot_taken[spot])
            print(self.paid[spot])

            self.spot_taken[spot] = False
            self.paid[spot] = True

            print('********************************')
            print('')
            print('Spots occupied:', self.spot_taken)
            print('Spots paid:', self.paid)
            print('')
            print('********************************')

class User_prompt():
    garage = Garage()

    @classmethod
    def main(cls):
        
        while True:
            prompt = input('What would you like to do? Park/Pay/Quit.\n').lower().strip()
            if prompt.lower() == 'park':
                cls.garage.assign_parking()
            elif prompt.lower() == 'pay':
                cls.garage.pay_parking()
            elif prompt.lower() == 'quit':
                break
            else:
                print('Invalid command. Try again.')   

if __name__ == "__main__":
    # Driver Code
    User_prompt.main()