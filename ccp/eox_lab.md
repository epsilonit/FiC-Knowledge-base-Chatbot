# FAIRiCUBE EOX Lab

<!-- ![img.png](../../images/Jupyter_FAIRiCUBE_Kernels.png) -->
<!--
<p align="center">
    <img src="../img/eoxhub_capabilities.png" alt="EOxHub Capabilities.png" style="height: 160px; width:400px;"/>
</p>
-->

## Basic usage

This section provides a brief introduction for users to the basic features of
the JupyterLab environment as offered by the FAIRiCUBE Lab.
For more in-depth documentation on the various components, see the links in the
section [Further Information](further-information.md).


### FAIRICUBE Lab Sign-Up / Sign-In

The FAIRICUBE EOX Lab is a moderated service i.e. access has to be granted by an Administrator.
Once the access is granted the login is possible.

To this, we kindly ask you to write as an email at `fairicube@nilu.no` with `Subject: FAIRiCUBE - New user` and we will see
if we can already onboard you.

To use the FAIRiCUBE JupyterLab environment, navigate to <https://eoxhub.fairicube.eu>
with a web browser (a recent version of Firefox, Chrome, or Safari is recommended).

In FAIRiCUBE you may use a combination of Username & Password or a GitHub account to authenticate. So if you are already registered as a FAIRiCUBE user, please use your GitHub account to log in.

<p align="center">
    <img src="../../images/FAIRiCUBE_Hub_Login.png" alt="FAIRiCUBE_Hub_Login.png"  style="height: 300px; width:291px;"/>
<!--    <img src="../img/FAIRiCUBE_Hub_Login.png" alt="FAIRiCUBE_Hub_Login.png" style="height: 160px; width:400px;"/>-->
</p>


### Use Case specific Workplace Profiles

If your Jupyter server is not already running, you may be presented with a menu of user JupyterLab profiles to use for your session; there might be one or more JupyterLab profiles to choose from, depending on the computational resources needs of your team. Please select a suitable profile for your current task; it might not always require the profile with the strongest computational resources available.

After choosing your environment, you will see a progress bar appearing for a few
moments while it is started for you. The JupyterLab interface will then appear in your web browser, ready for use.

Currently these FAIRiCUBE Use Case specific environments are provided which can be chosen by the user.

<p align="center">
    <img src="../../images/JupyterHub_server_options-use-cases.png" alt="JupyterHub_server_options-use-cases.png"/>
</p>


### JupyterLab workspace launcher

The launcher provides access to various Jupyter Notebooks, tools (e.g. console, VS-Code), and applications (e.g. MLflow, TensorBoard, NotebookViewer) as configured.

Furthermore it shows the files in the [local storage](storage.md) and, if configured, provides access to a shared folder using [Object storage](storage.md) granting direct access to the provided datasets as well as to Machine Learning Notebooks.

<p align="center">
    <img src="../../images/JupyterLab_workspace_launcher.png" alt="JupyterLab Workspace Notebook Launcher"/>
</p>

Here the users can develop and run their own code as well as share it with other FAIRiCUBE users or make them available via a curated shared folder again leveraging [Object storage](storage.md).


### JupyterLab workspace monitoring

The workspace also provides interesting monitoring information about the usage.

<p align="center">
    <img src="../../images/JupyterLab_workspace_Node_monitoring.png" alt="JupyterLab_workspace_Node_monitoring.png"/>
</p>


### Ending a Session

The correct way to end a session is to execute the following procedure:

* Use the Menu and click:  *File -> Hub control Panel*
* this will forward you to the following, where you should click the `Stop My Server` Button.
* just using:  *File -> Log Out* will not stop your server and unnecessary costs my occur

<p align="center">
    <img src="../../images/JupyterHub_start-stop_server.png" alt="JupyterHub_start-stop_server.png"/>
</p>

This ensures that no unnecessary costs are incurred due to a forgotten session (e.g. an open Tab in your Browser).
In any case, unused session will be closed (culling) after a pre-defined time.

Once the Server has stopped (see Figure in next section) you can regularly `Log Out` using the `Logout` button located in the Top-right corner.


### Changing a JupyterLab profile

If you have already started your session but you need to change the JupyterLab profile,
you can do this by selecting *File -> Hub control panel* from the menu within
JupyterLab. Then click the `Stop my server` button and wait for your current
server to shut down.

After you clicked the `Stop My Server` button you will be presented with:

