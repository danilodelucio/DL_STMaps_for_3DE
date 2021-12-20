# DL_STMaps_for_3DE
Creates STMaps for 3DEqualizer.

You must run this app in the same local of your 3DE.exe ("bin" folder).
The following files are required for this app to work fine:

- create_identity_uv_map.exe
- exr_channel_to_text.exe
- libgcc_s_sjlj-1.dll
- pthreadGC2-w64.dll

![Screenshot 2021-12-18 214036](https://user-images.githubusercontent.com/47226196/146659457-69b43f9c-523a-48be-b7df-8e5930dfa0f5.png)
![Screenshot 2021-12-18 214219](https://user-images.githubusercontent.com/47226196/146659474-a02d44aa-c434-4729-bce1-781a5e4d0937.png)
![Screenshot 2021-12-18 214456](https://user-images.githubusercontent.com/47226196/146659475-707f7393-a9d9-4f20-a9bd-47a289ab07cf.png)

# Manual Process (how it was)

Before creating this app, we had to run the CMD and execute the following steps:

1-) Accesing the "bin" directory from 3DEqualizer in your computer.

![Screenshot 2021-12-20 132300](https://user-images.githubusercontent.com/47226196/146799577-c9274fc5-fa17-4726-af03-969a17773512.png)

<i>Note: The ">" symbol is a prefix that I've set up for my own CMD, you can't use it.</i>

2-) Having the files required as said before, you use this command below replacing the infos properly.

![Screenshot 2021-12-20 133741](https://user-images.githubusercontent.com/47226196/146801367-653ce8fe-7346-4f4d-9b8d-f55e6007e653.png)

<i>Note: You must use your custom resolution as a string (inside apostrophes), and space key to separate the values.</i>

Your first STMap should be created.

![Screenshot 2021-12-20 134235](https://user-images.githubusercontent.com/47226196/146802027-65245bc3-d28d-4d96-a231-33e8d6e78426.png)

3-) Now, you will need to repeat the same process, but using the custom resolution with an overscan applied.

To find out the overscan value, you just need to calculate: (percentage_value * resolution) / 100 + resolution = overscan_value

![Screenshot 2021-12-20 140538](https://user-images.githubusercontent.com/47226196/146805051-8110890b-13e5-4b24-9889-4f77ff871023.png)

<i>Note: In this example, I've calculated the overscan for Full HD resolution, so you need to calculate the percentage value for width and height size separately.</i>

Then here we go.

![Screenshot 2021-12-20 141643](https://user-images.githubusercontent.com/47226196/146806425-cc0670ea-cbf2-4907-873e-7acb4f3c7abb.png)

# Finally

So this is the deal: to help create both STMaps without using CMD and calculate the overscan manually, with everything working in a simple and humble GUI.

I hope you enjoy it, thanks in advance!

<b>Danilo de Lucio</b>
