#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: SpotTheErrors1.py
    Author: Shawn Hutchinson
    Description:  Sample script containing only five types of obvious errors
    Date created: 09/25/2023
    Python Version: 3.9.16
"""

# Import arcpy module:
import arcpy

# Set geoprocessing environments:
env.workspace = "D:\GEOG728\Exercises\KansasData.gdb"
env.overwriteOutput = True

# Local variables:
Infc = "ks_major_rivers"
Clipfc = "flint_hills"
Outfc = "clipped_rivers"

# Process: Clip (analysis):
arcpy.Clip.analysis(Infc, Clipfc, Outfc)  

# Print the name for and spatial reference of the clipped output
spatialRef = arcpy.Describe(Outfc)
print("The spatial reference for {0} is {1}."(spatialRef.baseName, spatialRef.spatialReference.name))
