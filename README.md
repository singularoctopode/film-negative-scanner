# film-negative-scanner
Simply takes an image of a film negative and applies a few tweaks to get a positive colour image. Disclaimer: this project is very far from completion and its features are very limited. This is more of a personal archive for myself; a sandbox for me to play around with the charming antiquities of film photography. 

![comparisonImage](/images/comparison.png)
The above image is courtesy of John Alan Elson as shared under the Creative Commons Attribution-Share Alike 4.0 International license and is hosted [here](https://commons.wikimedia.org/wiki/File:Nimslostripneg.jpg) by Wikimedia Commons.

## How it works
The image white balance first needs to be adjusted to account for the orange backing of the film; the white point is set to the colour value of the unexposed film. We need to find out the multiple by which to scale the individual R, G, and B channels in order to acheive white (255, 255, 255). This can be found by dividing 255 by each channel value and multiplying all image pixels by these values. Succinctly, we use the equation below:

$$
\begin{bmatrix}
R\\
G\\
B
\end{bmatrix} = \begin{bmatrix} 
255/{R'}_w & 0 & 0\\
0 & 255/{G'}_w & 0\\
0 & 0 & 255/{B'}_w
\end{bmatrix} \begin{bmatrix}
R'\\
G'\\
B'
\end{bmatrix}
$$

($R,G,B$) are the new pixel values, ($R',G',B'$) are the origional pixel values, and (${R'}_w, {G'}_w, {B'}_w$) are the sample values (for a pixel which should ideally be white). 
The next thing to do is simply invert the image. This simply requires subtracting each channel value from its maximum value: 
$$(R,G,B) \rightarrow (255-R, 255-G, 255-B)$$

I've found that after doing this, images take on a blueish hue and further fiddling in photoshop is required to bring out the warmer tones, up the saturation, and improve the contrast. As hinted at below, these are features I intend to impliment, alongside a method to sample the white point. 

## Features to add
- [ ] auto colour/tone
- [ ] gamma correction
- [ ] auto contrast
