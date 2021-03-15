# CATSAD
China Academic Traffic Sign Amalgamated Dataset

<p align="center" width="100%">
    <img width="33%" src="./catsad.svg"> 
</p>

-----------------------------------------

CATSAD is a Chinese traffic sign recognition meta-dataset. It contains greater than 69,000 classifiable raw images of Chinese traffic signs in greater than 200 categories. These images have been sampled from seven different academic detection and recognition datasets published by Chinese academia. The ability to apply modern classification algorithms to a useful number of sign types is only reasonably realizable via their combination. CATSAD is a not a benchmark, but is a window to further computer vision research in China.

CATSAD is greatly inspired by the German GTSRB and American LISA data benchmarks. The qualitative nature and number of images are of a similar order of magnitude.  The images are of varying size (with a histogram shown in figure 1) with a square aspect ratio. The images are of real-world traffic signs at various angles in various lighting scenarios. 

A python code (resample.py) converts the raw dataset (in raw/) into a form friendly to modern artificial intelligence frameworks (into a folder named data/).  It allows image size standardization as well as removing categories with insufficient numbers. Figure 2 provides the number of categories as a function of minimum number of images in category as a guide for this purpose. 

Documentation connecting to the underlying datasets can be found under the folder documentation/. This details the source and location of each traffic sign image. Any academic use of this dataset should properly reference the various authors listed there. They were vital in creating and publishing their datasets publically which were needed to generate CATSAD. As such, the original publishers should retain all attribution and ownership.

This dataset is originally published in Spring 2021. Any help in improving, correcting, or diversifying it is greatly appreciated. The dataset can be found on github at https://github.com/icfaust/CATSAD
