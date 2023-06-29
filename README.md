# MySQL to Google Sheets Python Script
This script automates the process of fetching data from a MySQL database and dropping it into a Google Sheets document. The script makes use of pandas to convert the fetched data into a pandas DataFrame, allowing for further data manipulation if required.

### Requirements
The script requires the following Python libraries:
* `pandas`
* `mysql-connector-python`
* `gspread`
* `oauth2client`

Install these dependencies with pip:
`pip install pandas mysql-connector-python gspread oauth2client`

### Google Sheets API Setup
Before using the script, you need to set up the Google Sheets API:
* Go to the [Google Cloud Console](https://console.cloud.google.com/).
* Create a new project.
* Search for "Google Sheets API" in the library and enable it for your project.
* Create credentials for the Sheets API. When asked which API are you using, choose "Google Sheets API". When asked where will you be calling the API from, choose "Web server (e.g. node.js, Tomcat)". When asked what data will you be accessing, choose "Application data".
* Now create a Service Account. Download the JSON file and place it in the same folder as your script.
* Share your Google Sheet with the client email in the downloaded JSON file. More info on this [here](https://stackoverflow.com/questions/38949318/google-sheets-api-returns-the-caller-does-not-have-permission-when-using-serve).
* This JSON file contains the private key and other details required for authorization. You should refer to this file in the ServiceAccountCredentials.from_json_keyfile_name() function in the script.

### Usage
1. The script is started by running the `main()` function. 
2. Modify the MySQL host, database, user, and password in the `connect_to_mysql()` function, and the Google Sheets URL in the `drop_data_to_google_sheets()` function. 
3. Provide your query as the query string in the `main()` function.

### Warning
Ensure that sensitive data such as your MySQL and Google Sheets credentials are secured and not exposed in your script. Use environment variables or external configuration files to keep these details safe.

### Contributions
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

