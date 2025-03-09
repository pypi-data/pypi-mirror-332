# API Arsenal

![Python Version](https://img.shields.io/badge/python-3.x-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## Description

This library was developed to simplify handling HTTP requests, logging responses, and deriving statistics from them. It provides tools for testing and monitoring the performance of endpoints and generating detailed reports on successful and non-successful responses.

## Core Features

#### HTTP Request Handling:

- Log HTTP responses into an array for further analysis.
- Check if a response is successful (status code 2xx).

#### Response Statistics:

- Calculate minimum, maximum, and average response times.
- Display statistics about all logged responses.

#### Logging:

- Securely log usernames and passwords to a file using encryption.
- Log response statistics to a file.

#### Response Printing:

- Print detailed information about a response, including the response body.
- Print brief information about a response (status code, elapsed time, etc.).
- Print all logged responses with details.
- Print only successful responses with details.
- Print only non-successful responses with details.

#### Utility Functions:

- Generate random usernames, passwords, letters, numbers, and symbols for testing.

#### History Logging:

- Display a history of logged credentials.
- Display a history of logged statistics.”

## Installation

To install the library, you can use `pip`:

`pip install api-arsenal`

## Usage

### Simple Example

`from api_arsenal import api_arsenal import requests  # Create a utility object utility = api_arsenal()  # Send an HTTP request response = requests.get('https://api.example.com/data') utility.push_response(response, 'Example Endpoint')  # Print statistics utility.print_stats()`

### More Examples

`# Print all responses with details utility.print_all_detailed()  # Print only successful responses utility.print_successful_detailed_only()  # Log credentials to a file utility.log_user_credentials_in_file(comments='Test User')`

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or inquiries, you can contact me via email.
iabdullahban@gmail.com
