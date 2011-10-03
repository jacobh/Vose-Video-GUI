# imports up in this
import os, sys

# imports from project dir
import db
import defaults

# Create New Project
def Create_project(foldername, unit_coordinator, unit_name):
	#changes into project directory
	os.chdir(foldername)
	#creates default folder structure
	for folder in defaults.Folder_defaults:
		os.makedirs(folder)

	db.Init_project(foldername, unit_coordinator, unit_name)
