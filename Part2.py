# --- 1. DATA STRUCTURES ---
# Dictionary for prophecy messages based on the final score range
PROPHECY_MESSAGES = {
    "LOW": "A solid path lies ahead. Trust your instincts and remain vigilant.",
    "MEDIUM": "Your destiny is guided by your own inner strength. Opportunities await.",
    "HIGH": "The stars align perfectly for you! Great fortune and success await.",
    "CRITICAL": "A rare cosmic event grants you unparalleled luck. Seize the day!"
}

# --- 2. CLASS AND OOP ---
class DestinyPredictor:
    """
    Represents the Destiny Prediction Simulator.
    Encapsulates user data and calculation methods.
    """
    def __init__(self):
        # Initialize object attributes
        self.user_name = ""
        self.birth_day = 0
        self.lucky_number = 0
        self.cosmic_factor = 0.0
        self.has_amulet = False
        self.favorite_color = ""
        self.mystic_choice = 0
        self.energy_level = 0
        self.birth_month = 0
        self.birth_year = 0
        
        self.final_destiny_score = 0.0
        self.lucky_year = 0
        self.prophecy_message = ""

    # --- 3. FUNCTIONS AND LOOPS ---
    def _get_validated_input(self, prompt, input_type=int, min_val=None, max_val=None):
        """
        Function to get a validated user input using a 'while' loop and 'try/except'.
        """
        while True:
            try:
                value = input_type(input(prompt))
                # Use 'if' conditions to check boundaries
                if (min_val is not None and value < min_val) or \
                   (max_val is not None and value > max_val):
                    print(f"Error: Value must be between {min_val} and {max_val}.")
                    continue
                return value
            except ValueError:
                print("Error: Invalid input type. Please try again.")

    def collect_inputs(self):
        """
        Collects all user inputs.
        """
        print("\n--- Input Collection ---")
        
        # 1. STR Input
        self.user_name = input("1. Enter your full name: ")
        self.favorite_color = input("2. What is your favorite color? ")
        
        # 3-7. INT Inputs (with int() conversion)
        self.birth_day = self._get_validated_input("3. What is your birth day (1-31)? ", min_val=1, max_val=31)
        self.lucky_number = self._get_validated_input("4. Choose a lucky number (1-99): ", min_val=1, max_val=99)
        self.mystic_choice = self._get_validated_input("5. Enter 1 for Wisdom or 2 for Strength: ", min_val=1, max_val=2)
        self.energy_level = self._get_validated_input("6. On a scale of 1 to 10, what is your current energy level? ", min_val=1, max_val=10)
        self.birth_month = self._get_validated_input("7. What is your birth month (1-12)? ", min_val=1, max_val=12)
        
        # 8-9. FLOAT Inputs (with float() conversion)
        self.cosmic_factor = self._get_validated_input("8. Enter your cosmic factor (decimal, e.g., 1.25): ", input_type=float)
        self.luck_multiplier = self._get_validated_input("9. Enter a luck multiplier (e.g., 0.8 or 1.5): ", input_type=float)
        
        # 10. BOOL Input
        has_amulet_str = input("10. Do you wear a protective amulet (yes/no)? ").lower()
        self.has_amulet = (has_amulet_str == "yes")

    # --- 4. FUNCTIONS AND CONDITIONS ---
    def calculate_destiny(self):
        """
        Calculates the destiny score, lucky year, and selects the prophecy message.
        """
        # Calculate base score 
        base_score = (self.birth_day * self.cosmic_factor) + (self.lucky_number / 10.0)
        
        # Conditional Bonus 
        bonus = 0.0
        if self.has_amulet:
            bonus = 15.0 # High bonus for amulet
        elif self.mystic_choice == 1:
            bonus = 8.0 # Medium bonus for Wisdom
        else:
            bonus = 3.0 # Low bonus for Strength
            
        # Calculate final score 
        self.final_destiny_score = (base_score + bonus) * self.luck_multiplier
        
        # Calculate lucky year (Arithmetic Expression 3 - Guaranteed >= 2025)
        shift = (self.birth_day + self.lucky_number) % 10
        self.lucky_year = 2025 + shift
        
        # Select prophecy message based on score (Conditions and Dictionaries)
        if self.final_destiny_score > 60:
            self.prophecy_message = PROPHECY_MESSAGES["CRITICAL"]
        elif self.final_destiny_score > 40:
            self.prophecy_message = PROPHECY_MESSAGES["HIGH"]
        elif self.final_destiny_score > 20:
            self.prophecy_message = PROPHECY_MESSAGES["MEDIUM"]
        else:
            self.prophecy_message = PROPHECY_MESSAGES["LOW"]

    def generate_output(self):
        """
        Displays the final prophecy summary.
        """
        print("\n" + "="*60)
        print(f"*** DESTINY PROPHECY FOR {self.user_name.upper()} ***")
        print("="*60)
        
        # Display key results
        print(f"Your calculated Destiny Score is {self.final_destiny_score:.2f} points.")
        print(f"Your luckiest year will be {self.lucky_year}.")
        print(f"Your soul color is {self.favorite_color}.")
        
        # Display conditional message
        print(f"\nProphecy: {self.prophecy_message}")
        
        print("="*60)

# --- 5. MAIN PROGRAM LOOP ---
def main():
    """
    Main function that handles the replay loop.
    """
    print("****** Welcome to the Advanced Destiny Predictor Simulator! ******")
    
    # 'while' loop for replayability
    while True:
        predictor = DestinyPredictor()
        
        predictor.collect_inputs()
        predictor.calculate_destiny()
        predictor.generate_output()
        
        # Ask user if they want to play again
        play_again = input("\nDo you want to predict another destiny (yes/no)? ").lower()
        if play_again != 'yes':
            break
            
    print("\nThank you for using the Destiny Predictor. Goodbye!")

# --- 6. PROGRAM ENTRY POINT ---
if __name__ == "__main__":
    main()
