# conding=utf8
import math
import os
import cv2

# format train txt
import numpy


class formatTrain:

    def run(self):

        g = os.walk(r"./train_data/mtwi/txt_train")
        # g = os.walk(r"./train_data/chword/txt_train")

        # write imageFile to train.txt
        trainTxt = "./train_data/mtwi/train.txt"
        # trainTxt = "./train_data/chword/train.txt"
        f = open(trainTxt, 'w')

        textFiles = []
        # list text file
        for path, dir_list, file_list in g:
            for file_name in file_list:
                textFile = os.path.join(path, file_name)
                textFiles.append(textFile)
        i = 0
        for textFile in textFiles:
            # read label
            textF = open(textFile, 'r')
            imageFile = textFile.replace("txt_train", "image_train").replace(".txt", ".jpg")
            chTrainPath = "./train_data/mtwi/train/"
            # chTrainPath = "./train_data/chword/train/"
            if not os.path.exists(imageFile):
                continue
            # imageFile = imageFile.replace("./", "")
            img = cv2.imread(imageFile)
            print(imageFile)
            if not isinstance(img, numpy.ndarray):
                continue
            while True:
                i = i + 1
                if i > 1000:
                    exit()
                label = textF.readline()
                if len(label) == 0:
                    break
                label = label.split(",")
                print(label)

                box = {0: [label[0], label[1]], 1: [label[6], label[7]], 2: [label[4], label[5]],
                       3: [label[2], label[3]]}
                targetPath = chTrainPath + "chword_" + str(i) + ".jpg"
                print(targetPath)
                ret = self.shot(img, box, targetPath)
                if label[8].find("#") >= 0:
                    continue
                if not ret:
                    continue
                f.writelines(targetPath.replace("./train_data/", "") + "\t" + label[8])
                # f.write('\n')
            # break

    def shot(self, img, box, targetPath):  # 应用于predict_det.py中,通过dt_boxes中获得的四个坐标点,裁剪出图像
        # dt_boxes = np_list_int(dt_boxes)
        num = 0
        # box = dt_boxes[num]
        tl = box[0]
        tr = box[1]
        br = box[2]
        bl = box[3]
        # print("打印转换成功数据num =" + str(num))
        # print("tl:" + str(tl), "tr:" + str(tr), "br:" + str(br), "bl:" + str(bl))
        # print(tr[1], bl[1], tl[0], br[0])
        ty = math.floor(float(tr[1]))
        by = math.ceil(float(bl[1]))
        lx = math.floor(float(tl[0]))
        rx = math.ceil(float(br[0]))

        if lx < 0:
            lx = 0
        if rx < 0:
            rx = 0
        if lx > rx:
            lx, rx = rx, lx
        if ty > by:
            ty, by = by, ty
        print("t y ", ty)
        print("b y ", by)
        print("l x ", lx)
        print("r x ", rx)
        print("img type ", type(img))
        if lx == rx or ty == by:
            return False
        crop = img[ty:by, lx:rx]
        # cv2.polylines(src_im, [box], True, color=(255, 255, 0), thickness=2)
        # crop = img[27:45, 67:119] #测试
        # crop = img[380:395, 368:119]
        # cv2.imshow('img2', crop)

        # cv2.waitKey(5)
        if len(crop) > 0:
            cv2.imwrite(targetPath, crop)
            return True
        return False

    def np_list_int(tb):
        tb_2 = tb.tolist()  # 将np转换为列表
        return tb_2


fmt = formatTrain()

fmt.run()
