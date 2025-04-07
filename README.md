# Webhook Listener Application

This FastAPI application listens for webhooks from ERPNext and handles purchase order (PO) creation and assignment events.

## Overview

The application exposes two primary endpoints:

*   `/erpnext-po-webhook`:  Handles notifications when a new Purchase Order is created in ERPNext.
*   `/po-assignment`: Handles notifications related to Purchase Order assignments.

It also has a root endpoint:

*   `/`: Returns a simple "Hello, world!" message.

## Endpoints

### `/erpnext-po-webhook`

*   **Functionality:** Currently, it logs the received data to the console.  You should add your custom logic here, such as sending a message to a communication platform like Lark or Slack.

### `/po-assignment`

*   **Functionality:**

    *   Validates the presence of the `allocated_to` field.
    *   Skips processing if the assignment `status` is "Cancelled".
    *   Returns a success response with assignment details on successful processing.
    *   Returns an error response if any exceptions occur during processing.

## Getting Started

### Prerequisites

*   Python 3.7+
*   [pip](https://pypi.org/project/pip/) (Python package installer)

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install dependencies:
    ```bash
    pip install fastapi uvicorn
    ```

### Running the Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000