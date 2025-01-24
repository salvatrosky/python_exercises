import os
import unittest
import json
import csv

from python_exercises.src.exercise_1 import process_log_file


class TestProcessLogFile(unittest.TestCase):

    def setUp(self):
        self.input_file = "test_requests.log"
        self.output_dir = "test_reports"
        self.csv_output_file = os.path.join(self.output_dir, "ipaddr.csv")
        self.json_output_file = os.path.join(self.output_dir, "ipaddr.json")

        with open(self.input_file, "w") as file:
            file.write("2025-01-01T00:00:01;1024;200;192.168.1.1\n")
            file.write("2025-01-01T00:00:02;512;200;192.168.1.2\n")
            file.write("2025-01-01T00:00:03;256;404;192.168.1.3\n")
            file.write("2025-01-01T00:00:04;128;200;192.168.1.1\n")

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)

    def test_csv_output(self):
        process_log_file(self.input_file, self.csv_output_file, "csv")
        self.assertTrue(os.path.exists(self.csv_output_file))

        with open(self.csv_output_file, "r") as file:
            reader = csv.reader(file, delimiter=";")
            rows = list(reader)

        # Check headers
        self.assertEqual(
            rows[0], ["IP Address", "Requests number", "Percentage", "Bytes sent", "Bytes percentage"])

        # Check data rows
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[1], ["192.168.1.1", "2", "66.67", "1152", "69.23"])
        self.assertEqual(rows[2], ["192.168.1.2", "1", "33.33", "512", "30.77"])

    def test_json_output(self):
        process_log_file(self.input_file, self.json_output_file, "json")
        self.assertTrue(os.path.exists(self.json_output_file))

        with open(self.json_output_file, "r") as file:
            data = json.load(file)

        # Check data format
        self.assertEqual(len(data), 2)  # Only 2 valid IPs
        self.assertEqual(data[0]["ip_address"], "192.168.1.1")
        self.assertEqual(data[0]["requests_number"], 2)
        self.assertEqual(data[0]["percentage"], 66.67)


if __name__ == "__main__":
    unittest.main()
