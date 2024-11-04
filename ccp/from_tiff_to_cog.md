# How to transform a GeoTiff file into a Cloud-Optimised-Geotiff

## Reference Use Case 
Common

## Problem statement 
Using GeoTIFFs in the cloud presents several challenges, particularly related to efficiency and scalability. GeoTIFF files are often large and stored as monolithic blocks, making them cumbersome to work with in cloud environments where data access needs to be fast and scalable. When performing analyses on cloud platforms, retrieving entire GeoTIFFs, especially when only small portions of the data are needed, leads to unnecessary data transfer, increased costs and slower processing times.

##  Envisaged impact
This problem causes execution time and resource consumption to increase exponentially.

## Affected component of FAIRiCUBE-Hub
FAIRiCUBE Lab (Storage, CPU, RAM and Network) 

## Proposed solution
[How to transform a GeoTiff file into a Cloud-Optimised-Geotiff is explained at this link](https://github.com/FAIRiCUBE/common-code/tree/main/fromTIFF_to_COG). 

## Expected benefits
The Cloud Optimized GeoTIFF (COG) addresses the challenges of using traditional GeoTIFFs in the cloud by optimizing the file format for efficient cloud-based access. COGs are structured with internal tiling and overviews, allowing users to request and retrieve only the specific portions of the data they need, rather than downloading the entire file. This reduces data transfer, lowers costs and speeds up processing. Additionally, COGs are compatible with web services and can be streamed directly over HTTP, making them ideal for scalable geospatial analysis in cloud environments.