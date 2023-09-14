# Network Scanner

This Python script provides functionality to scan two local subnets (`192.168.0.*` and `192.168.1.*`) to determine which IP addresses are active and then fetches the associated hostnames.

## Features

- Concurrently ping a range of IP addresses.
- Display active IP addresses along with their hostnames.
- Utilizes Python's `multiprocessing` for concurrent pinging.

## Prerequisites

You will need the following Python libraries:

- `socket`
- `os`
- `platform`
- `subprocess`
- `multiprocessing`
- `wmi` (for Windows)

You can install the necessary libraries using `pip`:

```bash
pip install wmi
```

## How to Use

1. Ensure you have all the necessary libraries installed.
2. Run the script:

```shell
python network_scanner.py
```

1. The script will ping IP addresses in the `192.168.0.*` and `192.168.1.*` ranges and display the active IPs with their associated hostnames.

## Code Overview

The script consists of several functions:

- `format_ips(hostnames, ip_list)`: Formats and prints the IP addresses and their associated hostnames.
- `get_hostname(ip_list)`: Fetches the fully qualified domain names for a given list of IP addresses.
- `ping(ip)`: Pings a single IP address.
- `pool(ip)`: Creates a pool of workers to ping IP addresses concurrently.
- `refine(ip_list)`: Filters out inactive IP addresses.
- `main()`: Main function to orchestrate the scanning process.

## Contributing

Contributions to enhance the functionality or efficiency of this script are welcome. Please create a pull request with your changes.

## License

This project is open-source. You can use, modify, and distribute the script as you see fit.

## Disclaimer

Please use this script responsibly and ensure you have permission to scan any network or IP range.
