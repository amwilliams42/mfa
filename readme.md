
# Authentication Modality Selection Project

This project implements a dynamic authentication modality selection algorithm. It evaluates various authentication modalities based on environment, device, and context data, then uses a SAT solver to determine the best combination of modalities that satisfy given attribute constraints.

## Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Authentication Factors](#authentication-factors)
6. [Attribute Constraints](#attribute-constraints)
7. [Example JSON File](#example-json-file)


## Overview

The primary goal of this project is to enhance security and user experience by dynamically selecting the best set of authentication modalities. The selection is based on real-time evaluations of environment, device, and context data. The project leverages Python's SAT solver to ensure that the selected modalities meet specified security, intrusiveness, privacy, and accuracy constraints.

## Project Structure
```bash
├── modalities
│   ├── __init__.py
│   ├── ip_address.py
│   ├── geolocation.py
│   ├── password.py
│   ├── facial_recognition.py
│   ├── battery_information.py
│   ├── screen_frame_resolution.py
│   ├── hardware_concurrency.py
│   ├── timezone.py
│   ├── network_flow_statistics.py
│   └── ...
├── environment_device_context.json
├── evaluate_and_select_modalities.py
├── sat.py
└── README.md
```
## Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/amwilliams42/mfa.git
    cd mfa
    ```

2. **Install Dependencies**:
    Ensure you have Python installed, then install the required packages:
    ```bash
    pip install python-sat
    ```

3. **Prepare the factor and attribute constraints**:
See the relevant sections [Authentication Factors](#authentication-factors)  and [Attribute Constraints](#attribute-constraints)

## Usage

1. **Prepare the JSON File**:
    Create or update the `environment_device_context.json` file with relevant environment, device, and context data.

2. **Run the Evaluation and Selection**:
    To run the selection algorithm, simply add all of the factors you would like considered, feed in a function to determine attribute constraints, and let the solver go. 
    ```python
    if __name__ == '__main__':
    # Example factor modules
    factor_modules = ['facial_recognition', 
                      'fingerprint', 
                      'password', 
                      ...]

    # Run the evaluation and selection process
    solutions = evaluate_and_select_factors("variables.json", factor_modules, determine_attribute_constraints)
    print("Solutions:", solutions)
    ```

## Authentication Factors

A factor is represented by a file in the `factors` subfolder. They are required to implement a function called `evaluate` that takes environemtn, device, and context data as input and returns a dictionary of attribute values. Adding a new factor is as simple as adding a new file to the `factors` folder and implementing this evaluate function. Then add the factor to the dict of considered factors. 

### Example: IP Address Evaluation

**File**: `modalities/ip_address.py`
```python
# new_modality.py

def evaluate(env, device, context):
    # Initialize default attribute values
    security = 5
    intrusiveness = 3
    privacy = 5
    accuracy = 7

    # Implement logic to evaluate attributes based on input data
    # Example: Adjust security based on environment
    if env.get('network_type') == 'wired':
        security += 2

    return {
        'Security': max(1, security),
        'Intrusiveness': intrusiveness,
        'Privacy': max(1, privacy),
        'Accuracy': accuracy
    }

```

## Attribute Constraints

In order to dynamically assign constraints to the system, you must provide a constraint function that takes in the environment, device, and context data, and returns a dict of each of the attributes you are considering and a corresponding tuple with (min, max) constraints. The values must be integers.
```python
def determine_attribute_constraints(env, device, context):
    # Function implementation...
```

## Example JSON File

Here is an example JSON file that provides the necessary environment, device, and context data. Note that the JSON file contains 3 main parent entries, environment, device, and context information. The intention is that this data is collected using a dynamic process prior to running the algorithm

```json
{
    "environment": {
        "location": "office",
        "network_type": "wired",
        "vpn_enabled": true,
        "public_wifi": false,
        "time_of_day": "afternoon",
        "recent_security_alerts": false
    },
    "device": {
        "ip_address": "192.168.1.105",
        "battery_status": "charging",
        "battery_percentage": 88,
        "screen_frame_resolution": "1920x1080",
        "screen_color_depth": 24,
        "hardware_concurrency": 8,
        "timezone": "UTC+01:00",
        "dns_resolver": "8.8.8.8",
        "clock_skew_ms": 30,
        "network_flow_statistics": {
            "inbound_bandwidth": "50Mbps",
            "outbound_bandwidth": "20Mbps",
            "packet_loss_rate": "0.2%",
            "latency_ms": 15
        }
    },
    "context": {
        "user_logged_in": true,
        "recent_failed_attempts": 1,
        "device_usage": {
            "last_login_time": "2024-05-09T14:30:00Z",
            "app_usage": ["browser", "email_client", "office_suite", "battery_saver", "multi-threaded_apps"]
        },
        "historical_timezones": ["UTC+01:00", "UTC+02:00"],
        "recent_travel": true,
        "consent": true
    }
}
```