import cv2


class TargetDetect:
    def __init__(self):
        self.hog = cv2.HOGDescriptor()  # 定义一个模型
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # 分类是基于人的分类

    def is_inside(self, o, i):  # 如果o框在i框里面，那么就返回True，否则，返回False
        ox, oy, ow, oh = o
        ix, iy, iw, ih = i
        return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh < iy + ih

    @staticmethod
    def draw_person(img, person):  # 给检测出来的人画框
        x, y, w, h = person
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

    def dectect(self, img):

        found, w = self.hog.detectMultiScale(img)  # 这里用detectMultiScale来加载图像
        # found is the rectangle of target

        found_filtered = []
        for ri, r in enumerate(found):
            for qi, q in enumerate(found):
                if ri != qi and self.is_inside(r, q):  # 如果是索引不同的两个框，并且r框在q框里面完全包含了，就直接break
                    print('过')  # 这里我们发现没有这种不同框相互包含的情况，三个框都不是相互包含的关系
                    break
                else:
                    found_filtered.append(r)
        for person in found_filtered:
            self.draw_person(img, person)

        return img


if __name__ == "__main__":
    detectModel = TargetDetect()
    img = cv2.imread('../video/people3.png')
    detectModel.dectect(img)