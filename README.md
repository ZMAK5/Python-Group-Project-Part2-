# Python-Group-Project-Part2-
# Destiny Predictor Simulator (Advanced Python Version)

## Project Description

This console application, the **Destiny Predictor Simulator**, is the advanced version of the part1 Python program designed to collect various personal and "mystic" inputs from the user and calculate a unique **Final Destiny Score** and a **Lucky Year**.

The program is structured using **Object-Oriented Programming (OOP)** principles and incorporates advanced Python concepts such as functions, loops, conditional logic, and data structures to provide a robust and reusable application. It also features a main loop for **replayability**, allowing the user to run multiple predictions without restarting the script.

## Installation and Execution

### Prerequisites

You only need a working installation of Python 3.x.

### Steps

1.  **Save the Code:** Save the provided Python code into a file named `destiny_predictor.py`.
2.  **Run the Program:** Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:

    ```bash
    python3 Part2.py
    ```

3.  **Follow the Prompts:** The program will guide you through 10 input prompts. After the prediction is displayed, you will be asked if you wish to run another prediction.

## Advanced Python Concepts Used

This project serves as a comprehensive demonstration of modern Python programming techniques:

### 1. Object-Oriented Programming (OOP)

*   **Class (`DestinyPredictor`):** Encapsulates all data (user inputs, scores) and logic (methods) related to a single prediction session.
*   **Object Instantiation:** A new `DestinyPredictor` object is created for each prediction run, ensuring data isolation and clean state management.
*   **Attributes (`self.`):** All user inputs and calculated results are stored as instance attributes, making them accessible across all methods of the class.

### 2. Functions and Modularity

*   **Methods (`collect_inputs`, `calculate_destiny`, `generate_output`):** The code is organized into clear, single-responsibility methods, improving readability and maintainability.
*   **Main Function (`main()`):** Serves as the program's entry point, managing the overall flow and replay loop.

### 3. Control Structures

*   **`while` Loops (Replayability):** The `main()` function uses a `while True` loop to continuously run the prediction until the user explicitly chooses to exit.
*   **`while` Loops (Input Validation):** The private method `_get_validated_input` uses a `while` loop combined with `try/except` blocks to repeatedly prompt the user until a valid input (correct type and range) is provided.
*   **Conditional Logic (`if/elif/else`):** Used extensively in `calculate_destiny` to:
    *   Apply different bonus scores based on user choices (e.g., `has_amulet`).
    *   Select the appropriate prophecy message from the dictionary based on the calculated score range.

### 4. Data Structures

*   **Dictionaries (`PROPHECY_MESSAGES`):** Used to store and manage the prophecy text dynamically. This allows the program to select a message based on the score without hardcoding complex conditional statements for every possible outcome.

## Technical Details

| Feature | Implementation |
| :--- | :--- |
| **Minimum Inputs** | 10 inputs are collected, demonstrating extensive use of `input()`. |
| **Type Casting** | `int()` and `float()` are used within the validation loop to safely convert user input. |
| **Arithmetic Expressions** | Multiple expressions are used to calculate `final_destiny_score` and `lucky_year`. |
| **Replayability** | Implemented via the `main()` function's `while` loop. |
| **Language** | All code, comments, and user prompts are in English. |
