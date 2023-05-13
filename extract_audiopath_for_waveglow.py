path = "~/jhl/deepvoice/multi-Speaker-tacotron-tensorflow/datasets/kss/audio/"

with open("splitted_kss.txt", "r", encoding="UTF-8") as f:
	lines = f.readlines()

new_lines = []	
for line in lines:
	parts = line.strip().split('|')
	extracted = parts[0]
	# new_line = f"{parts[0]}|{extracted}\n"
	new_lines.append(path + extracted + '\n')

with open('kss_train_waveglow.txt', 'w') as f:
	f.writelines(new_lines)