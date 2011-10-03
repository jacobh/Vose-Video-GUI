def renderExcerpt(sourceFile, outputFile, inPoint, outPoint):
    # sourceFile - project.kdenlive
    # outputFile - export.vob
    # inPoint - number of frames of start point
    # outPoint - number of frames of end point
      
    launch = "/usr/bin/kdenlive_render -kuiserver"
    section = "in=" + inPoint + " out=" + outPoint
    render = "/usr/bin/melt"
    profile = "hdv_1080_25p"
    rendermodule = "avformat"
    player = "-"
    args= " f=dvd vcodec=mpeg2video acodec=ac3 b=5000k maxrate=8000k minrate=0 bufsize=1835008 mux_packet_s=2048 mux_rate=10080000 ab=192k ar=48000 s=720x576 g=15 me_range=63 trellis=1 profile=dv_pal_wide"
    
    cmd = launch + section + render + profile + rendermodule + player
    cmd += "consumer:" + sourceFile + " " + outputFile + args
    
    print cmd

def exportFromProject():
    # This is complicated... will explain to you later
    pass

def createProjectFileFromTemplate():
    # Create from a template.
    # If you're feeling adventerous, 
    #  - try and insert the clips into the project
    #  - try and insert the clips onto the timeline, one after another, onto "DEFAULT"
    pass