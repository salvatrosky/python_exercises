import csv
import os
import json
from http import HTTPStatus
import logging
import sys

logging.basicConfig(level=logging.INFO, format='\n%(message)s\n')


def process_log_file(input_file, output_dir, output_format="csv"):
    data = {}
    total_requests = 0
    total_bytes = 0

    with open(input_file, "r") as file:
        for line in file:
            try:
                _, bytes_sent, status, remote_addr = line.strip().split(';')

                if int(status) != HTTPStatus.OK:
                    continue

                if remote_addr not in data:
                    data[remote_addr] = {"requests": 0, "bytes_sent": 0}

                total_requests += 1
                total_bytes += int(bytes_sent)
                data[remote_addr]["requests"] += 1
                data[remote_addr]["bytes_sent"] += int(bytes_sent)
            except ValueError:
                logging.warning(f"Invalid line format ignored: {line.strip()}")
                continue

    report = []
    for ip, values in data.items():
        requests = values["requests"]
        bytes_sent = values["bytes_sent"]
        request_percentage = round((requests / total_requests) * 100, 2)
        bytes_percentage = round((bytes_sent / total_bytes) * 100, 2)
        report.append((ip, requests, request_percentage,
                      bytes_sent, bytes_percentage))

    report.sort(key=lambda x: x[1], reverse=True)

    return create_report_file(output_dir, report, output_format)


def create_report_file(output_file, report, output_format="csv"):
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    headers = ["IP Address", "Requests number",
               "Percentage", "Bytes sent", "Bytes percentage"]
    if output_format == "csv":
        return create_csv_file(output_file, report, headers)
    elif output_format == "json":
        return create_json_file(output_file, report, headers)


def create_csv_file(output_file, report, headers):
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(headers)

        for row in report:
            writer.writerow(row)

    return writer


def create_json_file(output_file, report, headers):
    json_headers = [header.lower().replace(" ", "_") for header in headers]
    with open(output_file, "w") as file:
        data = [
            {
                json_headers[0]: ip,
                json_headers[1]: requests,
                json_headers[2]: request_percentage,
                json_headers[3]: bytes_sent,
                json_headers[4]: bytes_percentage
            } for ip, requests, request_percentage, bytes_sent, bytes_percentage in report
        ]

        json.dump(data, file, indent=4)

    return data


if __name__ == "__main__":
    if len(sys.argv) < 4:
        logging.error(
            "Usage: python script.py <input_file> <output_file> <output_format>")
        logging.info(
            "Example: python script.py data/requests.log data/ipaddr.csv csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_name_file = sys.argv[2]
    output_format = sys.argv[3]

    if output_format not in ["csv", "json"]:
        logging.error("Invalid output format. Use 'csv' or 'json'.")
        sys.exit(1)

    output_file = f'./reports/{output_name_file}.{output_format}'
    try:
        process_log_file(input_file, output_file, output_format)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)
