
import urllib2
import csv
import argparse
import logging
import datetime

def downloadData(url):


    return urllib2.urlopen(url)

def processData(infile):


    processed_data = {}

    csv_reader = csv.reader(infile)

    next(csv_reader)

    for i, person in enumerate(csv_reader):
        try:
            p_id = int(person[0])

            P_name = person[1]

            p_birth_date = datetime.datetime.strptime(person[2], "%d/%m/%y")

            processed_data[p_id] = (p_name, p_birth_date)

        except:
            error_msg ="Error processing line# # for ID #{}.".format(i, p_id)

            logging.basicConfig(filename="error.log",  level= logging.ERROR)

            logger = logging.getLogger("assignment 2")

            logger.error(error_msg)


        return processed_data

def displayPerson(pid, dict_data):

    if pid in dict_data:

        name = dict_data[pid][0]

        bdate = datetime.datetime.strftime(dict_data[pid][1], "%y-%m-%y")

        print("Person #{} is {} with a birthday of {}."). format(pid, name, bdate)


    else:
        print("No one with this ID")

def main():

    downloaded_data = None

    parser = argparse.ArgumentParser()

    parser.add_argument("--url", required=True, help="Providing CSV file's Url")

    args = parser.parse_args()

    try:
        downloaded_data = downloadData(args.url)

    except:
        print("Error occured ")

        process_dict = processData(downloaded_data)

        while True:

            pid = int(input("Enter ID to look: "))

            if pid <= 0:
                break

            else:
                displayPerson(pid, process_dict)

if __name__ == "__main__":
