# Intel Unnati Project - Team TRON</u>

#### under development

This project was created as part of Intel UNNATI Industrial Training Project. The topic of our project was "Road Object Detection with Deep Learning". <br>Our aim was to develop a model that 

1. Clone | fork this project.
2. Download IDD from http://idd.insaan.iiit.ac.in/ [you will be asked to create an account]. IDD Detection (22.8 GB) is the dataset being used in this case. <br>- Note that *IDD_Detection* directory here does not have *Annotations* and *JPEGImages* folders due to their size.
3. Extract downloaded dataset and place the dataset into cloned directory. This will replace the already present *IDD_Detection* folder. <br>
4. In your preferred code editor, navigate to the cloned directory and run the following command in the terminal:  `python datasetPreprocessing.py`. This will create a new folder *modified_dataset* which is where dataset is stored in the proper format. This process may take around 20 minutes, depending on your system configuration.
5. Clone [YOLOv5 GitHub repository](http://github.com/ultralytics/yolov5) into your directory. Instructions for installation can be found in the repository. <br> _Optional: Create a virtual environment before running ``pip install -r requirements.txt`` so as to not interfere with any other versions which may be already installed in your system._
6. 
