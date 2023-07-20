# <u>Intel Unnati Project - Team TRON</u>

This project was created as part of Intel UNNATI Industrial Training Project. The topic of our project was "Road Object Detection with Deep Learning". <br><p>Our aim was to develop a model that could identify objects specifically in Indian roads. This is because roads in India may be completely different from other countries thus their datasets will not be of much use here. <br>

<p> Procedure to train the model are as follows -

1. Clone | fork this project.

2. Download IDD from http://idd.insaan.iiit.ac.in/ [you will be asked to create an account]. IDD Detection (22.8 GB) is the dataset being used in this case. <br>- Note that *IDD_Detection* directory here does not have *Annotations* and *JPEGImages* folders due to its large size.

3. Extract downloaded dataset and place the dataset into cloned directory. This will replace the already present *IDD_Detection* folder. <br>

4. In your preferred code editor, navigate to the cloned directory and run the following command in the terminal:  `python datasetPreprocessing.py`. This will create a new folder *modified_dataset* which is where dataset is stored in the proper format. This process may take around 20 minutes, depending on your system configuration.

5. Clone [YOLOv5 GitHub repository](http://github.com/ultralytics/yolov5) into your directory. Instructions for installation can be found in the repository. <br> _Optional: Create a virtual environment before running ``pip install -r requirements.txt`` so as to not interfere with any other versions which may be already installed in your system._

6. In *yolov5/data*, create a new file named *idd.yaml* and place the following into the file<br>
   
   ```yaml
   # Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
   path: ../modified_dataset   # dataset root dir
   train: images/train         # train images (relative to 'path') 128 images
   val: images/val             # val images (relative to 'path') 128 images
   test: images/test           # test images (optional)
   nc: 15                      # number of classes
   
   names: ['car', 'bus', 'autorickshaw', 'vehicle fallback', 'truck', 'motorcycle', 'rider', 'person', 'bicycle', 'animal', 'traffic sign', 'train', 'trailer', 'traffic light', 'caravan']
   ```

7. In yolov5/models, there are different models thet can be trained. Choose the one based on requirements. Before using model, confirm that 'nc' i.e., number of classes, is same as in *idd.yaml*.

8. Run the model using the command<br>
   
   ```python
   python train.py --img <image_size> --batch <batch_size> --epochs <num_epochs> --data <data/data.yaml> --cfg <path_to_model_config>
   ```
   
   add '--device cuda:0' if you are using a dedicated GPU (please do check if your [GPU supports CUDA](https://developer.nvidia.com/cuda-gpus)). Also try installing [cuDNN](https://developer.nvidia.com/cudnn), but a *NVIDIA Developer Program Membership* is required <br>
   
   use '--weights <path_to_weights>' if you have pretrained weights <br>
   
   _optionally, you can set the number of workers with --workers <no of workers> but do take note that workers should not exceed the number of cores your CPU has._
   
   For example during the first training, the command was:
   
   ```python
   python train.py --img 640 --batch 8 --epochs 50 --data data/idd.yaml --cfg models/yolov5s.yaml --device cuda:0 --workers 4
   ```

9. In the second run, yolov5m was used along with pretrained weights:
   
   _note: path to best.pt may be different depending upon iteration_
   
   ```python
   python train.py --img 640 --batch 8 --epochs 50 --data data/idd.yaml --cfg models/yolov5m.yaml --device cuda:0 --workers 6 --weights runs/train/exp3/weights/best.pt
   ```

10. Results of each training procedure wil present within yolov5/runs/train/*exp_no* <br>

<br>

<p>Results of training operation will be placed in results folder in main directory of the repository for easier review.

<br><br>
Collaborators: <br>
&nbsp;&nbsp; [@Josh-Alex](https://github.com/JoshAlex12) <br>
&nbsp;&nbsp; [@noel-robert](https://github.com/noel-robert) <br>
&nbsp;&nbsp; [@nubifathima](https://github.com/nubifathima) <br>
