import sys

def run_converter():
   
    while True:
        print("\n" + "="*30)
        print(" KMUTT ENGINEERING CONVERTER ")
        print("="*30)
        print("1. Celsius to Fahrenheit")
        print("2. Meters to Feet")
        print("Q. Quit Program")
        
        choice = input("\nSelect an option (1, 2, or Q): ").strip().upper()

        if choice == '1':
            try:
                c = float(input("Enter Celsius value: "))
                f = (c * 9/5) + 32
                print(f">>> Result: {c}C is {f:.2f}F")
            except ValueError:
                print(" ERROR: Please enter a number, not text.")

        elif choice == '2':
            try:
                m = float(input("Enter Meters value: "))
                ft = m * 3.28084
                print(f">>> Result: {m}m is {ft:.2f}ft")
            except ValueError:
                print(" ERROR: Please enter a number, not text.")

        elif choice == 'Q':
            print("Exiting... Sawatdee kha!")
            break 
            
        else:
            print(" INVALID CHOICE. Please try again.")


if __name__ == "__main__":
    run_converter()

