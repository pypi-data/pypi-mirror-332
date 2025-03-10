import argparse
from fetch_med import fetch, log
import sys


def get_user_input() -> tuple[str, bool, int | None, int | None, str | None, bool]:
    while True:
        query = input("Query: ").strip()
        if query:
            break
        print("Error: Query cannot be empty. Please enter a value.")

    debug = input("Debug [Default: n] [Input: y/n]: ").strip().lower()
    if debug not in {"", "y", "n"}:
        print('Invalid input. Only "y", "n", or empty input allowed.')
    debug = debug == "y"

    force = input(
        "Add article without author [Default: n] [Input: y/n]: ").strip().lower()
    if force not in {"", "y", "n"}:
        print('Invalid input. Only "y", "n", or empty input allowed.')
    force = force == "y"

    get = input(
        "Max number of articles in Output [Default: ALL] [Input: any integer]: ").strip()
    if get.isdigit():
        get = int(get)
    elif get.lower() == "all" or get == "":
        get = None
    else:
        print("Invalid input. Only an integer or empty input allowed.")

    count = input(
        "Max number of articles to fetch and parse [Default: ALL] [Input: any integer]: ").strip()
    if count.isdigit():
        count = int(count)
    elif count.lower() == "all" or count == "":
        count = None
    else:
        print("Invalid input. Only an integer or empty input allowed.")

    file_path = input("File Path [Default: Print in console]: ").strip()

    return query, force, count, get, file_path, debug


def main() -> None:
    if len(sys.argv) <= 1:
        query, force, count, get, file_path, debug = get_user_input()
        if debug:
            log(True)
        obj = fetch(query, force, count, get)
        obj.save(file_path)
    else:
        parser = argparse.ArgumentParser(
            description="Fetch MetaData of the PUBMED Papers")

        parser.add_argument("-d", "--debug", dest="debug",
                            action="store_true", help="debug the program")
        parser.add_argument("-q", "--query", dest="query",
                            type=str, help="query to get papers")
        parser.add_argument("-f", "--file", dest="file", type=str,
                            help="path of the output file.")
        parser.add_argument("--force", dest="force",
                            action='store_true', help="force article to be added even if author is not present")
        parser.add_argument("-g", "--get", dest="get",
                            type=int, help="max number of articles to be present in output. By default all")
        parser.add_argument("-c", "--count", dest="count",
                            type=int, help="max number of articles to fetch and parse. By default all")
        parser.add_argument("-e", "--ext", dest="extension",
                            action='store_true', help='supports: .json, .csv and .xlsx')

        args = parser.parse_args()

        if args.extension:
            print('Extension Supported: .json, .csv and .xlsx')
            if args.query:
                print('remove -e or --ext to run the program')
        else:
            if args.debug:
                log(True)
            if args.query:
                obj = fetch(args.query, args.force, args.count, args.get)
                obj.save(args.file)
            else:
                print("EMPTY QUERY")
