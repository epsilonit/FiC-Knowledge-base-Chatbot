# Getting Started with AI-toolkit

Jupyter Notebooks typically follow the same architecture involving five major sections, which are supported by markdown cells, comments and plots:

* Import necessary libraries and mltools
* Load data (s3 object store)
    * Initialize data mask
* Assign train/test split
    * Random sampling
    * Block sampling
* Model set-up (linear regression with 1 node/ shallow neural network)
* Model training and testing
    * Iteration over chunks of the datacubes and subsequent sampling
    * Preprocessing (filtering NaNs, standardization, normalization)
    * Get train/test data
    * Generate training batches using existing data loading and transformation mechanisms from Keras and PyTorch (DataGenerator, DataLoader)
    * Train model, return error and loss
    * Evaluate model
    * Plot results

It is mandatory to enable machine learning that respects the basic principles of geo-data way beyond naive applications of machine learning in the Earth system context. To avoid auto-correlation during the training phase of the model, data sampling is preferably  guided by a block sampling strategy. Data blocks are chunks of datacubes, rectangular shaped, varying in size and number of data points.

The workflow is implemented (Credit: DeepESDL) for three python-based Machine Learning libraries (scikit-learn, PyTorch, TensorFlow) based on a generic use case and will be provided as [Jupyter Notebooks](ai_toolkit_examples.md)

<p align="center">
<img src="../../images/mltoolkit_scheme.png" width="70%" height="70%">
</p>
<p align = "center"><i>
Machine Learning workflow on Analysis Ready Data Cubes (Credit: DeepESDL)</i>
</p>

