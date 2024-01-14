
#!/bin/bash
for file in /mnt/Brain/1uni/1RechnerArchi/1Vor/*.mp4; do
    echo "ffmpeg -i '$file' -q:a 0 -map a '${file%.mp4}.mp3'"
done
