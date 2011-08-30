# Vose Video Editing GUI

## Context

At Vose we edit videos on linux, using kdenlive.  We’ve chosen this workflow because it allows much of the grunt-work, like transcoding, exporting, and creating DVD menus, to be automated.  (Yay for command line tools!)

I have a bunch of scripts (python, bash, haxe) that I’ve been using to process parts of the files.  I would like a GUI that would show me where a particular project is up to, let me run some of the automated commands, and let me launch the various programs that are involved (kdenlive, dvd-styler, inkscape etc).

## Basic Process

1. Copy MTS files from camera or SD card (can be largely automated)
2. Transcode files into MP4 (is automated, bash, sshhh about the quality drop)
3. Place the files on a track in kdenlive (can be automated)
4. Edit the files in kdenlive (needs to be done manually)
5. Export the various sections of the project (is automated, haxe)
6. Get a snapshot from the video to use on menus / labels (manual)
7. Create menus/labels in Inkscape (creation using templates can be automated, manual editing still required)
8. Convert SVG menus to PNG (automated, bash I think)
9. Create basic DVD structure (can be automated using template)
10. Import clips and menu items (can be automated using template)
11. Link specific clips to specific videos (still manual for now)
12. Export DVD to ISO (can be automated)
13. Create backups of final ISO, and of Raw footage (can be automated)

## Objectives

* Create a basic inteface that can:
  * Open up a certain week (there will probably have an XML file for each week)
  * At a glance see progress on a certain week.  (A simple tick or some kind of colour will do)
  * Click on a step that hasn’t been done, and it will launch the relevant process

## Mockup

Main Menu:
![](http://s.hzy.im/0687.png)