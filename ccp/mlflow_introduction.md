# FAIRiCUBE - MLflow Introduction

![MLflow logo](../images/mlflow_logo.png)

Each Use Case team decides which apps shall be made available. One of these apps is MLflow.

MLflow is an open-source platform for managing the end-to-end machine learning lifecycle. It allows the user to track experiments, package code into reproducible runs, and share and deploy models.<br>
MLflow can be incorporated into Jupyter notebooks or other code and supports multiple programming languages. MLflow provides a comprehensive solution for managing the machine learning lifecycle, from tracking experiments to deploying models. It is widely used in industry and academia and is constantly evolving to support the latest trends and technologies in the field of machine learning.<br>
MLflow supports the MLOps pipelines particularly to log and evaluate experiment runs as well as to store models in a registry​. Persistent MLflow deployments are made available on team level to allow each team member to compare their experiments with those of the other team members and to use the trained models of others.

At a high level, MLflow consists of four main components: tracking, projects, models, and registry. All components can be accessed via Python code in the FAIRiCUBE Lab.


## MLflow Tracking

The MLflow tracking component (here an example form DeepESDL) allows users to log and track training parameters, code, and output metrics from their machine learning experiments.

![mlflow.png](../images/mlflow.png)
<p align = "center">
  <i>Collaborative Experiment Tracking with MLflow</i>
</p>

The tracking component provides an API for Python, R, and other languages, as well as an UI for visualising experiments and comparing different runs. The tracking server can store data in various backends, including a local file system, an Amazon S3 bucket, or a PostgreSQL database.

MLflow Tracking uses the concept of runs, which are executions of some piece of data science code, e.g., training of models. MLflow Tracking supports auto-logging for many classic libraries such as TensorFlow, Scikit-Learn, Spark, or Pytorch, but manual logging is available in other cases. Runs can be stored as local files, on a remote server, or into an SQLAlchemy compatible database. The tracking UI allows to directly visualise tracked metrics and search for the best components.

## MLflow Projects

The MLflow projects component provides a standard format for packaging and distributing machine learning code, including dependencies, in a reproducible way. Projects can be run locally or on a cluster, and MLflow can manage the environment and dependencies for each run.

In addition, the Projects component includes an API and command-line tools for running projects, making it possible to chain together projects into workflows. In the MLproject file it is possible to define the software environment and entry points with parameters to define workflow.

## MLflow Models

The models component allows users to easily package models in a standard format for deployment. Models can be exported in multiple formats, including TensorFlow, PyTorch, and ONNX, and can be deployed using a variety of tools, including Docker, Kubernetes, and Amazon SageMaker.

It is also possible to access models with standard ways as REST API or batch inference on Apache Spark. Native flavours allow MLflow models to be treated with corresponding functions without the need to integrate tools with each library. Flavours can be defined in the MLmodel file. Model signatures are defining outputs and inputs needed for deploying models as a REST API.

The Model API allows saving, loading, and logging of the model also as adding different flavours. MLflow also provides an evaluate API to evaluate previously built models on one or more datasets.

## MLflow Model Registry

Finally, the MLflow Model Registry component allows users to store, manage, and deploy models in a central repository. Models can be versioned, and access can be controlled using role-based access control. The Model Registry works both in UI and API versions.

It provides model lineage (which MLflow experiment and run produced the model), model versioning, stage transitions (for example from staging to production), and annotations. Model versioning allows models to be archived and redeployed in the future.

