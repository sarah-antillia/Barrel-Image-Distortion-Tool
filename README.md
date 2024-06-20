<h2> Barrel-Image-Distortion-Tool (Updated: 2024/06/20)</h2>

<br>
<a href="#1">1. Seeing Is Believing</a><br>
<a href="#2">2. Run BarrelImageDistorter</a><br>
<a href="#3">3. ImageMaskAugmentor </a><br>

<br>
This is a simple python class <a href="./BarrelImageDistorter.py">BarrelImageDistorter</a> to distort an image by using 
OpenCV remap.
This is based on the code in the following stackoverflow web-site.<br>
<br>
https://stackoverflow.com/questions/59776772/python-opencv-how-to-apply-radial-barrel-distortion
<br>
<br>
This ImageDistorter runs on Python 3.8 or later version. Please install opencv-python to your Python development enviroment.<br>  
This tool can be used to augment the image and mask files to train an image segmentation model.
<br>
<h3> 
<a id="1">1. Seeing Is Believing</a>
</h3>
<b>Input image</b><br>
<table>
<tr>
<td>
<img src="./meshed_images/MeshedPicture.png" width="320" height="auto">
</td>
</tr>
</table>

<h3>1.1 Barrel Distortion</h3>
Please run the following command with a configuration file <b>demo_distortion.config</b>.<br>
<pre>
>python BarrelImageDistorterDemo.py ./demo_distortion.config
</pre>
, where demo_distortion.config file is the following.<br>
<pre>
; demo_distortion.config
; 2024/06/18 (C) antillia.com

[barrdistortion]
radius     = 0.3
amount     = 0.3
centers    = [(0.3, 0.3), (0.5, 0.5), (0.7, 0.7)]
images_dir ="./meshed_images"
output_dir ="./distorted_meshed_images"
</pre>

<br>
<b>Barrel distorted images</b><br>
The yellow circles in the following images indicate the center of the barrel distortion.<br>
In the configration file above, there are three centers defined, and three distorted images will be
generated by this BarrelImageDistorter as shown below.<br>
<pre>
centers    = [(0.3, 0.3), (0.5, 0.5), (0.7, 0.7)]
</pre>
<b>Barrel distortion</b><br>
<table>
<tr>
<td>
<img src="./distorted_meshed_images/101_0.3_0.3_MeshedPicture.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_meshed_images/102_0.3_0.3_MeshedPicture.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_meshed_images/103_0.3_0.3_MeshedPicture.png" width="320" height="auto">
</td>
</tr>
</table>

<br>
<h3>1.2 Pincushion Distortion </h3>
If you would like try a pincushion distortion, please run the following command.<br>
<pre>
>python BarrelImageDistorterDemo.py ./demo_distortion2.config
</pre>
, where demo_distortion2.config file is the following.<br>
<pre>
; demo_distortion2.config
; 2024/06/18 (C) antillia.com

[barrdistortion]
radius     = 0.3
; Specify negative amount to produce pincushion distortion
amount     = -0.3
centers    = [(0.3, 0.3), (0.5, 0.5), (0.7, 0.7)]
images_dir ="./meshed_images"
output_dir ="./distorted_meshed_images2"
</pre>
<b>Pincushion distorted images</b><br>
<table>
<tr>
<td>
<img src="./distorted_meshed_images2/101_0.3_-0.3_MeshedPicture.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_meshed_images2/102_0.3_-0.3_MeshedPicture.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_meshed_images2/103_0.3_-0.3_MeshedPicture.png" width="320" height="auto">
</td>
</tr>
</table>

<br>


<h3>
<a id="2">2. Run BarrelImageDistorter</a>
</h3> 
To run ImageDistorter, please specify a <i>distortion.config</i> as a command-line parameter as shown below.
<pre>
>python BarrelImageDistorter distortion.config
</pre>
, where distortion.config file is the following.<br>
<pre>
; distortion.config
; 2024/06/18 (C) antillia.com

[barrdistortion]
radius     = 0.3
amount     = 0.3
centers    = [(0.3, 0.3), (0.5, 0.5), (0.7, 0.7)]
images_dir ="./images"
output_dir ="./distorted_images"
</pre>

By running the command above, each image in images_dir will be read, distorted by the parameters in [distortion] section, and
saved to output_dir.<br>

<br>
<b>Input images</b> <br>
<img src="./asset/Images_sample.png" width="1024" height="auto"><br>
<br>
<b>Distorted images</b><br>
<img src="./asset/distorted_images.png" width="1024" height="auto"><br>

<br>
<b>Enlarged sample images</b><br>
coca-cola <br>
<table>
<tr>
<td>
<img src="./distorted_images/barrdistorted_101_0.3_0.3_coco-cola.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_102_0.3_0.3_coco-cola.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_103_0.3_0.3_coco-cola.png" width="320" height="auto">
</td>
</tr>
</table>
<br>
cranes <br>
<table>
<tr>
<td>
<img src="./distorted_images/barrdistorted_101_0.3_0.3_cranes.jpg" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_102_0.3_0.3_cranes.jpg" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_103_0.3_0.3_cranes.jpg" width="320" height="auto">
</td>
</tr>
</table>
<br>

