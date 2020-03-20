from pigeon import annotate
from IPython.display import display, Image
import glob

list = glob.glob("Dataset//*.png")

# print(list)

annotations = annotate(
  list,
  options=['Dhaka', 'Metro', '1','2','3','4', '5','6','7','8','9','0','GA'],
  display_fn=lambda filename: display(Image(filename))
)