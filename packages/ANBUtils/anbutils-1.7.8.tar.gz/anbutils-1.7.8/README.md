# ANBUtils

ANBUtils is a Python package that provides various utility functions for common tasks in data analysis and database
operations. It includes functions for working with MongoDB, sending messages via DingTalk, and handling date and time
operations.

## Stable Version

- Version: 1.7.x
- Release Date: Mar 28, 2024

## Installation

You can install ANBUtils using pip:

```
pip install ANBUtils == 1.7.0
```

## Functions

### MongoDB Operations

- `DBWorker`: A class that provides convenient methods for working with MongoDB databases and collections. It allows you
  to perform operations such as querying data, inserting data, updating data, and more.

### Environment Checker

- `environment_checker`: A function that checks the required environment variables for the ANBUtils package. It verifies
  the presence of the following environment variables: `MONGODB_URL`, `MONGODB_PUB_URI`, and `DINGTALK_WEBHOOK`.
    - `MONGODB_URL`: URL of the MongoDB database.
    - `MONGODB_PUB_URI`: URL of the publicly accessible MongoDB database.
    - `DINGTALK_WEBHOOK`: Webhook address of the DingTalk bot.
    - `QYWECHAT_WEBHOOK`: Webhook address of the QiYe Wechat Work bot.

### DingTalk Message Sender

- `dingtalk_text_message`: A function that sends text messages to DingTalk. It requires the `DINGTALK_WEBHOOK`
  environment variable to be set. You can use this function to send notifications or alerts to a DingTalk group or chat.

### Date and Time Operations

- `future`: A function that returns the date in the future by adding a specified number of days to the current date.
- `utc2tz`: A function that converts a UTC datetime to a specified time zone.
- `today`: A function that returns the current date.
- `tomorrow`: A function that returns tomorrow's date.
- `yesterday`: A function that returns yesterday's date.
- `now`: A function that returns the current date and time.
- `future_base`: A function that returns a date in the future based on a given date.
- `ts2str`: A function that converts a timestamp to a formatted date string.
- `date_format`: A function that formats a date string according to a specified format.

## Usage

### MongoDB Operations

To use the MongoDB operations provided by ANBUtils, you need to instantiate a `DBWorker` object with the name of the
database you want to work with. Here's an example:

```python
from ANBUtils import DBWorker

# Instantiate a DBWorker object for the "mydb_key" database
db = DBWorker("mydb_key")

# Query data from a collection
data = db.to_df("mycollection")

# Query data from a collection list
data = db.to_df_many(["mycollection1", "mycollection2", "mycollection3"])

# Insert data into a collection
df = ...
db.insert_df(df, "mycollection")

# Update data in a collection
df = ...
db.update_df(df, "mycollection", key="id")
```

### Message Sender

To send text messages to DingTalk or QiYe Wechat using the `dingtalk_text_message` or `qywechat_text_message` function,
you need to set the `DINGTALK_WEBHOOK` environment variable to the webhook URL provided by DingTalk. Here's an example:

```python
from ANBUtils import dingtalk_text_message, qywechat_text_message

# Send a text message to DingTalk
dingtalk_text_message("Hello from ANBUtils!")
qywechat_text_message("Hello from ANBUtils!")

```

### Date and Time Operations

ANBUtils provides various functions for working with dates and times. Here are a few examples:

```python
from ANBUtils import future, utc2tz, today, tomorrow, yesterday, now, future_base, ts2str, date_format

# Get the date in the future
future_date = future(5)

# Convert UTC datetime to a specific time zone
utc_datetime = ...
tz_datetime = utc2tz(utc_datetime, tz="E8")

# Get the current date
current_date = today()

# Get tomorrow's date
next_date = tomorrow()

# Get yesterday's date
prev_date = yesterday()

# Get the current date and time
current_datetime = now()

# Get a date in the future based on a given date
base_date = "2023-01-01"
future_date = future_base(base_date, 10)

# Convert a timestamp to a formatted date string
timestamp = ...
date_string = ts2str(timestamp)

# Format a date string according to a specified format
date = "2023-06-06"
formatted_date = date_format(date, date_format="YYYY_MM_DD")
```

Please make sure to refer to the ANBUtils documentation for detailed information on each function and its parameters.

## Contributions and Support

ANBUtils is an open-source project, and contributions are welcome. If you encounter any issues or have suggestions for
improvements, please feel free to open an issue on the [GitHub repository](https://github.com/example-user/ANBUtils).

For support or general questions, you can reach out to the project maintainers or the community through the GitHub
repository.

## License

ANBUtils is released under the [MIT License](https://opensource.org/licenses/MIT). Please refer to the LICENSE file for
more details.