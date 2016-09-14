#!/usr/bin/env python

"""
Write program to HTML from the Google Spreadsheet.

Carlos Scheidegger and Sam Gratzl, 2016

We recommend you use this under a virtual environment. Create
a virtualenv and then install the required libraries with

$ pip install -r requirements.txt

If you need to run this locally, please contact Sam or Carlos for
the private key to access the spreadsheet from the script.

"""

from data import *

import min_html as h
import sys

gc = get_spreadsheet("50WordSummaries") ## Ask Panels folks to change this name
panels = load_sheet_by_name(gc, "Ranking all").get_all_records()
panel_dict = dict((panel["Title"], panel) for panel in panels)

# def guess_venue(session):
#     ids = set([paper["ID"][:paper["ID"].find('-')] for paper in session["Value"]
#            if (not paper["ID"].startswith("TVCG"))])
#     if len(ids) > 1 and list(ids)[0].startswith("CG&A"):
#             return "cga" 
#     if len(ids) <> 1:
#         raise Exception("couldn't guess conference for session %s" % session["Key"])
#     return list(ids)[0]

# venue_name = { "cga": "CG&A",
#                "infovis": "InfoVis",
#                "scivis": "SciVis",
#                "vast": "VAST" }

# def paper_type(paper):
#     t = paper["Type"]
#     if t == "AJ":
#         return "J"
#     if t == "AC":
#         return "C"
#     if t == "TVCG":
#         return "T"
#     if paper["ID"].startswith("TVCG"):
#         return "T"
#     return "J"

# def render_session(session, out):
#     name = session["Key"]
#     venue = venue_name[guess_venue(session)]
#     out.write("**%s**  \n" % session_dict[name]["Day"].upper())
#     out.write("**%s**  \n" % session_dict[name]["Time"])
#     out.write("**Room: %s**  \n" % session_dict[name]["Room"])
#     out.write("*%s: %s*  \n" % (venue, name))
#     out.write("*Session Chair: %s*  \n" % (session_dict[name]["Chair"]))
#     out.write("\n")
#     for paper in session["Value"]:
#         out.write(("**%s (%s)**  \n" % (paper["Title"], paper_type(paper))).encode("utf-8"))
#         out.write(("Authors: %s\n" % paper["Author list"]).encode("utf-8"))
#         out.write("\n")
#     out.write("<hr/>\n\n")


# def session_key(session):
#     order = {
#         "8": 0,
#         "10": 1,
#         "2": 2,
#         "4": 3,
#         }
#     name = session["Key"]
#     metadata = session_dict[name]
#     day = metadata["Day"][-4:-2]
#     time = order[metadata["Time"][:metadata["Time"].find(':')]]
#     return (day, time)

date_dict = { 25: "TUESDAY, OCTOBER 25TH",
              26: "WEDNESDAY, OCTOBER 26TH",
              27: "THURSDAY, OCTOBER 27TH",
              28: "FRIDAY, OCTOBER 28TH" }

time_dict = { 8: "8:30AM-10:10AM",
              10: "10:30AM-12:10PM",
              2: "2:00PM-3:40PM",
              4: "4:15PM-5:55PM" }

tkey = { 8: 1, 10: 2, 2: 3, 4: 4 }

# out = sys.stdout
for panel in sorted(panel_dict.values(), key = lambda panel: (panel["Date"], tkey[panel["Time"]])):
    print "* %s" % panel["Title"]
print

for panel in sorted(panel_dict.values(), key = lambda panel: (panel["Date"], tkey[panel["Time"]])):
    print "#### %s" % panel["Title"]
    print
    print "%s  " % date_dict[panel["Date"]]
    print "%s  " % time_dict[panel["Time"]]
    print "Location: %s" % panel["Location"]
    print
    print "Organizer: %s  " % panel["Organizer"]
    print "Panelists: %s" % panel["Panelists"]
    print
    print panel["50 Word Summary"]
    print
    
