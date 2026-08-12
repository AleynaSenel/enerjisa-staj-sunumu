import os
import shutil

src_dir = r"c:\Users\Aleyna\Desktop\toroslar-tanitim\pptx_extracted\ppt\media"
dst_dir = r"c:\Users\Aleyna\Desktop\toroslar-tanitim\team_photos"

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

mapping = {
    "image5.jpeg": "aydanur.jpeg",
    "image7.jpeg": "gokalp.jpeg",
    "image12.jpeg": "yasemin.jpeg",
    "image6.jpeg": "ozgur.jpeg",
    "image11.jpeg": "aleyna.jpeg",
    "image8.png": "zeliha.png",
    "image9.jpeg": "selin.jpeg",
    "image10.jpeg": "arzu.jpeg",
}

for src_name, dst_name in mapping.items():
    src = os.path.join(src_dir, src_name)
    dst = os.path.join(dst_dir, dst_name)
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"Copied {src_name} to {dst_name}")
    else:
        print(f"Missing {src_name}")
