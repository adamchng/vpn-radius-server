from flask import Flask
import re

app = Flask(__name__)

# Path to the log file that's constantly updated
LOG_FILE_PATH = '/var/log/freeradius/radius.log'

def process_log_file(filepath):
    ip_attempts = {}
    ip_regex = r'cli\s([\d.]+)'
    with open(filepath, 'r') as file:
        for line in file:
            match = re.search(ip_regex, line)
            if match:
                ip_address = match.group(1)
                ip_attempts[ip_address] = ip_attempts.get(ip_address, 0) + 1
    return [ip for ip, count in ip_attempts.items() if count > 10]

@app.route('/')
def show_suspicious_ips():
    suspicious_ips = process_log_file(LOG_FILE_PATH)
    return '<br>'.join(suspicious_ips)

if __name__ == '__main__':
    app.run(debug=True)
