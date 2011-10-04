# imports up in this
import os, sys

# imports from project dir
import db
import defaults

# Create New Project
def Create_project(folder_name, unit_coordinator, unit_name, unit_code):
	db.Init_project(folder_name, unit_coordinator, unit_name, unit_code)

def Create_video(project_folder, lecturer_name, video_name):
	db.Init_video(project_folder, lecturer_name, video_name)

	#changes into project directory, then creates folder for the week, then cd's into that
	os.chdir(project_folder)
	os.makedirs(video_name)
	os.chdir(video_name)
	#creates default folder structure
	for folder in defaults.Folder_defaults:
		os.makedirs(folder)
