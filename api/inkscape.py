#imports
from pystache import render
import sys, os
from subprocess import Popen

#saves this for stability
cwd = os.getcwd()

def createMenuAndLabel(unitCode, unitTitle, lecturerName, videoTitle, links, projectLocation):
	# Copy the Main menu and label from the template
	template_menu = open('assets/tpl/slides/Menu.svg').read()
	template_label = open('assets/tpl/slides/Label.svg').read()
	context = {'unitCode': unitCode, 'unitTitle': unitTitle, 'lecturerName': lecturerName, 'videoTitle': videoTitle}

	# break open the links
	length = len(links)
	if length >= 4:
		context['link_one'] = links[0]
		context['link_two'] = links[1]
		context['link_three'] = links[2]
		context['link_four'] = links[3]
	elif length == 3:
		context['link_two'] = links[0]
		context['link_three'] = links[1]
		context['link_four'] = links[2]
	elif length == 2:
		context['link_two'] = links[0]
		context['link_three'] = links[1]
	elif length == 1:
		context['link_two'] = links[0]

	# get some renders up in this
	rendered_menu = render(template_menu, context)
	rendered_label = render(template_label, context)

	# write this back to disk
	os.chdir(projectLocation+'/'+videoTitle+'/slides')
	file = open('menu.svg', 'w')
	file.write(rendered_menu)
	file.close()
	file = open('label.svg', 'w')
	file.write(rendered_label)
	file.close()

	os.chdir(cwd)


def createSlide(slideTitle, slideTime, slideText, videoName, projectLocation):
    # Create slide from the template
	template = open('assets/tpl/slides/Slide.svg').read()
	context = {'title': slideTitle, 'time': slideTime, 'text': slideText}
	rendered_slide = render(template, context)
	#write it to disk
	os.chdir(projectLocation+'/'+videoName+'/slides/svg')
	file = open(slideTitle+'.svg', 'w')
	file.write(rendered_slide)
	file.close()
	os.chdir(cwd)

def openMenu(projectLocation, videoName):
    # Open the menu for editing in Inkscape
    #inkscape menu.svg
	Popen('inkscape '+projectLocation+'/'+videoName+'/slides/menu.svg')

def openLabel():
    # Open the menu for editing in Inkscape
    #inkscape label.svg
	Popen('inkscape '+projectLocation+'/'+videoName+'/slides/label.svg')

def openSlide(projectLocation, videoName, slideName):
    # Open the menu for editing in Inkscape
    #inkscape $slideName.svg
	Popen('inkscape '+projectLocation+'/'+videoName+'/slides/svg/'+slideName+'.svg')

def convertSlidesToPng(projectLocation, videoName):
    # Read a folder, convert all SVG to PNG
    # inkscape -f infile.svg -C -e outfile.png
	os.chdir(projectLocation+'/'+videoName+'/slides/svg')
	svgs = os.listdir('.')
	for svg in svgs:
		Popen('inkscape -f '+svg+' -C -e ../png/'+svg[:-3]+'png')
	os.chdir(cwd)
	
    
def convertMenuToPng(projectLocation, videoName):
    # inkscape -f menu.svg -C -e menu.png
	os.chdir(projectLocation+'/'+videoName+'/slides')
	Popen('inkscape -f menu.svg -C -e menu.png')
	os.chdir(cwd)

def convertLabelToPdf(projectLocation, videoName):
    # Convert a single SVG file to PDF
    # inkscape -f infile.svg -C -e outfile.png
	os.chdir(projectLocation+'/'+videoName+'/slides')
	Popen('inkscape -f label.svg -C --export-pdf=label.pdf')
	os.chdir(cwd)
