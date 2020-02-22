#! /usr/bin/env python3
import argparse
import base64

def create_parse():
    """ set up parser options """
    parser = argparse.ArgumentParser(description="convert file to base64")
    parser.add_argument("action", help="e to encode, d to decode")
    parser.add_argument("source", help="file to be converted")
    parser.add_argument("destination", help="file to receive converted chars")
    return parser

def main():
    """ main event loop """
    parser = create_parse()
    args = parser.parse_args()
    source = open(args.source,"rb")
    destination = open(args.destination,"wb")
    if args.action == "e":
        base64.encode(source, destination)
    elif args.action == "d":
        base64.decode(source, destination)

if __name__ == "__main__":
    main()
