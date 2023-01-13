from src.parser import parsed_translations
from pprint import pprint
from time import time

from tqdm import tqdm

def main():
    pb = tqdm(unit=" lines", colour="pink", unit_scale=True)
    file_count = 0
    for p in parsed_translations('paralleltext-master/bibles/corpus/'):
        file_count += 1
        pb.update(len(p["data"]["lines"]))
        if file_count % 25 == 0: pb.set_postfix({'Files': file_count})
    
if __name__ == '__main__':
    b_t = time()
    main()
    print(f"It took {round(time() - b_t, 2)}s")