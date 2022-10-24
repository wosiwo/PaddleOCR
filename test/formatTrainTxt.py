# conding=utf8
import os

# format train txt

g = os.walk(r"./train_data/mtwi/txt_train")

# write imageFile to train.txt
trainTxt = "./train_data/mtwi/train.txt"
f = open(trainTxt, 'w')

for path, dir_list, file_list in g:
    for file_name in file_list:
        textFile = os.path.join(path, file_name)
        # read label
        textF = open(textFile, 'r')
        labels = textF.read(1)
        imageFile = textFile.replace("txt_train", "image_train").replace(".txt", ".jpg")
        if os.path.exists(imageFile):
            imageFile = imageFile.replace("./", "")
            print(imageFile)
            f.writelines(imageFile)
            f.write('\n')

