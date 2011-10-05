import pexpect
import os

def transcodeToMP4(inFile, outFile):
    try:
        open(inFile)
        
        # Open file exists
        
        # If the outFile exists, then delete it
        try:
            open(outFile)
            os.remove(outFile)
            print "Deleted old File"
        except IOError as e:
            pass # Doesn't exist... all good
        
        # ffmpeg -i $inFile -s 1440x1080 -aspect 16:9 -threads 4 -r 50 -f mp4 -acodec copy -pix_fmt yuv420p -vcodec libx264 -minrate 0 -b 50000k -b_strategy 1 -subcmp 2 -cmp 2 -coder 1 -flags +loop -flags2 dct8x8 -qmax 51 -subq 7 -qmin 10 -qcomp 0.6 -qdiff 4 -trellis 1 $outFile &
        cmd = "ffmpeg -i " + inFile + " -s 1440x1080 -aspect 16:9 -threads 4 -r 50 -f mp4 -acodec copy -pix_fmt yuv420p -vcodec libx264 -minrate 50000 -b 50000k -b_strategy 1 -subcmp 2 -cmp 2 -coder 1 -flags +loop -flags2 dct8x8 -qmax 51 -subq 7 -qmin 10 -qcomp 0.6 -qdiff 4 -trellis 1 " + outFile
        
        thread = pexpect.spawn(cmd)
        print "started %s" % cmd
        cpl = thread.compile_pattern_list([
                pexpect.EOF,
                "frame= *(\d+)"
            ])
        
        (fps, hours, mins, secs, frames, total) = getDuration(inFile)
        
        while True:
            i = thread.expect_list(cpl, timeout=None)
            if i == 0: # EOF
                print "the sub process exited"
                break
            elif i == 1:
                frame_number = int(thread.match.group(1))
                percent = int (float(frame_number) / float(total) * 100)
                print str(frame_number), " / ", str(total), " ", percent, "%"
                thread.close

        
    except IOError as e:
        # Open file does not exist
        print 'Input File does not exist: ' + inFile
        
    

def getDuration(inFile):
    # ffmpeg -i $inFile
    # Look for this line:
    # Duration: $HH:$MM:$SS.$FF, start: 0.000000, bitrate: 1161 kb/s
    #   Stream #0.0(und): Video: h264, yuv420p, 1440x1080 [PAR 1:1 DAR 16:9], 932 kb/s, $framerate fps, 25 tbr, 25 tbn, 50 tbc
    # And use this, combined with FPS, to figure it out.
    
    hours = 0
    mins = 0
    secs = 0
    frames = 0
    fps = 25
    total = 0
    try:
        open(inFile)
        
        # Open file exists
        cmd = "ffmpeg -i " + inFile
        
        thread = pexpect.spawn(cmd)
        print "started %s" % cmd
        cpl = thread.compile_pattern_list([
                pexpect.EOF,
                "Duration.+(\d+):(\d\d):(\d\d).(\d\d)",
                " (\d+) fps.+\d+ tbr" # " 50 fps, 50 tbr, 90k tbn, 50 tbc"
            ])
        while True:
            i = thread.expect_list(cpl, timeout=None)
            if i == 0: # EOF
                break # the subprocess finished
            elif i == 1:
                hours = thread.match.group(1)
                mins = thread.match.group(2)
                secs = thread.match.group(3)
                frames = thread.match.group(4)
            elif i == 2:
                fps = int(thread.match.group(1))
                fps = 25 # For some reason this is more accurate than the apparent 50
                
                total = int(hours)
                total = total * 60 + int(mins)
                total = total * 60 + int(secs)
                total = total * fps + int(frames)
                
                print "FPS: ", fps
                print "Duration {}:{}:{}.{}".format(hours, mins, secs, frames)
                print "Duration ", total, " frames"
                
    except IOError as e:
        # Open file does not exist
        print 'Input File does not exist: ' + inFile
    return (fps, hours, mins, secs, frames, total)