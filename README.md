# Truth Table Generator and Quine-McCluskey Minimization

This project provides a graphical user interface (GUI) for generating truth tables and performing the Quine-McCluskey minimization for Boolean expressions. The project is built using Python's `tkinter` library.

## Features

- **Truth Table Generator**: Allows the user to input variables and logical functions (AND, OR, NOT, or custom lambda functions) and generate a truth table.
- **Quine-McCluskey Minimization**: A tool to minimize Boolean expressions using the Quine-McCluskey algorithm. The user can input minterms and get the minimized Boolean expression.

## Requirements

- Python 3.x
- `tkinter` (which is included by default in most Python installations)
- No additional dependencies required for this project

## Running the Project

1. Clone or download the repository to your local machine.
2. Make sure you have Python 3 installed.
3. Run the project by executing `main.py`.

### Step-by-step to run the application:

1. **Open a terminal/command prompt** and navigate to the folder where you downloaded the project.
2. **Run the `main.py` file**:
   ```bash
   python main.py

This will launch the menu window, where you can select between:

- **Truth Table Generator**: For generating truth tables.
- **Quine-McCluskey Minimization**: For minimizing Boolean expressions.

### Truth Table Generator
1. **Enter Variables**: Input the Boolean variables, separated by commas (e.g., `A, B, C`).
2. **Enter Functions**: Define the logical functions to be used in the truth table. Supported functions are:
   - `and`: Logical AND
   - `or`: Logical OR
   - `not`: Logical NOT
   - **Custom Lambda Functions**: You can also input your custom lambda expressions, for example: `lambda a, b: a and b`
3. **Enter Column Names**: Define custom names for the columns that will appear in the truth table.
4. **Click "Generate Truth Table"**: This will calculate and display the truth table based on the input variables, functions, and column names.

### Quine-McCluskey Minimization
1. **Enter Minterms**: Input the minterms as space-separated values (e.g., `1 3 7`).
2. **Click "Process"**: The program will process the minterms and display the Quine-McCluskey minimization, showing:
   - Prime Implicant Chart
   - Essential Prime Implicants (EPI)
   - The minimized Boolean expression.

## Screenshots

### Menu Screen
![Menu](https://imgur.com/rJgE8un.png)

### Truth Table Generator
![Truth Table Generator](https://imgur.com/yksUCRl.png)

### Quine-McCluskey Minimization
![Quine McCluskey Minimization](https://imgur.com/svk5XUD.png)

## Troubleshooting

### Error: "Invalid input"
If you encounter an "Invalid input" error, ensure that:
- The variables are entered as comma-separated values (e.g., `A, B, C`).
- The logical functions are correctly entered as `and`, `or`, `not`, or lambda functions.
- Minterms are provided as space-separated integers (e.g., `1 3 7`).

### Common Issues

1. **No output or blank result**:
   - Ensure that all required fields are filled out correctly before pressing the generate/process button.
   - If you encounter any issues, check the console for error messages.

2. **Incorrect Lambda Syntax**:
   - Ensure that the lambda functions are entered correctly, starting with `lambda` followed by the function body, such as `lambda a, b: a and b`.

