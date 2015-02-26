#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
#
#  qooxdoo - the new era of web development
#
#  http://qooxdoo.org
#
#  Copyright:
#    2013 1&1 Internet AG, Germany, http://www.1und1.de
#
#  License:
#    LGPL: http://www.gnu.org/licenses/lgpl.html
#    EPL: http://www.eclipse.org/org/documents/epl-v10.php
#    See the LICENSE file in the project's top-level directory for details.
#
#  Authors:
#    * Richard Sternagel (rsternagel)
#
################################################################################

##
# Creates (sanitized) contrib index for contrib webinterface.
##

import codecs
import json
import os
import sys
import re

# --- constants ---

# input / output
CONTRIB_PATH = "../../../catalog.git/contributions"
IDX_FILENAME = "../website/json/contribindex.json"

MANIFEST_FILE = "Manifest.json"
CONTRIB_URL_FORMAT = ("https://github.com/qooxdoo-contrib/catalog/"
                           "blob/master/contributions/{name}/")
MANIFEST_URL_FORMAT = CONTRIB_URL_FORMAT + "{version}/" + MANIFEST_FILE

SEM_VER_RE = (r"^(trunk|master|\d+\.\d+(\.\d+)?(?:-[0-9]+-?)?"
              "(?:[-a-zA-Z+][-a-zA-Z0-9\.:]*)?)$")


# --- vars ---

# @type {"name": ["1.0", "master"], "name2" ...}
contribs = {}
# @type [{"name": "", "description": "", "summary": "", ...}, { ... }]
index = []


# --- helper/sanitizer ---

def stripHtml(text):
    return re.sub('<[^<]+?>', '', text)

def truncate(text, chars_amount=120):
    shorter = text[:chars_amount]
    if not shorter or shorter == text:
        return text
    elif shorter[-1] == '.':
        return shorter
    else:
        ellipsis = ""
        if (len(text) >= len(shorter)+1 and
            re.search('\w', text[chars_amount])):
            ellipsis = "..."
        else:
            ellipsis = " ..."
        return shorter + ellipsis

def trunkToMaster(versions):
    return ["master" if vers == "trunk" else vers for vers in versions]

def getFirstCategory(categories):
    if categories:
        return categories[0]

    return ""

def sanitizeLicense(license):
    if not license or license == "SomeLicense":
        return ""

    return license

def sanitizeHomepage(homepage):
    defaults = ("http://some.homepage.url/",
                "http://qooxdoo.org/",
                "http://www.qooxdoo.org/",
                "http://contrib.qooxdoo.org")

    if not homepage or homepage in defaults:
        return ""

    return homepage

def sanitizeAuthors(authors):
    if authors[0] and authors[0]["name"] == "First Author (uid)":
        authors = []

    return authors

def sanitizeVersions(versions):
    for i, version in enumerate(versions):
        if not re.search(SEM_VER_RE, version):
            versions[i] = "master"

    return versions

# --- main ---

# collect all contrib versions
for dirname, dirnames, filenames in os.walk(CONTRIB_PATH):
    if MANIFEST_FILE in filenames:
        name = os.path.basename(os.path.dirname(dirname))
        version = os.path.basename(dirname)

        if name in contribs:
            contribs[name].append(version)
        else:
            contribs[name] = []
            contribs[name].append(version)

# fail early
if not contribs:
    print "No contribs collected. Check CONTRIB_PATH: " + CONTRIB_PATH
    sys.exit(1)

# collect and tailor contrib data
for name, versions in contribs.iteritems():
    join = os.path.join
    versions.sort()
    latest_vers = versions[-1]
    abspath = join(join(join(CONTRIB_PATH, name), latest_vers), MANIFEST_FILE)
    manifest = json.load(codecs.open(abspath, encoding="utf8"))
    entry = {}

    if "info" in manifest:
        data = manifest["info"]
        data["qooxdoo-versions"] = trunkToMaster(data["qooxdoo-versions"])
        try:
            entry["name"] = data["name"]
            entry["description"] = stripHtml(data["description"])
            entry["shortdesc"] = truncate(stripHtml(data["description"]))
            entry["summary"] = data["summary"]
            entry["category"] = getFirstCategory(data["category"])
            entry["authors"] = sanitizeAuthors(data["authors"])
            entry["homepage"] = sanitizeHomepage(data["homepage"])
            entry["versions"] = sanitizeVersions(versions)[::-1]
            entry["qxversions"] = data["qooxdoo-versions"][::-1]
            entry["license"] = sanitizeLicense(data["license"])
            entry["demos"] = data["demos"] if "demos" in data else []
            entry["keywords"] = data["keywords"] if "keywords" in data else []

            entry["catalogurl"] = {}
            entry["catalogurl"]["base"] = CONTRIB_URL_FORMAT.format(name=name)
            entry["catalogurl"]["latest"] = MANIFEST_URL_FORMAT.format(name=name, version=latest_vers)
        except KeyError:
            pass

    # add to index
    index.append(entry)

# sort index after contrib name
index = sorted(index, key=lambda k: (k["name"].upper(), k["name"].islower()))

# write index to disc
raw_json = json.dumps(index)
idx_file = codecs.open(IDX_FILENAME, "w", "utf8")
idx_file.write(raw_json)
idx_file.close()

# print success message
amount = str(len(index))
print 'Done. Wrote index for '+amount+' contribs into "'+IDX_FILENAME+'".'
