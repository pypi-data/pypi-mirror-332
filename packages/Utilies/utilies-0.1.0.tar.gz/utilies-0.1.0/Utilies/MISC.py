import glob
import logging
import os
import shutil
import smtplib
import sys
import threading
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import json
import random
import string
import re
import subprocess
import time
import datetime

import pandas as pd
import win32com.client

# Set current directory path
Path = os.curdir
sys.path.append(Path)

# Threading lock for synchronization
lock = threading.Lock()


class Utility:
    """
    A class that encapsulates a variety of utility methods for file processing, emailing,
    Excel manipulation, and data cleanup.
    """

    def str_to_float(self, df, cols):
        """
        Convert columns to float in a pandas DataFrame after cleaning the data.

        Args:
            df (pandas.DataFrame): DataFrame containing the data.
            cols (list): List of column names to be converted.

        Returns:
            pandas.DataFrame: Updated DataFrame with cleaned and converted columns.
        """
        for col in cols:
            try:
                df[col] = df[col].map(str).apply(lambda x: self.cleanAmount(x)).astype(float)
            except Exception as e:
                logging.error(f"Error converting column {col} to float: {str(e)}")
        return df

    def log_infos(self, message):
        """Logs the provided info message."""
        logging.info(message)

    def log_renames(self, fname1, fname2):
        """Logs the renaming or copying of files."""
        shutil.copy(fname1, fname2)

    def TimeOut(self, timeout):
        """Pauses execution for the specified timeout (in seconds)."""
        time.sleep(timeout)

    def get_config(self, configfile):
        """
        Reads and returns configuration data from the specified config file.

        Args:
            configfile (str): Path to the configuration file.

        Returns:
            configparser.ConfigParser: ConfigParser object with the parsed configuration.
        """
        import configparser
        config = configparser.ConfigParser()
        config.read(configfile)
        return config

    def GetFiscalYr(self, date):
        """
        Returns the fiscal year based on a given date.

        Args:
            date (datetime): The date to calculate the fiscal year.

        Returns:
            int: The fiscal year corresponding to the given date.
        """
        return date.year if date.month <= 10 else date.year + 1

    def GetFiscalMnth(self, month):
        """
        Returns the fiscal month number corresponding to a given month.

        Args:
            month (int): The month number (1 to 12).

        Returns:
            int: Fiscal month number (1 to 12).
        """
        fiscal_month_mapping = {
            11: 1, 12: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8,
            7: 9, 8: 10, 9: 11, 10: 12
        }
        return fiscal_month_mapping.get(month, "nothing")

    def GetFiscalQuarter(self, endDate):
        """
        Returns the fiscal quarter and corresponding months for a given end date.

        Args:
            endDate (datetime): The end date to calculate the fiscal quarter.

        Returns:
            tuple: (Quarter string, List of months in the quarter).
        """
        month = endDate.month
        if month in [11, 12, 1]:
            return "Q1", [11, 12, 1]
        elif month in [2, 3, 4]:
            return "Q2", [2, 3, 4]
        elif month in [5, 6, 7]:
            return "Q3", [5, 6, 7]
        else:
            return "Q4", [8, 9, 10]

    def MailTrigger(self, mfrom, mto, subj, msg, path=""):
        """
        Sends an email with the specified subject, message, and attachment.

        Args:
            mfrom (str): Sender's email address.
            mto (str): Receiver's email address (can be a semicolon-separated list).
            subj (str): Subject of the email.
            msg (str): Body of the email.
            path (str or list): Path(s) to attachment(s) (optional).
        """
        msg = MIMEMultipart()
        msg['From'] = mfrom
        msg['To'] = mto
        msg['Subject'] = subj

        # Attach files if specified
        if path:
            attachments = [path] if isinstance(path, str) else path
            for file in attachments:
                part = MIMEBase('application', "octet-stream")
                with open(file, 'rb') as f:
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file)}"')
                msg.attach(part)

        msg.attach(MIMEText(msg, 'html'))
        server = smtplib.SMTP('smtp3.hpe.com')
        server.sendmail(mfrom, mto.split('; '), msg.as_string())
        server.quit()

    def cleanAmount(self, amt):
        """
        Cleans and converts amounts to a float.

        Args:
            amt (str): Amount as a string.

        Returns:
            float: Cleaned amount as float.
        """
        if isinstance(amt, (int, float)):
            return amt
        if str(amt) == "nan" or not amt:
            return 0
        return float(str(amt).replace(',', '').replace('-$', '-').replace('$', ''))

    def GetDataFromDirFiles(self, flpath, fltype, filterlist):
        """
        Reads data from all files in a directory with the specified file extension.

        Args:
            flpath (str): Directory path to search for files.
            fltype (str): File extension to search for (e.g., 'csv', 'xlsx').
            filterlist (list): List of columns to filter in the data.

        Returns:
            pandas.DataFrame: Consolidated DataFrame with data from all files.
        """
        df = pd.DataFrame()
        for filename in glob.glob(f'{flpath}/*.{fltype}'):
            df1 = pd.read_csv(filename, encoding='ISO-8859-1') if fltype == 'csv' else pd.read_excel(filename)
            df1 = df1[filterlist]
            df = pd.concat([df, df1], ignore_index=True)
        return df

    def convert_Excel_to_csv(self, filename):
        """
        Converts Excel files (.xls, .xlsx, .xlsb) to CSV format.

        Args:
            filename (str): Path to the Excel file to convert.

        Returns:
            str: Path to the converted CSV file.
        """
        output_filename = filename.rsplit('.', 1)[0] + '.csv'
        if not os.path.exists(output_filename):
            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = False
            excel.DisplayAlerts = False
            doc = excel.Workbooks.Open(filename)
            doc.SaveAs(output_filename, FileFormat=6)  # CSV format
            doc.Close()
            excel.Quit()
        return output_filename

    def EmptyFolder(self, path, allow_root=False):
        """
        Deletes all files and subdirectories in a given folder, but keeps the folder itself.

        Args:
            path (str): Folder path to clear.
            allow_root (bool): If True, allows clearing the root folder even with short path lengths.
        """
        if len(path) > 10 or allow_root:
            if os.path.isdir(path):
                for root, dirs, files in os.walk(path, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))

    def csv_consolidation(self, files, column_list):
        """
        Consolidates data from multiple CSV files into a single DataFrame.

        Args:
            files (list): List of CSV files to be read.
            column_list (list): Columns to be retained in the final DataFrame.

        Returns:
            pandas.DataFrame: Consolidated DataFrame containing data from all files.
        """
        df = pd.DataFrame()
        for filename in files:
            df_temp = pd.read_csv(filename, encoding="ISO-8859-1")
            df_temp = self.Sanity_Clean_df(df_temp)
            df_temp = self.remove_unnamed_columns(df_temp)
            df = pd.concat([df, df_temp], ignore_index=True)
        return df

    def Sanity_Clean_df(self, df):
        """
        Cleans the DataFrame by stripping unwanted whitespace from strings.

        Args:
            df (pandas.DataFrame): DataFrame to clean.

        Returns:
            pandas.DataFrame: Cleaned DataFrame.
        """
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        df.columns = df.columns.map(lambda x: str(x).replace("\n", ' ').strip())
        return df

    def remove_unnamed_columns(self, df):
        """
        Removes columns from the DataFrame that have 'Unnamed' in their name.

        Args:
            df (pandas.DataFrame): DataFrame to clean.

        Returns:
            pandas.DataFrame: Cleaned DataFrame with 'Unnamed' columns removed.
        """
        return df.loc[:, ~df.columns.str.contains('^Unnamed')]

    def wait_untill_file_download(self, outputDir, sleep_time, skip_file_name="_ExpenseItemization"):
        """
        Waits until a file is fully downloaded in a specified directory.
`
        Args:
            outputDir (str): Directory to check for downloaded files.
            sleep_time (int): Time (in seconds) to wait before checking again.
            skip_file_name (str): Filename to skip if present in the directory.
        """
        while any(file.endswith(".crdownload") for file in os.listdir(outputDir)):
            time.sleep(sleep_time)

        while True:
            latest_pdf_file = max(glob.glob(os.path.join(outputDir, "*.pdf")), key=os.path.getmtime)
            if skip_file_name not in latest_pdf_file and os.path.getsize(latest_pdf_file) > 0:
                break
            time.sleep(sleep_time)

        file = [f for f in glob.glob(os.path.join(outputDir, "*.*")) if skip_file_name not in f]
        for filename in file:
            os.rename(filename, os.path.join(outputDir, "DownloadedFile.pdf"))


    def read_file(self,file_path, mode='r'):
        """Read content from a file."""
        try:
            with open(file_path, mode) as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None


    def write_to_file(self, file_path, data, mode='w'):
        """Write data to a file."""
        try:
            with open(file_path, mode) as file:
                file.write(data)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def create_directory(self,path):
        """Create a directory if it doesn't exist."""
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Directory '{path}' created.")
                return True
            else:
                print(f"Directory '{path}' already exists.")
                return False
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False


    def get_file_extension(self,file_path):
        """Get the file extension."""
        _, file_extension = os.path.splitext(file_path)
        return file_extension


    def is_valid_email(self,email):
        """Check if an email address is valid."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None


    def generate_random_string(self,length=8):
        """Generate a random string of a given length."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def pretty_print_json(self,data):
        """Pretty print JSON data."""
        print(json.dumps(data, indent=4))


    def convert_to_json(self,data):
        """Convert data to JSON."""
        try:
            return json.dumps(data)
        except TypeError as e:
            print(f"Error converting to JSON: {e}")
            return None


    def get_current_timestamp(self):
        """Get the current timestamp in ISO format."""
        return datetime.datetime.now().isoformat()


    def execute_shell_command(self,command):
        """Execute a shell command and capture the output."""
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            return result.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            return None


    def wait_until_file_exists(self, file_path, timeout=60, sleep_interval=1):
        """Wait until the file exists or timeout is reached."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            if os.path.exists(file_path):
                return True
            time.sleep(sleep_interval)
        print(f"Timeout reached. File '{file_path}' not found.")
        return False

    def get_file_size(self,file_path):
        """Get the size of a file."""
        try:
            return os.path.getsize(file_path)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None

    def send_post_request(self, url, data):
        """Send an HTTP POST request."""
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error sending POST request: {e}")
            return None

    def get_current_datetime(self):
        """Get the current date and time."""
        return datetime.datetime.now()

    def convert_to_datetime(self, date_str, date_format='%Y-%m-%d %H:%M:%S'):
        """Convert a string to a datetime object."""
        try:
            return datetime.datetime.strptime(date_str, date_format)
        except ValueError as e:
            print(f"Error converting string to datetime: {e}")
            return None

    def is_file_empty(self, file_path):
        """Check if a file is empty."""
        try:
            return os.path.getsize(file_path) == 0
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None

    def append_to_file(self, file_path, data):
        """Append data to an existing file."""
        try:
            with open(file_path, 'a') as file:
                file.write(data)
            return True
        except Exception as e:
            print(f"Error appending to file: {e}")
            return False

    def read_lines_from_file(self, file_path):
        """Read lines from a file into a list."""
        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error reading lines from file: {e}")
            return None

    def get_last_modified_time(self, file_path):
        """Get the last modified time of a file."""
        try:
            return os.path.getmtime(file_path)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None

    def is_directory_empty(self, directory_path):
        """Check if a directory is empty."""
        try:
            return len(os.listdir(directory_path)) == 0
        except FileNotFoundError:
            print(f"Directory '{directory_path}' not found.")
            return None

    def copy_file(self, source, destination):
        """Copy a file from source to destination."""
        try:
            if not os.path.exists(source):
                print(f"Source file '{source}' does not exist.")
                return False
            with open(source, 'rb') as src, open(destination, 'wb') as dest:
                dest.write(src.read())
            print(f"File copied from '{source}' to '{destination}'")
            return True
        except Exception as e:
            print(f"Error copying file: {e}")
            return False

    def move_file(self, source, destination):
        """Move a file from source to destination."""
        try:
            if not os.path.exists(source):
                print(f"Source file '{source}' does not exist.")
                return False
            os.rename(source, destination)
            print(f"File moved from '{source}' to '{destination}'")
            return True
        except Exception as e:
            print(f"Error moving file: {e}")
            return False

    def remove_file(self, file_path):
        """Remove a file."""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' removed.")
                return True
            else:
                print(f"File '{file_path}' not found.")
                return False
        except Exception as e:
            print(f"Error removing file: {e}")
            return False

