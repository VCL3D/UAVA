# **UAV Assistant (UAVA) Dataset**

[![Paper](http://img.shields.io/badge/DronePose-arxiv.2008.08823-critical.svg?style=plastic)](https://arxiv.org/abs/2008.08823)
[![Conference](http://img.shields.io/badge/ECCV-2020-blue.svg?style=plastic)](https://eccv2020.eu/)
[![Workshop](http://img.shields.io/badge/R6D-2020-darkblue.svg?style=plastic)](http://cmp.felk.cvut.cz/sixd/workshop_2020/)
[![Project Page](http://img.shields.io/badge/Project-Page-blueviolet.svg?style=plastic)](https://vcl3d.github.io/UAVA/)

## TODO
- [x] Add DJI M2ED drone model.
- [x] Add colour, depth, and silhouettes from an exocentic view.
- [x] Add colour, and depth, from an egocentric view.
- [x] Add UAVA toolset.
- [x] Add data loaders.
- [ ] Add normals, and optical flow from an exocentic view.
- [ ] Add normals, and optical flow from an egocentic view.
- [ ] Add extra drone models.


# UAVA Toolset
A set of tools for working with the [UAVA dataset](https://vcl3d.github.io/UAVA/)
  - PyTorch data loaders
  - Dataset splits
  - Visualisation script

The **UAVA** dataset was generated following a carefully data synthesis pipeline for ensuring the generation of photorealistic images and realistic trajectories.

Please download the [trajectories](https://vcl3d.github.io/UAVA/trajectories/trajectories.zip) before using the scripts.
 

## Data Loading
An example data loading usage can be found in ['visualize_dataset.py'](./visualize_dataset.py) where the dataset is loaded and visualized using visdom.

Given that **UAVA** dataset can be used in a variatety of tasks ranging from computer vision to robotics, data loading can be modified accordingly w.r.t. `drone model` , `camera views`, `image types` and `time frames`.

Apart from the default values, there are some system specific arguments that need to be set up. We provide two indicative cases about how the data structure of each folder should look like. 

- `root_path` that points the root folder of the data (e.g. `"D:\\Data\\Cleaned"`).

<span class="img_container left" style="display: block;">
    <p align="left">
    <img alt="Data structure" height=250 src="images/data_structure.png" style="display:block; margin-right: auto;" title="caption" />
    <br />
    <span class="img_caption" style="display: block; text-align: left;">Data structure snapshot</span>
    </p>
</span>

- `trajectory_path` that points to the trajectory file (e.g. `"D:\\Data\\trajectories"`).

<span class="img_container left" style="display: block;">
    <p align="left">
    <img alt="Trajectory structure" height=250 src="images/trajectory_structure.png" style="display:block; margin-right: auto;" title="caption" />
    <br />
    <span class="img_caption" style="display: block; text-align: left;">Trajectory structure snapshot</span>
    </p>
</span>



## Splits
The data splits follow the same distribution of the [Matterport3D](https://niessner.github.io/Matterport/) dataset and can be found in the [data splits](data%20splits) folder. 
