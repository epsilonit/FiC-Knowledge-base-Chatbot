# How to speed-up NetCDF data loading and processing time on cloud environments

## Reference Use Case 
[UC1](https://github.com/FAIRiCUBE/uc1-urban-climate/tree/master)

## Problem statement 
The scope is to process 1 year of hourly climate data (around 14GB in NetCDF) to produce daily statistics for selected EU cities, using dask to (hopefully) speedup data loading and processing. However, the script runtime is considerably slower when executed on FAIRiCube Hub than when executed locally. 

##  Envisaged impact
This problem causes execution time and resource consumption to increase exponentially (up to 10x in some cases).

## Affected component of FAIRiCUBE-Hub
FAIRiCUBE Lab (Storage, CPU, RAM and Network) 

## Proposed solution
Traditional file formats (e.g. tiff, netCDF) cause a lot of network traffic and slow down the computation when the file resides on the cloud. <br> Cloud-optimized format like COG, zarr are designed to overcome this problem.

## Expected benefits
The use of cloud-optimised formats results in exponentially better performance (in terms of execution time and resources consumed) than traditional formats such as NetCDF.
