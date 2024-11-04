# FAIRiCUBE Hub platform

The FAIRiCUBE Hub is based on the existing software named EOxHub, which is also used to power, e.g., the [EuroDataCube (EDC) Marketplace](https://eurodatacube.com/marketplace), the [EDC EOxHub Workspace](https://eurodatacube.com/marketplace/infra/edc_eoxhub_workspace), the [Rapid Action for Citicens with Earth Observation (RACE) Dashboard](https://race.esa.int), the [EO Dashboard](https://eodashboard.org/), the [Polar Thematic Exploitation Platform (PolarTEP)](https://polartep.polarview.org), the [Deep Earth System Data Lab (DeepESDL) platform](https://www.earthsystemdatalab.net/) as well as various other science projects, workshops & contests.

EOxHub is a platform and workflow management runtime for Earth Observation services and apps. EOxHub can be branded to provide a project spcific Hub & Marketplace and can be deployed on any cloud, offering a managed Kubernetes service. <br>
The designated cloud for FAIRiCUBE is Amazon Web Services (AWS) in the Europe Frankfurt region, fulfilling the requirements with the managed Elastic Kubernetes Service (EKS).

### EOxHub platform

The EOxHub provides:

* Headless notebook execution
* Interactive managed Jupyter instances
* Notebook and App sharing
* Curated base images
* App deployment and execution
* Bring Your Own Algorithm to share and sell
* Different flavors of computational resources
* Shared storage
* Options to customize your resources

Technically EOxHub is split into the *Control Plane* and the *Worker Plane*. The Worker Plane is where all workloads from users are run at runtime. <br>

The *Control Plane* is configured to provide the following:

* User Management
* Access control
* User Workspaces (Tenants)
* Workspace Dashboard
* Service subscription management
* Marketplace
* Allocation functions for cloud resources and Data Services
* Deployment service
* Workload management functions
* Docker Image administration/assignment
* Example notebook catalogue supporting user contributions
* Automated verification of example notebooks
* Accounting and billing (voucher handling)


Deploying user workloads on the *Worker Plane *is performed on configured
autoscaling groups using the managed Elastic Container Service (ECS) of AWS.
This setup ensures, that only actually required resources are used and
thus need to be paid.

![EOxHub](../images/eoxhub.png)

The figure above shows the App deployment in user Workspaces.<br>
The sequence of steps is:

* The App or Notebook Developer pushes the App source code to the Code Management tool,
* adds the App as Docker image, and
* registers the App at the Marketplace.<br>

The App Consumer discovers and requests the App and triggers the deployment of the App to use it in their workspace to be run on the cloud infrastructure. The App is now available to be used by the Consumer within the resources provided in their workspace subscription.



