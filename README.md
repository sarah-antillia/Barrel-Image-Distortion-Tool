<h2> Barrel-Image-Distortion-Tool (2024/06/18)</h2>

<br>
<a href="#1">1, Seeing Is Believing</a><br>
<a href="#2">2, Run BarrelImageDistorter</a><br>
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

<b>BarrelImageDistorterDemo</b><br>
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

<b>Input image</b><br>
<table>
<tr>
<td>
<img src="./meshed_images/MeshedPicture.png" width="320" height="auto">
</td>
</tr>
</table>
<br>
<b>Barrel distorted images</b><br>
The yellow circles in the following images indicate the center of the barrel distortion.<br>
In the configration file above, there are three centers define. <br>
<pre>
centers    = [(0.3, 0.3), (0.5, 0.5), (0.7, 0.7)]
</pre>
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
MeshedPicture <br>
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

