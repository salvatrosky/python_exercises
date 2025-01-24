# Python Exercises

This repository contains two Python exercises designed to demonstrate data processing and algorithm implementation

---

## **Exercise 1: Generate IP Traffic Report**

### **Overview**
This exercise generates a traffic report per IP address based on a log file. The report includes details such as the number of requests, the percentage of total requests, the total bytes sent, and the percentage of the total amount of bytes.

### **Assumptions**
- The input file does not have headers, so the analysis starts from the first line.
- According to RFC 2616, status `OK` is only `200`, although in practice, any `2xx` status could indicate a successful request.
- The file does not contain empty lines, and all fields are present in every line.
- The output file must be named `/logfiles/requests.log`. However, in the case of JSON format, the extension was changed for clarity.
- All provided directories (e.g., `logfiles/` and `reports/`) are assumed to be relative to the project root directory, not the root of the computer's file system.

### **Features**
- Reads a log file with semicolon-separated values.
- Excludes entries where the HTTP status is not `200` (OK).
- Calculates statistics for each unique IP address.
- Supports output in both `CSV` and `JSON` formats.
- Outputs the data sorted by the number of requests (descending).

### **Input Format**
The input file (`requests.log`) contains the following fields:
- `TIMESTAMP`: The moment when the event occurred.
- `BYTES`: The number of bytes sent to the client.
- `STATUS`: The HTTP response status.
- `REMOTE_ADDR`: The IP address of the client.

Each field is separated by a semicolon (`;`).

### **Output Format**
- **CSV**: A semicolon-separated file with headers:
  - `IP Address`
  - `Number of Requests`
  - `Percentage of Total Requests`
  - `Total Bytes Sent`
  - `Percentage of Total Bytes`

- **JSON**: An array of JSON objects with fields:
  - `ip_address`
  - `requests`
  - `request_percentage`
  - `total_bytes`
  - `bytes_percentage`

### **How to Run**
```bash
python3 src/exercise_1.py <input_file> <output_file> <format>
```

#### **Example**
```bash
python3 src/exercise_1.py logfiles/requests.log reports/ipaddr csv
```

---

## **Exercise 2: Multiplication Using Addition**

### **Overview**
This exercise implements a method to multiply integer numbers using the addition operator (`+`) instead of the multiplication operator (`*`), while storing the values in arrays. For example, to calculate `15 × 2`, you would store these values in two arrays to perform the operation.

### **Features**
- Implements array-based arithmetic to handle large numbers.
- Multiplies two numbers efficiently using repeated addition.
- Calculates factorial values using the same array-based approach.

### **Functions**
#### **1. Factorial**
- Calculates the factorial of a number (`n!`) using repeated addition.
- Handles large numbers by representing results as arrays of digits.

#### **2. Multiply Numbers**
- Multiplies two integers, including negative values.
- Uses array-based arithmetic to handle large results.

### **How to Run**
```bash
python3 src/exercise_2.py <operation> [arguments]
```

#### **Operations**
- **Factorial**:
  ```bash
  python3 src/exercise_2.py factorial <number>
  ```
  Example:
  ```bash
  python3 src/exercise_2.py factorial 10
  ```

- **Multiply**:
  ```bash
  python3 src/exercise_2.py multiply <number1> <number2>
  ```
  Example:
  ```bash
  python3 src/exercise_2.py multiply -10 3
  ```

---

## **Running Tests**
The repository includes unit tests for both exercises. To run all tests:
```bash
python3 -m unittest discover tests
```

---

## **Menu Script**
A Bash script (`menu_script.sh`) is included to provide an interactive way to execute the exercises or run the tests.

### **Usage**
```bash
bash python_exercises/menu_script.sh
```

### **Menu Options**
1. Execute Exercise 1
2. Execute Exercise 2
3. Run Tests
4. Exit

---

## **License**
This repository is open-sourced and available under the MIT License.

