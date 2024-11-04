# Introduction

AI is becoming increasingly important in Earth observations as most parts of the Earth system are continuously monitored by sensors and AI is able to cope  with both the volume of data and the heterogeneous data characteristics. For instance, satellites monitor the atmosphere, land, and ocean with unprecedented accuracy. In FAIRiCUBE the JupyterLab capabilities have been extended to support the application of machine learning (ML) methods on datacubes.

We provide three Python-based best practice Jupyter Notebooks (Credit: DeepESDL) based on a generic use case to showcase the implementation of state-of-the-art machine learning libraries in the FAIRiCUBE Hub environment. Each Jupyter Notebook involves a self-contained workflow, markdown cells, comments and plots for user-friendly application and guidance and is based on one of the three well established open source ML libraries respectively:

1. [scikit-learn](https://scikit-learn.org/stable/)<br>
For classical machine learning such as support vector machines, decision trees, regressions or clustering, scikit-learn provides a broad set of features that fulfills many basic requirements.

2. [TensorFlow/Keras](https://www.tensorflow.org/guide)<br>
Keras provides a high-level API that can be run on the popular execution backend TensorFlow. Due to its simplicity, it fits well to the requirements of those Earth system scientist that do not require to newly develop neuronal network architectures. As PyTorch, TensorFlow is python-based, allows for GPU computation and it supports Deep Learning applications including transfer learning or domain adaptation.

3. [PyTorch](https://pytorch.org/)<br>
For larger neural networks and support for Deep Learning additional ML toolchains are necessary, for example the python-based ML stack PyTorch. With PyTorch, experienced users are supported. It provides low-level API and allows for flexibility to develop and customize deep learning models. It allows for GPU computation and supports transfer learning, domain adaptation, or diverse methods for fine tuning of models.


Model tracking is realized through the usage of [TensorBoard](https://www.tensorflow.org/tensorboard) or
[MLflow](https://mlflow.org/). These tools offer science teams an easy-to-use platform allowing to run and scale their Machine Learning workloads in a collaborative environment supporting versioning and sharing of parameters, models, artefacts, results, etc. within the team and potentially external users.

TensorBoard, as another collaborative tool in this MLOPs space is currently evaluated by the science teams and available as part of the TensorFlow conda kernel to individual users within their JupyterLab session.


One may also want to reuse information gained during model training for a second related task, especially when it comes to a lack of data. A PyTorch based Jupyter Notebook provides the implementation of [Transfer Learning](https://github.com/deepesdl/ML-Toolkit/blob/master/src/transfer_learning.ipynb).


# Overview

* [Getting started with AI-toolkit](ai_toolkit_getting_started.md)
* [AI-toolkit examples](ai_toolkit_examples.md)
* [Introduction to scikit-learn](scikit_introduction.md)
* [Getting started with scikit-learn](scikit_getting_started.md)
* [Scikit-learn examples](scikit_examples.md)
* [Introduction to TensorFlow](tf_introduction.md)
* [Getting started with TensorFlow](tf_getting_started.md)
* [TensorFlow examples](tf_examples.md)
* [Introduction to MLflow](mlflow_introduction.md)
* [TensorBoard Introduction](tb_introduction.md)
* [Introduction to PyTorch](pt_introduction.md)
* [Getting started with PyTorch](pt_getting_started.md)
* [PytTorch examples](pt_examples.md)


