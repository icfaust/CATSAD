The documentation in this folder links the images contained in CATSAD to their original datasets. This traceability is provided for the purpose of showing compliance with all rules and regulations of the People’s Republic of China. CATSAD does not contain materially modified or enhanced images, and the dataset images are only extracted sub-images from the publicly-available originals. In some cases rotations of the images were made. As such, all ownership and legal liability of the individual images are retained by the various original authors.

The prescribed sign ground truth locations from the original datasets have been corrected for errors and brought to similar qualitative standards. Additional signs have also been added which were overlooked in their originals. However, these improvements do not signify that CATSAD is perfect or complete and any errors are up to the user to report and correct. Updates to the dataset may occur at any time, but any future changes will be documented. The source location of each image in CATSAD from each dataset has been given in format particular to the underlying dataset. This information is stored in dataset*groundtruth.txt .  A guide to parsing each of these files is given in a list below.

The sign type categories follow the convention used in the 100k Tsinghua-Tencent dataset and can be referenced from their website under dataset 0. Corrections have also been made from the original classifications. Some images do not fall under any category, and are stored under the ‘other’ folder.  The sign types have expanded to contain certain common signs that are not listed in the original convention. Any use, reproduction, or derivative work dependent on CATSAD should reference each of the 7 following datasets listed below.


0. Tencent Tsinghua 100k dataset
**CVPR 2016 Traffic-Sign Detection and classification in the wild** https://cg.cs.tsinghua.edu.cn/traffic-sign/

  - image name format: 00 + 5 digit image number + 3 digit number of sign in image 
  - ground truth file format: original image name; xmin; ymin; xmax; ymax

1. Traffic Sign Recognition Database
Beijing Jiaotong University, LinLin Huang http://www.nlpr.ia.ac.cn/pal/trafficdata/recognition.html

  - image name format: 10 + 8 digit number in corresponding to the order of the ground truth file
  - ground truth file format: original image name; xmin; ymin; xmax; ymax

2. CCTSDB, CSUST China Traffic Sign Database
**A Real-time Chinese Traffic Sign Detection Algorithm** https://github.com/csust7zhangjm/CCTSDB

  - image name format: 11 + 5 digit number in corresponding to the order of the ground truth file + 3 digit number of sign in image
  - ground truth file format: original image name; xmin; ymin; xmax; ymax

3. Traffic Sign Detection Database
Beijing Jiaotong University, LinLin Huang http://www.nlpr.ia.ac.cn/pal/trafficdata/detection.html

  - image name format: 10 + 1 + 4 digit number corresponding to the order of the ground truth file + 3 digit number of sign in image
  - ground truth file format: original image name; xmin; ymin; xmax; ymax

4. 2015 China fuzzy image processing competition 交通标识图像增强挑战赛初赛
NSFC / Xi’an Jiaotong University http://ccvai.xjtu.edu.cn/ http://pan.baidu.com/s/1jG3upoU

  - image name format: 12 + 3 digit video number + 2 digit frame number + 3 digit number of sign in image
  - ground truth file format: original video number; original frame number; xmin; ymin; xmax; ymax

5. 2015 China traffics sign degradation video training set 交通标识退化视频训练集
NSFC / Xi’an Jiaotong University http://ccvai.xjtu.edu.cn/ http://pan.baidu.com/s/1jG3upoU

  - image name format: 12 + 3 digit video number + 2 digit frame number + 3 digit number of sign in image
  - ground truth file format: original video number; original frame number; xmin; ymin; xmax; ymax

6. TrafficSignData_Norm
Vision and Cognition Lab (VCL), Department of printing and packaging, Wuhan University https://github.com/jizhongxun12306/TrafficSignData_Norm

  - image name format: 13 + 2 digit data set sign number + 3 digit image number + 3 digit sign number in image
  - ground truth file format: original folder number; original image number; xmin; ymin; xmax; ymax

7. SODA10M Dataset
**SODA10M: A Large-Scale 2D Self/Semi-Supervised Object Detection Dataset for Autonomous Driving** Noah's Ark Lab, Huawei Technologies https://soda-2d.github.io/

  - image name format: 14 + 0 for train, 1 for val, 2 for test + 5 digit data set image number + 2 digit sign number in image
  - ground truth file format: original image name; xmin; ymin; xmax; ymax
