import re

# Sample log lines
with open('/var/log/freeradius/radius.log', 'r') as file:
    log_lines = file.readlines()

# Initialize a dictionary to count login attempts per IP
ip_attempts = {}

# Regular expression to match the IP address in the log line
ip_regex = r'cli\s([\d.]+)'

for line in log_lines:
    # Search for IP addresses in the log line
    match = re.search(ip_regex, line)
    if match:
        ip_address = match.group(1)
        # Increment the count for the IP address
        if ip_address in ip_attempts:
            ip_attempts[ip_address] += 1
        else:
            ip_attempts[ip_address] = 1

# Filter IP addresses with more than 5 incorrect login attempts
suspicious_ips = {ip: count for ip, count in ip_attempts.items() if count > 10}
sorted_ips = sorted(suspicious_ips.items(), key=lambda x: x[1], reverse=True)


print("IP Addresses with more than 10 incorrect login attempts, sorted by attempts:")
for ip, count in sorted_ips:
    # Use the str.format() method for Python 3.5 compatibility
    print("{}: {} attempts".format(ip, count))
