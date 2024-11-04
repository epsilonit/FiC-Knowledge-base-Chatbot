# How to contribute to the FAIRiCUBE-HUB Community collaboration platform

The content of this collaboration platform is managed via a github repository, which is connected to [ReadTheDocs](https://about.readthedocs.com) resulting in automatically deployments of newly merged contents to its final destination: the [FAIRiCUBE-HUB - Getting started, Examples & How To's](https://fairicube.readthedocs.io/en/latest/)

All documents are provided as Markdown-files (i.e. *.md).
Help with the Markdown-syntax can be found [here](https://daringfireball.net/projects/markdown/syntax)

To contribute to this documentation, you need to:

## First, clone this repository to your local computer:

e.g from the command-line:

    $> git clone git@github.com:FAIRiCUBE/collaboration-platform.git

or by using any other of the other methods offered by github.


## Building the docs (for local usage/evaluation)

The following procedure allows you to view the 'real look' of your editied/created Markdown documents of your local instance, prior to submitting them to the github repository

    $> conda install -c conda-forge mkdocs mkapi
or

    $> pip3 install mkdocs mkapi

Thereafter, you can build a local version of the documentation by:

    $> cd  <to the directory containing the 'mkdocs.yml' file>

then run:

    $> mkdocs serve -a localhost:8001

this will provide a local web-server offering the newly build documentation at the following location: **http://localhost:8001/**

This allows it to easily check locally for all the formatting , structuring, etc. before uploading it to the repository.


## Start providing/editing documents

Before you begin, please make sure that you **START A NEW BRANCH** for your additions/editing.

    $> git checkout -b  <new_branch_name>
<br>
_**Note:**_ *The Structure of the collaboration site (provided on the left side) is defined in the* _**mkdocs.yml**_ *file.*<br>
*Changes to this structure are not immediately viewable under **http://localhost:8001/**.* <br>
*In order to see you changes there, you need to restart the local web-server ('mkdocs serve -a localhost:8001').*<br>
*All other changes to the documents are immediately rendered locally.*

Now you can start creating your content or edit already existing information.

Once you finished all your edits or newly created documents and have thoroughly checked them in your local instance, you may submit your input to the git repository to be merged into the main branch.

First you need to commit the changes to your local git branch. Please always provide a meaningful commit-message with your commits.

    $> git commit -m "this is an explanation how to commit changes"  <doument_1> <document_2> ....

Once the commit is performed, you may push your changs to the github repository

For the first push of your branch use:

    $> git push --set-upstream origin   <new_branch_name>

For later pushes, you may just use

    $> git push


Once the **push** was successful you need to create a **merge request** for your submitted changes. Best is to do this directly at the website of the [collaboration-platform](https://github.com/FAIRiCUBE/collaboration-platform) repository.
At the website click on *"Pull Requests"* then click the Button *"Create Pull Request"*. Thereafter choose **your branch name** as source and **main** as target.

Once the repository owner accepts your merge request, the content will be merged and automatically deployed to *readthedocs.io* and soon after it will be available at [https://fairicube.readthedocs.io](https://fairicube.readthedocs.io).

_**Note:**_ *After  a successful merge the repository owner will delete your submitted branch! <br> You should do the same in your local instance by issuing:*

    $> git branch -d <your_branch_name>


<br>

##### Some rules we ask you to follow:

* Please try to keep the structure as much as possible. Try not to introduce unnecessary directories.
* Use issues in the github [collaboration-platform](https://github.com/FAIRiCUBE/collaboration-platform) repository  for questions or for discussion.
* The general *Netiquette* applies


<br>



