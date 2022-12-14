# Python basic imaging processing course

Here are the packages this course will use:<br>
tifffile: tiff import and export<br>
pandas: dataframe manipulation<br>
numpy: multidimensional arrays<br>
matplotlib: standard plotting package including image viewing<br>
scipy ndimage: core image processing tools including label comprehension<br>

How to install the packates with conda:<br>
Create and environment called ipenv:
```
conda create -n ipenv python=3.8
```
Activate the environment:
```
conda activate ipenv
```
Optional: set ipykernel in jupyter:
```
pip install --user ipykernel
python -m ipykernel install --user --name=ipenv
```
Install packages:
```
conda install -c conda-forge jupyter numpy pandas scipy matplotlib tifffile pillow
```

To activate environment: `conda activate ipenv`

To deactivate: `conda deactivate`

### To open notebook environment gui: 
  * type `conda activate ipenv`: 
  * type `cmd` to switch to command prompt
  * type `activate base`
  * type `jupyter notebook`
  * to exit command prompt: type `exit`
  * to deactivate the environment: type `conda deactivate`



Alternative: To install from environment.yml file (environment will be called ipenv):
```
conda env create -f environment.yml
```

## Instructions
The notebook image_processing_basics.ipynb is the starting place for the course and talks about pixels and image display in python.

The notebook image_label_measurements.ipynb talks about segmenting and labeling image objects and performing measurements on them.

Image sources: the images are from https://imagej.nih.gov/ij/images. They have been made into tif files for easy import.
