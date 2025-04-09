import argparse
import csv
import random
import qrcode
from pptx import Presentation

def order_presenters(presenters):
    new_order = random.sample(presenters, len(presenters))
    return new_order


def make_qr(url):
    img = qrcode.make(url[0])
    img.save("PPT-Club-QR.png")

def calc_score(score_file):
    presenters = {}
    with open(score_file, 'r') as file:
        csvreader = csv.DictReader(file)
        responses = [row for row in csvreader]
        headers = responses[0].keys()
        for h in headers:
            if "Best Presentation Overall" in h:
                presenters[h] = 0
        pres_list = presenters.keys()
        for r in responses:
            for p in pres_list:
                place = text_to_int(r[p], len(pres_list))
                presenters[p] += len(pres_list) - place

    return presenters

def text_to_int(word, grp_size):
    intmap = {'First': 1, 'Second': 2, 'Third': 3, 'Fourth': 4,
        'Fifth': 5, 'Sixth': 6, 'Seventh': 7, 'Eigth': 8, 'Ninth': 9,
        'Tenth': 10}
    if word in intmap:
        return intmap[word]
    else: return grp_size

def score_print(output):
    sorted_out = dict(sorted(output.items(), key=lambda item: item[1], reverse=True))

    for k,v in sorted_out.items():
        print(k[26:], " : ", v)

def make_ppt(scores):
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--order", nargs="+", help="specify space seperated list of presenters ex Curly Larry Moe")
    parser.add_argument("-q", "--qr", nargs=1, help="specify URL for QR code generation in quotes")
    parser.add_argument("-s", "--score", nargs="?", const="export.csv", help="specify CSV file for scoring, (default: %(const)s)")
    parser.add_argument("-p", "--powerpoint", nargs="?", help="specify filename for ppt, default will be results.pptx" )
    args = parser.parse_args()

    if args.order:
        #print(args.order)
        new_order = order_presenters(args.order)
        print(new_order)
    if args.qr:
        #print(args.qr)
        make_qr(args.qr)
    if args.score:
        output_score = calc_score(args.score)
        score_print(output_score)
    if args.powerpoint:
        print(args.powerpoint)
