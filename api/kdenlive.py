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

def openXmlProjectFile(filename):
    # Return an XML Document, using whichever python library we think suitable
    # Usually we will read the template, and then save back to a different file
    # which will become our project file.
    # Return a new KdenliveProject
    pass

class KdenliveProject():
    projectXml = someXml
    currentID = 0
    
    def __init__(self, projectXmlString):
        # When we add a producer, we need to give it an ID.  Increment this to figure out what we're up to.
        # For now though, read what the highest existing one is
        currentID = 1# Search for the <kdenlive_producer> with the highest ID. 
        pass
    
    def saveXmlProjectFile(self, filename):
        # Save the XML document, usually to a new file.
        pass

    def findTrackByName(self, name):
        # Given the project Xml, find the track by the given name
        
        # Search for top level element <mlt> (this is your opening tag, equivalent of <html>)
        #   MLT is the command line rendering engine that powers the project.  So all our our main data goes in here
        # Search for child <kdenlivedoc> (should be last child, should only be one of them)
        #   This is the data that isn't important to rendering, but is to the project - tracknames, project imports etc.
        # Search for child <tracksinfo> (should only be one of them)
        # Get list of children <trackinfo> (should be about 6 of them in our template)
        #   These correspond to the tracks in our kdenlive project.  The first element is the bottom track,
        #   The second element is the second from the bottom, the final element is the top track etc.
        # Get the one who has the attribute trackname="$name"
        # Get it's index.  (First child=0, second child=1, third=2 etc)
        # Now get it's MLT playlistID: 
        #   playlistID = "playlist" + index # "playlist0" ... "playlist5"
        # Go back to the MLT object, and select the child <playlist>, with id=$playlistID
        # Return this playlist.
        
    def addClipToProject(self, filepath):
        # add a clip to the given project.
        
        # Add it to the project file list.
        
        # Search for top level element <mlt> (this is your opening tag, equivalent of <html>)
        # Search for child <kdenlivedoc> (should be last child, should only be one of them)
        #    The <kdenlive_producer> child elements are our project clips.
        # Create a new XML element
        #    $path=
        #    $filename=
        #    $duration= (use ffmpeg api to get this)
        #    $filesize= (size in bites, same as using "ls -l")
        #    $filehash= tempted to leave this out for now, I'm not sure what it is or how you create it.
        #    $kdenliveProducerID = $currentID++
            kdenliveProducer = '<kdenlive_producer audio_max="1" id="$currentID" default_video="0" fps="24.780702" name="$filename" videocodec="H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10" resource="$path" default_audio="1" audiocodec="ATSC A/52A (AC-3)" duration="228" file_hash="ddd081e1b4346172793090539c473b5f" aspect_ratio="1.333333" channels="2" frequency="48000" video_max="0" type="3" frame_size="1440x1080" file_size="$filesize"/>'
        # Place /after/ any exiting <kdenlive_producer> elements
        
        # Add it to the "Default" timeline.
        
        # defaultPlayList = findTrackByName("Default")
        # $mltProducerID = $kdenlive_producerID + "_0" # kdenlive does some weird inverse-track-number here, but I think just using 0 will work.
        # Create a new <producer> element
        mltProducer = '''<producer in="0" out="($duration - 1)" id="$mltProducerID">
          <property name="mlt_type">producer</property>
          <property name="aspect_ratio">1.333333</property>
          <property name="length">$duration</property>
          <property name="eof">pause</property>
          <property name="resource">$path</property>
          <property name="meta.media.nb_streams">2</property>
          <property name="meta.media.0.stream.type">video</property>
          <property name="meta.media.0.stream.frame_rate">24.780702</property>
          <property name="meta.media.0.stream.sample_aspect_ratio">1.333333</property>
          <property name="meta.media.0.codec.frame_rate">100.000000</property>
          <property name="meta.media.0.codec.pix_fmt">yuv420p</property>
          <property name="meta.media.0.codec.sample_aspect_ratio">1.333333</property>
          <property name="meta.media.0.codec.colorspace">709</property>
          <property name="meta.media.0.codec.name">h264</property>
          <property name="meta.media.0.codec.long_name">H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10</property>
          <property name="meta.media.0.codec.bit_rate">2566724</property>
          <property name="meta.media.1.stream.type">audio</property>
          <property name="meta.media.1.codec.sample_fmt">s16</property>
          <property name="meta.media.1.codec.sample_rate">48000</property>
          <property name="meta.media.1.codec.channels">2</property>
          <property name="meta.media.1.codec.name">ac3</property>
          <property name="meta.media.1.codec.long_name">ATSC A/52A (AC-3)</property>
          <property name="meta.media.1.codec.bit_rate">256000</property>
          <property name="seekable">1</property>
          <property name="meta.media.sample_aspect_num">4</property>
          <property name="meta.media.sample_aspect_den">3</property>
          <property name="meta.attr.title.markup"/>
          <property name="meta.attr.author.markup"/>
          <property name="meta.attr.copyright.markup"/>
          <property name="meta.attr.comment.markup"/>
          <property name="meta.attr.album.markup"/>
          <property name="audio_index">1</property>
          <property name="video_index">0</property>
          <property name="mlt_service">avformat</property>
          <property name="meta.medbyia.frame_rate_num">25</property>
          <property name="meta.media.frame_rate_den">1</property>
          <property name="source_fps">24.780702</property>
          <property name="meta.media.colorspace">709</property>
          <property name="meta.media.width">1440</property>
          <property name="meta.media.height">1080</property>
          <property name="meta.media.top_field_first">0</property>
          <property name="meta.media.progressive">1</property>
         </producer>'''
        # Insert this mltProducer /before/ our currentTrack (so it is a sibling)
        
        # Insert our currentTrack
        # Create a new entry element
        entry = '<entry in="0" out="($duration - 1)" producer="$mltProducerID"/>'
        # Insert as last child of current track
        # currentTrack.append(entry)
        
    def getSegmentsToExport(self):
        # Take a look at our break track
        breakPlaylist = findTrackByName("Break")
        currentFrame = 0 # Or should this be 1 to start?  Will have to test
        
        # currentSegment = 1;
        # for (child in breakPlaylist)
        #    If it's <entry>, then there's something in this track, so we do not export this segment.
        #        duration = <entry>.out - <entry>.in
        #        currentFrame = currentFrame + duration
        #    If it's <blank>, then there's nothing in this track, so we do export this segment
        #        startPoint = currentFrame
        #        duration = <blank>.length
        #        currentFrame = currentFrame + duration
        #        endPoint = currentFrame
        #        print (" Export Part" + $currentSegment + ".vob from " + startPoint + " to " + endPoint