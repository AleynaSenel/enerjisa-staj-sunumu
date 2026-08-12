import os
import win32com.client

ppt_file = r"c:\Users\Aleyna\Desktop\toroslar-tanitim\Enerjisa_Sunum spark 2026 (2).pptx"
out_dir = r"c:\Users\Aleyna\Desktop\toroslar-tanitim\slides"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

try:
    powerpoint = win32com.client.Dispatch("Powerpoint.Application")
    presentation = powerpoint.Presentations.Open(ppt_file, WithWindow=False)

    for i, slide in enumerate(presentation.Slides):
        image_path = os.path.join(out_dir, f"slide_{i+1}.png")
        slide.Export(image_path, "PNG")

    presentation.Close()
    powerpoint.Quit()
    print("Export complete")
except Exception as e:
    print("Error:", e)
