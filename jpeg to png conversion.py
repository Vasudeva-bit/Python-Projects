import pathlib
import sys
from PIL import Image
c=1
sour=sys.argv[1]
des=sys.argv[2]
if not((pathlib.Path(des)).is_dir()):
 pathlib.Path(des).mkdir()
for path in pathlib. Path(sour).iterdir():
if path.is_file() :
img = Image.open(path)
img.save(f'{des}\\fun{str(c)}.png','png')
c+=1