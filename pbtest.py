import os
from tqdm import tqdm
import json
import Diffractor
# import nltk
# nltk.download('punkt_tab')

eps = 0.1
L = Diffractor.Lists(home='./embeddings')
D = Diffractor.Diffractor(L=L, epsilon=eps)

print('Rewriting text...')
DATA_DIR = "/home/ykwy/EnochPB/USPB/ForUsers/qOnly"
OUTPUT_DIR = f"./output/epsilon-{eps}"
dir_list = os.listdir(DATA_DIR)

for file_name in tqdm(dir_list):
    data_file = os.path.join(DATA_DIR, file_name)
    file_idx = file_name.split(".")[0]
    out_file = os.path.join(OUTPUT_DIR, file_idx + ".json")
    with open(data_file, 'r') as rf:
        queries = json.load(rf)
    private_texts = D.rewrite(queries)
    # print(private_texts[0])
    with open(out_file, 'w') as wf:
        json.dump(private_texts[0], wf)
