# CATSAD
China Academic Traffic Sign Amalgamated Dataset

<p align="center" width="100%">
    <img width="33%" src="./catsad.svg"> 
</p>

This repository is a combination of 3 Chinese road sign datasets from various Chinese academics.  Due to legal limitations within the People's Republic of China, acquiring and publishing such data is forbidden without certain approvals and licenses.  By leveraging these publically published works done by others in China, such legal problems are avoided and a more complete dataset for traffic sign recognition is possible. This dataset contains more than 50,000 images of more than 60 types of Chinese roadsigns extracted from 3+ other traffic sign recognition and detection datasets.  This includes non-standard versions of some traffic signs to better represent the real-world driving experience within China. 

The storage structure has been set up in such a way to minimize data engineering so the user can focus on the algorithmic implementation. Specifically, it has been designed to work out-of-the-box with Keras' image_dataset_from_directory function and with an associated Pytorch dataloader. The images vary in size from 5x5 to 300x300 and are square, roughly centered, with the sign existing in approximately the inner 84% of the image. Associated documentation is included but stored separately from the images, allowing for full tracibility to the underlying datasets.  This not only secures the legality of CATSAD, but expands the usefulness in sign detection in the other datasets by correcting their errors.

The images within CATSAD are not necessarily uniform or consistent, it is hoped that this will make recognition algorithms more robust. For example, the centering and size of the traffic signs within an image can vary due to the underlying dataset.  Some images in the dataset will contain regions of black in order to maintain a square shape (due to being at the image-edge from the derivative dataset). Other images within CATSAD may have more than one sign, and occlusions and oblique angles can make the signs themselves occupy significantly less area of the image. Some of the underlying images which make the other datasets were aquired using a rolling shutter causing skew, while other images contain are over or under staturation or even lens flare. CATSAD has only modified the location of some signs or their labels from the other datasets. This was done to correct errors in sign labels or to make the full boundary of the traffic sign visible.

All attribution and ownership is retained by the original publishers. All works derivative from this dataset should follow the standards and rules of these underlying datasets. Links, citation guidelines, and authors of the contained datsets are listed below.
