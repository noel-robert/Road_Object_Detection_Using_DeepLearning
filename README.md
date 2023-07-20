##### *status: porting to YOLOv8*

# <u>Road Object Detection using Deep Learning</u>

This project was created as part of Intel UNNATI Industrial Training Project. The topic of our project was "Road Object Detection with Deep Learning". <br><p>Our aim was to develop a model that could identify objects specifically in Indian roads. This is because roads in India may be completely different from other countries thus their datasets will not be of much use here. <br>

<p> Procedure to train the model are as follows -

1. Clone | fork this project.

2. Create a virtual environment named *yolo-virtualenv* using the following command `python -m venv yolo-virtualenv`. Activate it using `yolo-virtualenv\Scripts\activate`.

3. Download IDD from http://idd.insaan.iiit.ac.in/ [you will be asked to create an account]. *IDD Detection(22.8 GB)* is the dataset being used in this case. <br>- Note that *IDD_Detection* directory here does not have *Annotations* and *JPEGImages* folders due to its large size.

4. Extract downloaded dataset and place the dataset into cloned directory. This will replace the already present *IDD_Detection* folder. <br>

5. In your preferred code editor, navigate to the cloned directory and run the following command in the terminal:  `python datasetPreprocessing.py`. This will create a new folder ***modified_dataset*** which is where dataset is stored in the proper format. This process may take around *15 minutes*, depending on your system configuration.

6. Download CUDA from ??. Optionally, cuDDN can be obtained from ??. 

7. Download and install [PyTorch](https://pytorch.org/get-started/locally/) depending on your system configuration.

8. To download YOLOv8, run the following command 
   Collaborators: <br>
   &nbsp;&nbsp; [@Josh-Alex](https://github.com/JoshAlex12) <br>
   &nbsp;&nbsp; [@noel-robert](https://github.com/noel-robert) <br>
   &nbsp;&nbsp; [@nubifathima](https://github.com/nubifathima) <br>
