def transcodeToMP4(inFile, outFile):
    # ffmpeg -i $inFile -s 1440x1080 -aspect 16:9 -threads 4 -r 50 -f mp4 -acodec copy -pix_fmt yuv420p -vcodec libx264 -minrate 0 -b 50000k -b_strategy 1 -subcmp 2 -cmp 2 -coder 1 -flags +loop -flags2 dct8x8 -qmax 51 -subq 7 -qmin 10 -qcomp 0.6 -qdiff 4 -trellis 1 $outFile &
    pass

def getNumOfFrames(inFile):
    # ffmpeg -i $inFile
    # Look for this line:
    # Duration: $HH:$MM:$SS.$FF, start: 0.000000, bitrate: 1161 kb/s
    #   Stream #0.0(und): Video: h264, yuv420p, 1440x1080 [PAR 1:1 DAR 16:9], 932 kb/s, $framerate fps, 25 tbr, 25 tbn, 50 tbc
    # And use this, combined with FPS, to figure it out.
    return 0