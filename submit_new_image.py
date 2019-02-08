#!/usr/bin/python3

import logging
import argparse
import requests
import os
import sys

def get_image_layers (repo, tag):
	api_url_base = "https://containers.biocontainers.pro/v2"
	full_url = api_url_base+"/"+repo+"/manifests/"+tag
	logging.debug (full_url)
	r = requests.get(full_url)
	logging.debug (r.status_code)
	if r.status_code == 200:
		logging.debug (r.json()['fsLayers'])
	else:
		logging.warning("Could not find manifest for "+repo+":"+tag)

##########
###MAIN###
##########

logging.basicConfig(
		level=logging.DEBUG,
		format="%(levelname)s:%(message)s"
	)

parser = argparse.ArgumentParser(description="")
parser.add_argument('-r','--repo', help="Repo of the image to push", required="true")
parser.add_argument('-t','--tag', help="Tag of the image to push", required="true")
args = parser.parse_args()

##First we get all the image's layers info

layers = get_image_layers (args.repo, args.tag)
