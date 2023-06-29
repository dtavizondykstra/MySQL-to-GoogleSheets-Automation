import pandas as pd
import mysql.connector
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connect to the MySQL database
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="<YOUR_HOST>",
            database="<YOUR_DATABASE>",
            user="<YOUR_USER>",
            password="<YOUR_PASSWORD>",
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))
        return None

# Fetch data from MySQL and return as a Pandas DataFrame
def fetch_data(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(data, columns=columns)

        # Optionally Convert date columns to string representation
        # date_columns = ["<NAME_OF_DATE_COLUMN>"]
        # df[date_columns] = df[date_columns].astype(str)

        return df

    except mysql.connector.Error as error:
        print("Failed to fetch data from MySQL: {}".format(error))
        return None

# Drop data into Google Sheets
def drop_data_to_google_sheets(data, spreadsheet_url):
    # Set up credentials
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "<YOUR_JSON_CREDENTIALS>", scope
    )

    # Authenticate and open the Google Sheets file
    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_url(spreadsheet_url)

    # Select the worksheet
    # Assuming you want to use the first worksheet (gid=0)
    worksheet = spreadsheet.get_worksheet(1)

    # Clear existing data in the worksheet
    worksheet.clear()

    # Append the new data to the worksheet
    header = list(data.columns)
    data_values = data.values.tolist()
    worksheet.append_row(header)
    worksheet.append_rows(data_values)

    print("Data has been successfully dropped into the Google Sheets file.")

# Main script
def main():
    # Connect to MySQL
    connection = connect_to_mysql()
    if connection is None:
        return

    # Define your query
    query = """<YOUR_SQL_QUERY>"""

    # Fetch data from MySQL
    data_frame = fetch_data(connection, query)
    if data_frame is None:
        connection.close()
        return

    # Print the data frame
    print(data_frame)

    # Drop data into Google Sheets
    spreadsheet_url = "<YOUR_SPREADSHEET_URL>"
    drop_data_to_google_sheets(data_frame, spreadsheet_url)

    # Close the MySQL connection
    connection.close()

if __name__ == "__main__":
    main()
