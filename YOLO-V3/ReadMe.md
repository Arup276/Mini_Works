# What is YOLO-V3?
YOLO ,or You Only Look Once is a object detion algoritham. iT's the most accurate real time object detection algorithm.
If want to more about YOLO-V3 then you check [here](https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b).



 So recently i was playing with yolo-v3 (i was also do little bit yolo-v2) and since now a days PUBG moblie is very famous to i tried this yolo on pubg.Though i don't get high accuracy but it's ok because i was trained this model just around 300 hundred of images(i was too much excited about that) but now i know little about the procedure so again i will do with more images.

This madole is trained on 4 classes : car,Medicine,Weapon,Enwmies.

# This is my model demo([Video demo](https://www.youtube.com/watch?v=hIV3EJVeiA4&t=9s))

![car](https://user-images.githubusercontent.com/32811517/52165274-782c8400-2724-11e9-8df5-82a879d7ca96.PNG)

#### If you want to use my model then follow the steps ,i make it very simple because i was (still) very complicated for me so i try to break is down. Here Extra you have nothing to do extra.So jump right into it...



# How You Can Use My model?

# Step-1: 
### Download:
###         case-1:
Download the zip of [this](https://github.com/Arup276/Mini_Works/edit/master/YOLO-V3) repo and extract it.
And notice that after dowload file format should be this 

![format](https://user-images.githubusercontent.com/32811517/52165263-4d423000-2724-11e9-8f00-62dd00d120af.PNG)
## In this case after extracting you will see a ```bin``` folder you have to go their  `D:\YOLO-V3\bin` this ``` bin``` folder and extract the zip file(to get the full weights).
![weight_ext](https://user-images.githubusercontent.com/32811517/52165373-1a993700-2726-11e9-830b-995642347e58.PNG)
(like shown in image just extract that)

### Case-2:
Or you can download all the file from my google drive [here](https://drive.google.com/drive/u/3/folders/1JWjKtp9UXEFNrJBBVZKEG3_UOhRRTyrj)

Now if think that so why i upload this file file on github ? simple answer is Just for looks good😂.

Ok so next move on to step-2. 


# step-2:

### Download OpenCV from [here](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/3.3.0/opencv-3.3.0-vc14.exe/download)
### automatically downlaod will start .
now guys here little thing to do
# 1.
Go to ```C:\``` if you see any version of openCV then remane it to some thing else or delete it (easy one😁).
# 2.
then extract the downloaded OpenCV in ```C:/``` like this below image![opencv_ext](https://user-images.githubusercontent.com/32811517/52165569-90060700-2728-11e9-95df-a6ac8ecbf52f.PNG)
# 3.
After extracting if openCV has name some thing else rather than this imagen one ,then just rename and make it this below image one and the path of open should be this : ```C:\opencv_3.0\opencv``` .


![opencv](https://user-images.githubusercontent.com/32811517/52165602-ef641700-2728-11e9-9699-22e945a44a9e.PNG)

# Step-3:
Open ```cmd``` under YOLO-V3 folder and run this command :```darknet_no_gpu.exe detect cfg/yolov3_tiny_pubg.cfg bin/yolov3_tiny_pubg_2000.weights data/pubgcar.jpg```
if you follow the above steps then it should work and it will pop up a predicted image.
Congrats you successfully run YOLO-V3.

# Explaination of this code:
```darknet_no_gpu.exe```: Running darknet no GPU version.
```detect```: This command is for process images for video code is ```demo``` we will do it later.
```cfg/yolov3_tiny_pubg.cfg ```: Path of ```cfg``` file.
```bin/yolov3_tiny_pubg_2000.weights```: Path of weights.
```data/pubgcar.jpg```: path of the image.

enjoy feel free to try your own images.


