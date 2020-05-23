#!/bin/bash

ff=""
for f in *.gpx
do
    ff="$ff -f $f"
done
echo $ff
#gpsbabel -i gpx $ff -o gpx -F "All.gpx"
