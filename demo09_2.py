#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	File name: demo09_1.py
	Author:  Shawn Hutchinson
	Description: Example script that features lists and loops
	Data created: 9/25/2023
	Python version: 3.9.16
"""

# Import required module(s) 
import arcpy

# Create local variable(s)
targetWs = input("Enter target workspace: ")
inFc = "ks_ecoregions"
clipFc = "ks_major_rivers"
fields = ["US_L3NAME", "NA_L1CODE"]

# Set environments
arcpy.env.workspace = targetWs
arcpy.env.overwriteOutput = True

# Explode multiple polygon file into multiple files
arcpy.SplitByAttributes_analysis(inFc, targetWs, fields)	

# Create a list of Great Plains ecoregions
inRegions = arcpy.ListFeatureClasses("*9")

# Use a for loop to iterate through each single GP ecoregion, 
# clip the river file, and give output a custom name
for region in inRegions:
	desc = arcpy.Describe(region)
	arcpy.Clip_analysis(clipFc, region, "Rivers_" + desc.name)

# Clean up deleting outputs NOT in the Great Plains
for region in inRegions:
	arcpy.Delete_management(region)
arcpy.Delete_management("Ozark_Highlands_8")
print("Processing complete and current workspace cleaned!")

# Summarize the job performed by counting and joining results
newFiles = arcpy.ListFeatureClasses("Rivers_*")
count = len(newFiles)
print("A total of {} new files were created:".format(str(count)) + "\n" + 
	  "\n".join(newFiles))