koban <br>
<table>
<tr>
<td>
<img src="./distorted_images/barrdistorted_101_0.3_0.3_koban.jpg" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_102_0.3_0.3_koban.jpg" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_103_0.3_0.3_koban.jpg" width="320" height="auto">
</td>
</tr>
</table>
<br>

MeshedNioh <br>
<table>
<tr>
<td>
<img src="./distorted_images/barrdistorted_101_0.3_0.3_MeshedNioh.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_102_0.3_0.3_MeshedNioh.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_103_0.3_0.3_MeshedNioh.png" width="320" height="auto">
</td>
</tr>
</table>
<br>
picture <br>
<table>
<tr>
<td>
<img src="./distorted_images/barrdistorted_101_0.3_0.3_picture.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_102_0.3_0.3_picture.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_103_0.3_0.3_picture.png" width="320" height="auto">
</td>
</tr>
</table>

<br>
road_signs <br>
<table>
<tr>
<td>
<img src="./distorted_images/barrdistorted_101_0.3_0.3_road_signs.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_102_0.3_0.3_road_signs.png" width="320" height="auto">
</td>
<td>
<img src="./distorted_images/barrdistorted_103_0.3_0.3_road_signs.png" width="320" height="auto">
</td>
</tr>
</table>

<h3>
<a id="3">3. ImageMaskAugmentoe</a>
</h3> 
By using the barrel image distortion algorithm, we created a tiny offline <a href="ImageMaskAugmentor.py">ImageMaskAugmentor Tool.</a>.
 
To run the augmentation tool, please specify a <i>augmentor.config</i> as a command-line parameter as shown below.
<pre>
>python ImageMaskAugmentor.py augmentor.config
</pre>
, where augmentor.config file is the following.<br>
<pre>
; augmentor.config
; 2024/06/20 (C) antillia.com

[augmentor]
images_dir = "./BCSS-Breast-Cancer-mini-dataset/images/"
masks_dir  = "./BCSS-Breast-Cancer-mini-dataset/masks/"
output_dir = "./Augmented-BCSS-Breast-Cancer-mini-dataset/"
      
radius     = 0.3
amount     = 0.5
centers    = [(0.3, 0.3), (0.5, 0.5), (0.7, 0.7)]
</pre>
The original images files in "./BCSS-Breast-Cancer-mini-dataset/images/" and mask files in "./BCSS-Breast-Cancer-mini-dataset/masks/"
have been taken from <a href="https://github.com/PathologyDataScience/BCSS">
<b>Breast Cancer Semantic Segmentation (BCSS) dataset.</b>
 </a>
<br>
On that dataset, please see aslo our github repository <a href="https://github.com/sarah-antillia/Tiled-ImageMask-Dataset-Breast-Cancer">Tiled-ImageMask-Dataset-Breast-Cancer</a>.
<br>
<hr>
<b>Input images</b> <br>
<img src="./asset/bcc_images.png" width="1024" height="auto"><br>
<br>
<b>Input mask</b><br>
<img src="./asset/bcc_masks.png" width="1024" height="auto"><br>
<hr>
<br>
<b>Augmented images</b><br>
<img src="./asset/bcc_augmented_images.png"  width="1024" height="auto"><br>
<br>
<b>Augmented masks</b><br>
<img src="./asset/bcc_augmented_masks.png"  width="1024" height="auto"><br>
<br>
<hr>

<h3> Dataset Citation</h3>
The original dataset used here has been taken from the following github repository.<br>

<a href="https://github.com/PathologyDataScience/BCSS">
Breast Cancer Semantic Segmentation (BCSS) dataset
</a>
<br>
<br>
On detail of this dataset, please refer to the following paper.<br>

<a href="https://academic.oup.com/bioinformatics/article/35/18/3461/5307750?login=false">
<br>

<b>Structured crowdsourcing enables convolutional segmentation of histology images</b><br>
</a> 
Bioinformatics, Volume 35, Issue 18, September 2019, Pages 3461–3467, <br>
https://doi.org/10.1093/bioinformatics/btz083<br>
Published: 06 February 2019<br>

Mohamed Amgad, Habiba Elfandy, Hagar Hussein, Lamees A Atteya, Mai A T Elsebaie, Lamia S Abo Elnasr,<br> 
Rokia A Sakr, Hazem S E Salem, Ahmed F Ismail, Anas M Saad, Joumana Ahmed, Maha A T Elsebaie, <br>
Mustafijur Rahman, Inas A Ruhban, Nada M Elgazar, Yahya Alagha, Mohamed H Osman, Ahmed M Alhusseiny,<br> 
Mariam M Khalaf, Abo-Alela F Younes, Ali Abdulkarim, Duaa M Younes, Ahmed M Gadallah, Ahmad M Elkashash,<br> 
Salma Y Fala, Basma M Zaki, Jonathan Beezley, Deepak R Chittajallu, David Manthey, 
David A Gutman, Lee A D Cooper<br>

<br>
<b>Dataset Licensing</b><br>
This dataset itself is licensed under a CC0 1.0 Universal (CC0 1.0) license. 

<br>
