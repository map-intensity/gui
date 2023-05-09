import yaml
import subprocess

with open('data.yml', 'r') as f:
    data = yaml.safe_load(f)

class_id = data['class_id']
image_size = data['image_size']
input_dir = data['input_dir']
output_dir = data['output_dir']
yolo_dir = data['yolo_dir']

command = f"python detect.py --weights {yolo_dir} --conf 0.25 --img-size {image_size} --source {input_dir} --class {class_id} --save-txt --project {output_dir}"

subprocess.run(command, shell=True)
