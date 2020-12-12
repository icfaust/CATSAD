# CATSAD
China Academic Traffic Sign Amalgamated Dataset

![CATSAD](./catsad.svg)

This is a combination of 3 datasets from various Chinese academics of Chinese roadsigns.  Due to legal limitations within the People's Republic of China, acquiriing and publishing such data is forbidden without certain approvals and licenses.  By leveraging these publically published works done by others in China, such legal problems are avoided and a more complete dataset for traffic sign recognition was built. This dataset contains 50,000 images of 60+ types of Chinese roadsigns extracted from 3+ other traffic sign recognition and detection datasets.

It has been designed to work out-of-the-box with Keras' image_dataset_from_directory and with an associated Pytorch dataloader. This way, the user can focus on the algorithmic implementation. The images vary in size from 5x5 to 300x300. The images are roughly centered, with the sign taking the inner 84% of the image.  However, in some cases, the roadsigns are not centered due to limitations in the underlying dataset.  Those signs which are partially occluded...

All attribution and ownsership is retained to the original publishers. All works derivative from this dataset should follow the standards and rules of the underlying datasets. Below are listed 
