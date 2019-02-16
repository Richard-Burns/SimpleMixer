# Mara Lite
Mara Lite is SimpleMixer with some of my main media server bells and whistles added in. SimpleMixer is for single output use whereas Mara Lite is for bringing in projection mapped sets, previsualization, projection mapping and feed mapping.

[Watch the SimpleMixer explanation video](https://www.youtube.com/watch?v=P8iLnwoWyAI)

[Watch the SimpleMixer Post FX update explanation video](https://youtu.be/DhKZlpO24m4)


##### How It Works

Mara uses four banks at the top left of the screen which can have clips and tox files loaded into them. They can then be mixed between using the sliders and the compositing mode can be set.

Toxs are shown in the panel on the bottom left. These can be loaded by placing the tox file into the Assets/Tox directory.

For a tox to be compatible with Simple Mixer at the bare minimum it must have a TOP operator named 'out1' and another named 'thumb' in order to function. If your tox file is a container or has custom parameters these parameters will be exposed on the bottom right of the display when the tox is loaded into a bank and that bank is selected in the Current Visuals tab. If you want to set your tox files to the correct resolution then you can use the expressions op.output.par.w and op.output.par.h. To hook audio up to your component it's recommended to expose those parameters via custom parameters and then hook them up via the interface.

For audio analysis the system uses the audioanalysis component created by Greg Hermanovic. This has three different spectrum tabs you can select between and options for analysing particular frequencies. The CHOP itself is exposed ready to be hooked up to custom parameters directly in the interface.

At the very top of the screen is a tab to switch into mapping mode. Currently this is the standard TouchDesigner stoner however it will likely soon be replaced by a Resolume style poly drawing and warping system. You can also choose an output monitor and toggle the output on and off.

##### Changelog

###### 0.0.1