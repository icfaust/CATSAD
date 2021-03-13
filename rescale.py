import numpy as np
import os
from PIL import Image

def rescale(size=32, outfolder='data', images=200):

    loc = '.'

    if size > 100:
        raise ValueError

    if os.name == 'nt':
        s = '\\'
    else:
        s = '/'

    info = np.loadtxt(loc+s+'documentation'+s+'CATSADv2groundtruth.txt', dtype=str)
    
    categories = np.unique(info[:,1])
    
    #remove other categories from master list
    for i in ['io','po','wo']:
        categories = np.delete(categories, np.where(categories == i)[0])

    #find total numbers for every category
    histdata = np.zeros(categories.shape, dtype=int)
    for i in range(len(categories)):
        histdata[i] = np.sum((info[:,1] == categories[i]).astype(int))

    #reduce categories and histdata to those with sufficient numbers of images
    idx = np.where(histdata > images)[0]
    categories = categories[idx]
    histdata = histdata[idx]

    try:
     	os.makedirs(outfolder)
    except FileExistsError:
	#already exists	
	pass

    for i in categories:
    
        #create folders
        os.makedirs(outfolder+s+i)

        #resize and place images
        idx2 = np.where(info[:,1] == i)
        print(i)
        for j in info[idx2][:,0]:
            img = Image.open(loc+s+'raw'+s+i+s+j)
            img = img.resize((size,size))
            img.save(outfolder+s+i+s+j)

    return categories, histdata
