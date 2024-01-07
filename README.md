# Simple Mixer

# THIS IS A DEVELOPMENT BRANCH - DO NOT USE ON SHOWS
Simple Mixer is a real-time and video mixing tool built entirely in TouchDesigner. It's currently tested and working in build 2022.35280.

There's been a lot of one on one conversation regarding SimpleMixer and using it so I've now made a new discord in case anybody wants to discuss in a community manner:
[Join here](https://discord.gg/FubpKXZPBK)


[Watch the explanation video](https://www.youtube.com/watch?v=P8iLnwoWyAI)

[Watch the Post FX update explanation video](https://youtu.be/DhKZlpO24m4)


##### How It Works

Simple Mixer uses four banks at the top left of the screen which can have clips and tox files loaded into them. They can then be mixed between using the sliders and the compositing mode can be set.

Toxs are shown in the panel on the bottom left. These can be loaded by placing the tox file into the Assets/Tox directory.

For a tox to be compatible with Simple Mixer at the bare minimum it must have a TOP operator named 'out1' and another named 'thumb' in order to function. It can also have a text DAT called 'name' which will show up in the Asset Browser. If your tox file is a container or has custom parameters these parameters will be exposed on the bottom right of the display when the tox is loaded into a bank and that bank is selected in the Current Visuals tab. If you want to set your tox files to the correct resolution then you can use the expressions op.output.par.Resolutionw and op.output.par.Resolutionh. To hook audio up to your component it's recommended to expose those parameters via custom parameters and then hook them up via the interface.

For audio analysis the system uses the audioanalysis component created by Greg Hermanovic. This has three different spectrum tabs you can select between and options for analysing particular frequencies. The CHOP itself is exposed ready to be hooked up to custom parameters directly in the interface.

At the very top of the screen is a tab to switch into mapping mode. This has two projection mapping tools. One is the stoner from the Palette and the second is Warpa which is a polygon drawing and warping tool.

##### Changelog

To-do
- Finally switch out the audioanalysis for the new one
- re-arrange the UI to give more space for more functionality
- Loading fixes for toxes and post fx and memory saving stuff
- Remove replicators from toxes and movies provided the postfx update worked well
- presets for toxes and post fx media
- Fix Warpa so it uses the same UIKit as SimpleMixer

###### 1.3.5

Bug Fixes

- Fixed drop down menus for blend modes in new touch builds for the mixer
- Fixed The asset browser thumbnails being too small when using large numbers of toxes/movies.

###### 1.3.4

New Features

- Added Video Device In Tox
- Added Spout In Tox
- Added NDI In Tox
- Added Video Stream In Tox
- Added Webpage In Tox

Bug Fixes

- Fixed broken replicator in movie bin
- Turned off spout out by default

###### 1.3.3

- Fixed the resolution setup so now whatever resolution is set in settings is the final output.
- fixed bug where some post effects had their switch the wrong way around
- Removed some random junk OPs from base_mix
- Externalized Warpa

NOTE: op.output.par.w will give the output screen size. op.output.par.Resolutionw will give the resolution in settings.

###### 1.3.2

New Features

- New mapping control panel to enable/disable stoner
- New mapping tool called Warpa - See the video on how Warpa works here:
(https://www.youtube.com/watch?v=Ig19XN008Yw)


###### 1.3.1

New Features

- Upgraded to TouchDesigner 2022.35280
- replaced gui with text comp version
- added gpu memory usage to top bar
- postfx now get replicated on startup
- toxs, movies, notch blocks and postfx can now be titled and it will show in the media browser. To give a component a title add a text DAT in it called name and type in whatever you want it to say.
- some new postfx's to get people started
- Spout/Syphon output added - see settings
- RMTP output added - see settings
- NDI output added - see settings
- Video device output added - see settings

Bug Fixes

- fixed output dimmer toggle not working
- fixed crash when reloading postfxs
- removed faulty save component - ctrl + alt + s saves all

###### 1.2.1

Bug Fixes
- Fixed replicator re-init not initializing
- Fixed an old replicator COMP backwards compatibility issue with TouchDesigner

###### 1.2.0

Bug Fixes
- SimpleMixer updated to build 2021.14360
- Menu made smaller temporarily to account for a bug with cropping panels in TouchDesigner
- Notch block error fixes
- Replicators now check folders live so the panel can update when tox's added
- Startup errors from example TOXs fixed.

###### 1.1.5

Bug Fixes
- Emulate resolution issue fixed where the height was setting as the width
- Connection issue between base mix and the post fx fixed

###### 1.1.4

New Features
- Removed Learn buttons as they weren't reliable
- Added in a record button to record out a moviefileout. The recording goes into the /Recording folder

Bug Fixes
- Fixed issue where SimpleMixer was running slow due to a dodgy post effect.
- Fixed Central AB Fader referencing the wrong top in the base_mix component somehow.


###### Rich & Dithid - 1.1.3

New Features
- Now post FX can be turned on and off for both left and right fades via the two buttons in the Mixer section. (Thanks Dithid)
- See audio playlist updates below (Thanks Tim)
- Turned audio playlists off by default and reverted to an empty scene for people pulling the first time.

###### Tim - 1.1.2

New Features
- A new tab was added in the grid allowing you to create audio playlists.
- The button to setup test audio was replaced with new page that allows you to configure either single test audio files or playlists.

Known Issues
- if the audio file is shorter than the transition weird things will happen.
- When you make changes to the configuration of the autoMediaPlayer you sometimes need to reset it via the Reset pulse button. You can do this directly from the UI by opening the Music configuration button.

###### 1.1.1

Bug Fixes
- Post FX went very very wonky after the Touch updates due to the way op connectors were changed when reinitializing .tox files. This should now be fixed.

###### 1.1.0

New Features
- Notch Support - Place your blocks in the Assets/Notch folder and they'll become available under the "Notch Blocks" tab.

Bug Fixes
- Post FX Sliders no longer default to 0 on startup.
- TouchDesigner Upgrade broke the OSC mapping, this is now fixed.
- Issue where the parameter window would sometimes not update fixed.

###### 1.0.0

Bug Fixes
- Sliders reverting to 0 should be fixed
- Right clicking on a bank now reverts to the original functionality of setting that bank as the active parameter window.

###### 0.9.8

New Features
- Upgraded the TOX preview pane on the bottom right hand side to show Base COMPs as well as panels.
- The TOX selector grid is now adaptable in size to avoid scrollbars and make everything quickly draggable. (Thanks Dith_Id for that one)

###### 0.9.7

Bug Fixes
- The drag drop bug workaround broke PostFX dragging. You can now drag to Post FX slots again but right clicking is disabled as drag drop is fixed. SimpleMixer now only works in 25850 ONLY.
- Menus now have scrollbars so they don't go off the screen if they are too large.

###### 0.9.3  - BETA

Bug Fixes
- Drag Drop can now be avoided by selecting the TOX/Movie you wish to assign and right clicking the bank you want to assign it to. For PostFX you can simply select a bank and then left click the Post Effect you want to apply to it.
- Movie thumbnails should load properly now (seriousssslllyyy)
- UI error fixes when there are no secondary monitors present.
- Clear All Mappings button in settings now actually clears all mappings rather than just erroring.

Things To Note
- There seems to be an issue with menus loading slowly in some scenarios. This will be addressed in the next version.

###### 0.9.0 - BETA

New Features
- Gal is gone! We now have a completely new UI system that is both scaleable and MIDI/OSC/Key/UDP/Artnet Mappable.
- The new settings tab allows you to specify which inputs you are using and customize the highlight colour.
- Remove mappings in Settings by clicking the "Clear All Mappings" button.
- Halfway to the 1.0.0 release in which I hope to rebuild the Parameter COMP into a fully mappable system. For now you can use the container setup to map things in.

Notes
- Would really love it if people could report issues as I imagine there will be quite a few with this build.

###### 0.5.0

New Features
- You can now change the levels and hue parameters directly on movie clips.

Bug Fixes
- Second pre-viz window was broken on last update. This should now be fixed. You can now properly drag the line between the two to resize them.
- Movie thumbnails should now load properly.

###### 0.4.8

New Features
- added in a second pre-viz window. You can now choose between the four visuals in the banks and output. To make the window on the left or right bigger drag the border between the two.
- Cube matrix now has a colour offset parameter.
- New cloth TOX.
- Upgraded to latest version of gal.
- Right clicking on a bank will now auto switch the Current Visuals parameter window to that particular bank.
- Clicking on the previz window whilst viewing a particular bank will now switch the Current Visuals parameter window to that particular bank.
- Save Button.

Bug Fixes
- fixed re-initialization issue on toxs.


###### 0.4.0

- New Post Effects. Feedback Effect and Tile Effect Added.
- New Box Matrix TOX.

###### 0.3.7

- Upgraded to TouchDesigner build 22800.
- BPM + - buttons for adjustment.
- Clicking the bpm indicator now sets the system timeline to frame 1.
- bpm_pulse channel added into audioanalysis component.
- Post Effects will now fade in and out rather than snapping.
- Post Effects now have opacity sliders. This allows preparing a post effect before sending it to the main output.

###### 0.3.6

- If there is no second monitor SimpleMixer will now use /simplemixer/container_outputs "Emulate Output Resolution" parameter.
- Externalised container_output.

###### 0.3.5

- Updated to Experimental 21670
- Always on top bug has been fixed in TouchDesigner so is re-enabled in SimpleMixer
- Tested on TouchScreen. All functionality is working but certain buttons could be bigger.

###### 0.3.4

- Updated to Experimental 21150
- Opening the Post FX browser auto-switches the effect editor to Post FX Mode and vice versa.
- Dropping a Post Effect onto a TOX bank will no longer load it into the bank by mistake.
- Dropping a TOX onto a Post FX slot will no longer break the system.
- Removed random "hi" print from base_mix
