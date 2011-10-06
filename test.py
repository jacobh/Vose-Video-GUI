#!/usr/bin/python
import api.ffmpeg
from ProjectConf import ProjectConf

print ProjectConf.currentProject['path']
ProjectConf.currentProject = ProjectConf.projects['Jacob']
print ProjectConf.currentProject['path']

#api.ffmpeg.transcodeToMP4("assets/sampledata/originals/file.MTS", "assets/sampledata/transcodes/file.MTS.MP4")
