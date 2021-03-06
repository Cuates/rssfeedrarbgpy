##
#        File: rssfeedrarbg.py
#     Created: 03/16/2019
#     Updated: 04/13/2019
#  Programmer: Cuates
#  Updated By: Cuates
#     Purpose: Retrieve RSS feed from RarBg site
#     Version: 0.0.1 Python3
##

# Import modules
import rssfeedrarbgclass # rss feed rarbg class

# Set object
rfrbclass = rssfeedrarbgclass.RssFeedRarBgClass()

# Program entry point
def main():
    # Try to execute the command(s)
    try:
        # Check if modules are installed
        import tkinter, feedparser, webbrowser, pathlib, re, requests, bs4, logging, json, datetime, sqlite3, pytz, tzlocal, sqlalchemy, sys, pythonjsonlogger

        # Create tables
        rfrbclass._create_db_tables()

        # Set variable to local date time based on UTC current date time and format to date time for database storage
        currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

        # Insert action status record
        rfrbclass._actionStatusReg('SQLiteRarBG', 'actionstatus', 0, 'Register', currentDateTime, currentDateTime)

        # Set variable to local date time based on UTC current date time and format to date time for database storage
        currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

        # Insert action status record
        rfrbclass._actionStatusReg('SQLiteRarBG', 'actionstatus', 1, 'Ignore', currentDateTime, currentDateTime)

        # Set variable to local date time based on UTC current date time and format to date time for database storage
        currentDateTime = str(datetime.datetime.strptime(str(pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone(str(tzlocal.get_localzone())))), '%Y-%m-%d %H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S'))

        # Insert action status record
        rfrbclass._actionStatusReg('SQLiteRarBG', 'actionstatus', 2, 'Delete', currentDateTime, currentDateTime)

        # Call set tkinter
        rfrbclass._setTkinter('RarBg RSS Feed', '1675', '855', '#000000')

        # Execute tkinter main loop
        rfrbclass.initMainLoop()
    except Exception as e:
        # Log string
        rfrbclass._setLogger('Issue executing main PY file ' + str(e))

# Run program
if __name__ == '__main__':
    main()
