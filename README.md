# datapack-updater
<b>This python tool allows automatic conversion of Minecraft 1.16 data packs to 1.17.</b><br><br>
To update a 1.16 data pack to 1.17 enter the console command ```python dp_up.py <data pack path>```.<br><br>
To downgrade a 1.17 data pack to 1.16 enter ```python dp_up.py -back <data pack path>```<br><br>
To get help enter ```python dp_up.py -help```



It will update the ```pack_format``` in the pack.mcmeta and update all ```replaceitem``` commands to ```item [...] replace``` in the function files. 
