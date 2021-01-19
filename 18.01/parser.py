import json
import yaml


def json_to_text_parser(json_file, text_file):
	with open(json_file, 'r') as js_file:
		data = json.load(js_file)
	
	with open(text_file, 'w') as txt_file:
		txt_file.write(str(data))


def text_to_json_parser(text_file, json_file):
	with open(text_file, 'r') as txt_file:
		data = txt_file.read()

	with open(json_file, 'w') as js_file:
		json.dump(data, js_file, indent=4)	


def json_to_yaml_parser(json_file, yaml_file):
	with open(json_file, 'r') as js_file:
		data = str(json.load(js_file))
	
	with open(yaml_file, 'w') as yml_file:
		yaml.dump(data, yml_file, indent=4)	

def yaml_to_json_parser(yaml_file, json_file):
	with open(yaml_file, 'r') as yml_file:
		data = yaml.load(yml_file)

	with open(json_file, 'w') as js_file:
		json.dump(data, js_file, indent=4)	



