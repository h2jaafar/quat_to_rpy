#!/bin/bash

APPDIR="QuatToRPY.AppDir"
LIBDIR="$APPDIR/usr/lib"
mkdir -p "$LIBDIR"

# Copy required libraries for the Python interpreter
for lib in $(ldd $(which python3) | awk '{if (match($3,"/")){ print $3 }}'); do
    cp "$lib" "$LIBDIR/"
done

# Copy additional required libraries if necessary
# cp /path/to/your/library "$LIBDIR/"

# Copy Python standard library
cp -r /usr/lib/python3.8 "$LIBDIR/"