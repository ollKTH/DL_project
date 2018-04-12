import SimpleITK as sitk
import matplotlib.pyplot as plt
import sys

def image_read(filename):
    _file_name = filename
    _img = sitk.ReadImage(_file_name, sitk.sitkFloat32)
    _img = sitk.GetArrayFromImage(_img)

    return _img

if __name__ == '__main__':
    plt.close()
    images = []
    img = image_read('images/test_MRI.nii')

    for i in range(17, 27):
        plt.subplot(2, 5, i - 16)
        plt.imshow(img[i, :, :], 'gray')

        images.append(img[i, :, :])

    plt.show()