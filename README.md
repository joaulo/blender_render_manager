![Blender Render Manager](https://www.joaulo.com/media/projects/project_blender-render-manager-blender-addon/preview_big.jpg)
# blender-render-manager

This addon derives from the need to render a certain number of cameras from the scene across the night.

It currently has a number of limitations, for this reason it has its usefulness in a specific context but I'd like to make it grow in the future by expanding the possibilities of use.

# Installation

It installs like a standard Blender addon, just download the .zip file on your PC, then go to *Blender> Edit> Preferences...*, use the *Install…* button and use the File Browser to select the .zip add-on file. For more information, refer to the [Blender manual page](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html?highlight=preferences).

# How does it work?

Once installed and activated, the addon interface will be visible in a dedicated panel called "*Render Manager*" in the "*Output Properties*" section:

![Render Manager Panel](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_191102.jpeg)

In order from top to bottom:

* **Render output**: select the folder where you want to save the renders
* **Select a collection**: select a collection from the list, containing one or more cameras
* **Render Manager::Images**: start rendering static images (at the current frame) in sequence on all the cameras detected in the selected *Collection* and in all *nested Collections*
* **Render Manager::Animations**: button to start rendering animations in sequence on all the cameras detected in the selected *Collection* and in all *nested Collections*

You can save the render settings to a file and reload them later before launching the renders. To do this, the panels below are used:

* **Load Settings**
* **Save Settings**

In both panels there is a field where you can select the path and the file to load/save render settings.

# Limitations and known problems

* actually it is not possible to use different render settings for each camera detected in a collection! It is suggested to group the cameras in different collections according to the render settings. As a consequence of using the same settings, animations also start and end from the same frames.
* currently the extension of the files saved and loaded by the addon is not imposed, however it will be adopted the extension "*.brm*" in the future
* do not use the relative path in the selection of files or folders within the addon, use only absolute paths! Due to a still unresolved problem, using the relative path with the file or folder will result in an error message when executing the command. To use absolute paths, after clicking on the folder icon next to the selection field, use the following settings in the path selection window:

   * *select the gear icon at the top right:*

   ![path settings](https://www.joaulo.com/media/uploads/2020/05/10/screenshot_20200426_211442.jpeg)

   * *disable the checkbox:*

   ![checkbox_wrong](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211522.jpeg)
   ![checkbox_right](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211731.jpeg)

   * *verify that the path in the field is the full path to the file:*

   ![full_path](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211802.jpeg)

# TO DO

* save different settings for each camera
* load specific settings for each camera before launching the render
* manage file extension
* add progress bar to show rendering process
* add a button to stop render process
