# FAIRiCUBE Storage

Two types of storage, "File Storage" and "Object Storage", are provided with slightly different capabilities.

**What storage to use:**

* Do you need the data only locally, i.e., in JupyterLab? The recommended storage is your local workspace.
* Do you want to share the data with all users in your Use Case or do you need external access like via Sentinel Hub services? Please use the team shared bucket which is by default mounted at `~/s3/`.
* Do you want to share the data with all users of FAIRiCUBE or even external? Please use the common bucket which is by default mounted at `~/.fairicube-bucket/`.

## File Storage

Per default a user in a [FAIRiCUBE EOX Lab JupyterLab session](./eox_lab.md) gets access to their personal workspace, to a team shared directory as well as to a common shared one. The directory shared with the Use Case team is mounted under `~/team_extra/` whereas the common shared one is mounted under `~/.shared/fairicube/`. This common shared folder is not directly visible in the JupyterLab file browser interface as it is a hidden directory (note the `.`in the name) but can be accessed from notebooks or their content viewed via the commandline (i.e. via Terminal).

The personal workspace as well as the shared folders are persisted on File Storage and are only available in JupyterLab.

## Object Storage

In addition, Object Storage buckets are provided: 

* One separately for each Use Case
* A common bucket for all of FAIRiCUBE

Using the s3 protocol this buckets can be accessed from anywhere (i.e., if permissions are granted). These buckets can for example be used with [Sentinel Hub](../external_resource/sentinelhub_access.md).

The Use Case specific Object Storage bucket is, for convenience, mounted to `~/s3` for each user but preferably used via the `s3` protocol.

The common bucket is accessible to all Use Cases. This is the `fairicube` bucket where access keys are shared for usage. For convenience this bucket is typically mounted for each user to `~/.fairicube-bucket/`. Though possible, it is not recommended to add this directory permanently (eg. via symbolic linking) to the JupyterLab session, since this could slow down the session's performance considerably if a high number of files is stored on the bucket.

## Sharing

Data stored on any of the Object Storage buckets can be shared via various mechanisms and services. Access to the services can be granted publicly or to authorized users only, depending on the capabilities of the software tool used.

An additional consideration to take into account are the costs incurred that need to be covered either by the service provider or the consumer.

The currently available services are:

* Standardized API services provided by [Sentinel Hub](../external_resource/sentinelhub_access.md)
* Direct access to the objects via S3 API
* HTTPS file access provided via [AWS CloudFront CDN](https://aws.amazon.com/cloudfront/), which supports capabilities like custom domains, security, availability, and even adding own ones via lambda functions
* Time-limited sharing via [presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)

Potential future services include:

* Standardized API services provided by further software supporting Object Storage, like the [View Server](https://gitlab.eox.at/vs/vs) deployed in the EOxHub environment of FAIRiCUBE (needs to be evaluated on a case-by-case basis).

### Sentinel Hub

The required bucket settings, to grant Sentinel Hub access, are applied to all shared buckets.

After providing data to an Object Storage bucket it needs to be registered in a [Bring Your Own COG (BYOC) collection](https://docs.sentinel-hub.com/api/latest/api/byoc/). This BYOC collection can either be used directly or in layers of map configurations.

The provider can either share the data by sharing the collection ID or by sharing the map configuration ID. The map configuration ID is typically shared as OGC service capabilities like a WMS layer.

It is important to consider who is paying for the services.

The data provider always needs an Sentinel Hub (SH) subscription and in case of sharing the map configuration, requests count towards the data provider's processing units.

The BYOC collection ID can only be used via an SH subscription and thus the usage counts towards the processing units of the data consumer.

### S3 API

Direct access to a bucket or objects can be granted either to [individual users or publicly](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html). An interesting configuration option in this case is the so-called [*Requester Pays* option](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html). If this option is enabled the data consumer needs to use an AWS account which has to cover the incurred costs.

Public buckets should be used with caution as they easily incur considerable [costs](https://aws.amazon.com/s3/pricing/). The cost elements are data transfer (~0,09€/GB) and number of requests (~0,0004€/1.000 requests) in addition to storage costs (~0,022€/GB/month).

(PS:  Keep in mind that eg. for maps each map-tile shown needs a single request).

### AWS CloudFront CDN

Buckets can be easily configured as origin for the [AWS CloudFront CDN](https://aws.amazon.com/cloudfront/), which adds quite a number of standard CDN configuration capabilities, for direct file access, to a bucket. Also for high bandwidth buckets it should be noted that data transfer via CloudFront is generally cheaper compared to direct bucket access.

### Presigned URLs

[Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) are ideal for time-limited sharing. However, note that costs are still incurred with using presigned URLs.