<p align="center">
    <img src="../../images/JupyterHub_start_server.png" alt="JupyterHub_start_server.png"/>
</p>

If you click the `Start My Server` button you will be again confronted with the `Use Case specific Workplace Profiles`.


### Logging out of Jupyter Lab

To log out, select *File -> Log out* from the menu within JupyterLab.

Note that your JupyterLab session will continue in the background even after you have logged out, but will eventually be terminated due to inactivity.<br>
If you wish to stop your session explicitly, you can use the hub control panel as described in the [Ending a Session](#ending-a-session) section above.


### Getting-started notebooks

You can find example notebooks in FAIRiCUBE JupyterLab to help you to get
started.

To access them:

* Head to the JupyterLab `Launcher`
![JupyterLab_workspace_launcher.png](../images/JupyterLab_workspace_launcher.png)
If your `Launcher` is not visible right away, you can open it via the `plus` button in the top left corner, which is highlighted in blue in the screenshot.
* Once selected you see several example notebooks:
![JupyterLab_workspace_Notebook_Viewer.png](../images/JupyterLab_workspace_Notebook_Viewer.png)
* Select one of them, and you will see a preview of the notebook, to execute the selected notebook click on `EXECUTE NOTEBOOK` in the top right corner
![JupyterLab_workspace_Notebook_Example.png](../images/JupyterLab_workspace_Notebook_Example.png)
* The notebook is copied into your workspace, and you can run it and adjust it according to your needs.



## Advanced usage

### Python environment selection of the Jupyter Kernel

If you wish to use a special set of python packages, you can adjust it in the top right corner of the notebook. Next, a drop-down menu will appear, and you can select the desired kernel environment from it.

<p align="center">
    <img src="../../images/Jupyter_FAIRiCUBE_Kernels.png" alt="JupyterLab FAIRiCUBE Kernel selection" style="height:340px; width:200px;"/>
</p>

To get a custom environment which suits your needs, please contact the FAIRiCUBE
team directly.


### Creating custom team python environment

Up to two team members may create a custom python conda environment for a team. Please inform the FAIRiCUBE Team who should be granted these permissions.

Steps to create custom team conda environments:

* Head over to <https://eoxhub.fairicube.eu/conda-store/>
* Login with your GitHub Account which you also use to access the FAIRiCUBE JupyterLab
* If you have never created a custom environment, there will be none listed.
* Click on the Plus-sign next to *Environments*
* In the top section, select the namespace for which to create the custom environment. There might be more than one if you are part of several teams. If you are unsure which namespace you should use, have a look at the Server Options overview of the FAIRiCUBE JupyterLab.
* You may either choose an environment.yml file to upload or paste your [environment configuration](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually) into the window directly.
It should look something like this example:

        channels:
            - conda-forge
        dependencies:
            - xcube=1.1.1
            - xcube-cds
            - xcube-sh
            - xcube-cmems
            - xcube-cci
            - xcube_geodb
            - boto3
            - rasterio>=1.3.6
            - cartopy
            - ipykernel
        name: xcube-1.1.1

* Make sure to set a meaningful value to the environment's `name` property, so also your teammates will know what it is about.
* Once you are happy with your environment hit submit and grab a coffee. It will take some time to create your custom environment.
* After submission, it will appear in the overview on https://eoxhub.fairicube.eu/conda-store/
* You can click on the name of your newly created environment and see its status. There are three different statuses: Building, Completed, Failed
* If you click on the build number you can see the logs. This might be useful if the build has failed.
* Once the build is completed, you need to refresh your browser window to make it available in the kernel selection. Instructions how to change the kernel to your custom environment are provided in the section [python environment selection of the jupyter kernel](#python-environment-selection-of-the-jupyter-kernel).

You can also modify an existing environment and rebuild it; the conda-store will keep all the builds' logs.

It will look similar to the screenshot below.
![conda-builds.png](../images/conda-builds.webp)

The conda-build highlighted in green is the one, which you will use in you
FAIRiCUBE JupyterLab, per default it is the latest successful build. If you
wish to make a different build the one to be used in FAIRiCUBE JupyterLab,
select the check mark in the blue button panel of the desired conda-build.
The reload button in the blue button panel will trigger a rebuild of the
conda-environment specification of the selected conda-build. The bin button
deletes the conda-build of the selected conda-build.


## Example Notebooks

A series of helpful Jupyter Notebook Examples is provided under [Jupyter Notebook Examples](../user_guide/lab_examples.md)

