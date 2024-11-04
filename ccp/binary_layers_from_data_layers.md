# How to create binary layers from data layer in QGIS

## Reference Use Case 
Common

## Problem statement 
A binary layer simplifies data into two categories (e.g., presence/absence, true/false), which requires setting a threshold value to determine these categories.

##  Envisaged impact
Creating binary layers from data layers in QGIS can present challenges, particularly in terms of accuracy and threshold selection. Choosing an inappropriate threshold can lead to misclassification, where significant data might be oversimplified or important details lost. Additionally, binary conversion can introduce artifacts or errors, especially in complex datasets with subtle variations. This process may also reduce the granularity of the original data, impacting the precision of subsequent analyses or visualizations.

## Affected component of FAIRiCUBE-Hub
FAIRiCUBE Lab (Storage, CPU, RAM and Network) 

## Proposed solution
[How to create binary layers from data layer in QGIS is explained at this link](https://github.com/FAIRiCUBE/common-code/tree/main/QGIS-functionality). 

## Expected benefits
Creating binary layers in QGIS can streamline workflows, enhance clarity and focus analysis on specific aspects of the data.