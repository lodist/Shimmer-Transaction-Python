# Shimmer-Transaction-Python
This repository contains an example script demonstrating how to execute a native token transaction on the Shimmer network using the IOTA SDK. The script is written in Python and includes detailed comments to guide users through each step of the process

This repository contains a Python script that demonstrates how to execute a native token transaction on the Shimmer network using the IOTA SDK. The script includes detailed comments and logging to help users understand each step of the process.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.7 or higher
- IOTA SDK
- A Shimmer Stronghold file and password

## Setup

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/<username>/ShimmerTransactionExample.git
    cd ShimmerTransactionExample
    ```

2. Install the required Python packages:
    ```bash
    pip install iota-sdk boto3
    ```

3. Update the script with your configuration:
    - Replace `/path/to/your/wallet.stronghold` with the path to your Stronghold file.
    - Replace `your_stronghold_password` with your Stronghold password.
    - Replace `0xYourTokenID` with the actual token ID you want to send.

## Usage

To run the script, use the following command:
```bash
python shimmer_transact.py 'recipient_address'
