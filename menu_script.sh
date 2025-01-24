#!/bin/bash
# Set PYTHONPATH to the project root directory
export PYTHONPATH=$(cd .. && pwd)

# Function to display the menu
show_menu() {
  echo "Choose an exercise to execute:"
  echo "1) Exercise 1 - Generate IP report"
  echo "2) Exercise 2 - Calculate factorial or multiply numbers"
  echo "3) Run Tests"
  echo "4) Exit"
  echo -n "Enter your choice: "
}

# Function to execute Exercise 1
execute_exercise_1() {
  echo -n "Enter the input file path (default: ./logfiles/requests.log): "
  read input_file
  input_file=${input_file:-./logfiles/requests.log}

  echo -n "Enter the name of the output file (default: ipaddr.(csv/json)): "
  read output_file
  output_file=${output_file:-ipaddr}

  echo -n "Enter the output format (csv/json) (default: csv): "
  read format
  format=${format:-csv}

  echo
  echo "Running Exercise 1 with the following parameters:"
  echo "Input File: $input_file"
  echo "Output File: $output_file"
  echo "Format: $format"

  python3 src/exercise_1.py "$input_file" "$output_file" "$format"
}

# Function to execute Exercise 2
execute_exercise_2() {
  echo "Choose the operation to perform:"
  echo "1) Factorial"
  echo "2) Multiply"
  echo -n "Enter your choice (1/2): "
  read operation

  if [ "$operation" = 1 ]; then
    echo -n "Enter the number to calculate the factorial: "
    read n
    python3 src/exercise_2.py factorial "$n"
  elif [ "$operation" = 2 ]; then
    echo -n "Enter the first number: "
    read num1
    echo -n "Enter the second number: "
    read num2
    python3 src/exercise_2.py multiply "$num1" "$num2"
  else
    echo "Invalid operation. Please choose 'factorial' or 'multiply'."
  fi
}

# Function to execute tests
run_tests() {
  echo "Running all tests..."
  python3 -m unittest discover tests
}

# Main script loop
while true; do
  show_menu
  read choice

  case $choice in
    1)
      execute_exercise_1
      ;;
    2)
      execute_exercise_2
      ;;
    3)
      run_tests
      ;;
    4)
      echo "Exiting the script."
      exit 0
      ;;
    *)
      echo "Invalid choice. Please try again."
      ;;
  esac

done
