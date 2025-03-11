import pathlib
import sys

SPARED_PATH = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(SPARED_PATH))
import datasets

data = datasets.get_dataset("10xgenomic_mouse_brain_sagittal_posterior", visualize=False)
breakpoint()
#DONE