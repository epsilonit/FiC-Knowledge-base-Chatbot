# FAIRICUBE Hub

## Introduction

The FAIRiCUBE Hub provides a complete working environment that allows users to access algorithms and data remotely, providing computing resources and tools they might not otherwise have, and avoiding the need to download and manage large amounts of data (e.g. Earth Observation data), increasing the analytical power available to researchers, industry, operational service providers, regional authorities and policy analysts.

The Hub is a crosscutting platform and framework for data ingestion, provision, analysis, processing and dissemination, to unleash the potential of environmental, biodiversity and climate data through dedicated European data spaces. Within this project, TRL 7 will be attained, together with the necessary governance aspects to assure continued maintenance of the FAIRiCUBE Hub beyond the project lifespan.

The Hub embraces the entire FAIRiCUBE technical environment, including the FAIRiCUBE Catalog, FAIRiCUBE Services and Applications, and the FAIRiCUBE Lab.

It is based on the existing software named EOxHub, which is extended in two ways to provide the FAIRiCUBE *Collaborative Development Tools*:

* Extended support for teams as part of the multi-user plan. Allow for easier sharing of versioned notebooks and other artifacts within the team but not necessarily the public.
* Integrated support for Machine Learning (ML) workflows. This includes the versioning, sharing, and collaborative using of all ML artifacts like code, data, models, results, etc. Based on user feedback, the readily available Open-Source tools like Data Version Control (DVC), MLflow, Kubeflow, or similar, will be integrated during the project.

The FAIRiCUBE Hub manages use cases and their users. The Hub provides for each use case a workspace or tenant,
assigns project resources, hosts project artifacts, provides a shared storage for result dissemination, and integrates team collaboration tools. It also controls visibility of results of individual user projects so that they can be made part of a FAIRiCUBE public portrayal.

A FAIRiCUBE user project comprises numerous own applications, interfaces, services, and data available in the provided workspace.

## Hub Components Overview

* **[FAIRiCUBE Catalog](../user_guide/fic_catalog.md):** The integrated catalog providing metadata and references to ingested datasets, processes, and models available from FAIRiCUBE.
* **[FAIRiCUBE Workspace]:** The user area within the FAIRiCUBE Lab where users are able to collaborate and share the content of their workspaces.
* **[FAIRiCUBE Lab](../user_guide/eox_lab.md):** A single container for all workspaces, providing the interface to back-ends via various back-end protocols as well as an execution environment for user provided workloads.
* **[FAIRiCUBE Query Tool]:** The interactive Query Tool enabling both experts and non-experts to easily discover and analyse the FAIRiCUBE data analysis and processing resources (pipelines, pre-processing, ML models and algorithms …).
* **[FAIRiCUBE Knowledge Base](../index.md):**  A digital library where users can explore and benefit from the experience, know-how and services of the FAIRICUBE project. Its aim is to provide appropriate knowledge on how to apply algorithms and ML techniques to solve requirements similar to the FAIRICUBE use cases.

The figure below provides an Overview of the overall FAIRiCUBE Architecture.

<p align="center">
    <img src="../../images/fairicube_architecture.gif" alt="FAIRiCUBE Architectur.gif" />
</p>


In the table below find the links to the FAIRiCUBE services currently developed and accessible.

| Service name | Link to service | Description |
| ------------ | --------------- | ----------- |
| FAIRiCUBE Knowledge Base | [https://fairicube.readthedocs.io](https://fairicube.readthedocs.io) | Landing page for project documentation |
| FAIRiCUBE Catalog | [https://catalog.eoxhub.fairicube.eu/](https://catalog.eoxhub.fairicube.eu/) | Catalog of data and analysis/processing (a/p) resources |
| FAIRiCUBE Lab Rasdaman | [https://fairicube.rasdaman.com/](https://fairicube.rasdaman.com/) | Workspace to access and process data |
| FAIRiCUBE Lab EOX | [https://eoxhub.fairicube.eu/](https://eoxhub.fairicube.eu/) | Workspace to access and process data |
| FAIRiCUBE Query Tool | [https://fairicube-kb.dev.epsilon-italia.it/](https://fairicube-kb.dev.epsilon-italia.it/) | Interactive tool enabling searches over analysis and processing resources |
| FAIRiCUBE GitHub | [https://github.com/FAIRiCUBE](https://github.com/FAIRiCUBE) | Main GitHub project with thematic and use case repositories |
| FAIRiCUBE Data Metadata Ingestion Forms | [https://catalog-editor.eoxhub.fairicube.eu/](https://catalog-editor.eoxhub.fairicube.eu/) | Entry to data meta data ingestion (shared with data ingestion) |
| FAIRiCUBE a/p Resources Metadata Ingestion Forms | [https://fairicube-md.dev.epsilon-italia.it/](https://fairicube-md.dev.epsilon-italia.it/) | Entry to analysis and processing meta data ingestion  |


