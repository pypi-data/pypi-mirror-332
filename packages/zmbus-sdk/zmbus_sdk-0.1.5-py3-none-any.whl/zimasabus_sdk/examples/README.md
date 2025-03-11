# Zimasabus SDK Examples

This directory contains example scripts demonstrating how to use the Zimasabus SDK.

## Available Examples

- [Follow-up Example](followup_example.py) - Demonstrates how to use the `FollowUpService` class to manage appointment follow-ups.

## Running the Examples

To run an example, make sure you have set up the required environment variables in a `.env` file at the root of the project:

```
ZBUS_ZIMASAMED_USERNAME=your_username
ZBUS_ZIMASAMED_PASSWORD=your_password
ZBUS_ZIMASAMED_CLIENT_ID=zimasa-consumer-api
ZBUS_ZIMASAMED_GRANT_TYPE=password
ZBUS_ZIMASAMED_VERIFY_URL=https://zimasa-verify.turnkeyafrica.com/
ZBUS_ZIMASAMED_BASEURL=http://192.0.1.23:5001/
```

Then, run the example script:

```bash
python -m zimasabus_sdk.examples.followup_example
```

## Creating New Examples

When creating new examples:

1. Create a new Python file in this directory
2. Import the necessary classes from the SDK
3. Implement a `main()` function that demonstrates the functionality
4. Add error handling to catch and display any exceptions
5. Add the example to the list in this README 