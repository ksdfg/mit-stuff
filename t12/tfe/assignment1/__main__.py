from argparse import ArgumentParser

from assignment1 import run_google_scholar

if __name__ == "__main__":
    parser = ArgumentParser(description="Fetch links from Google Scholars for a specific query")
    parser.add_argument("-q", "--query", type=str, help="Query string to search for articles", default="anime cats")
    args = parser.parse_args()

    print(*run_google_scholar(args.query), sep="\n")
