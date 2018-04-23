import SimpleITK as sitk
import matplotlib.pyplot as plt
import sys

def image_read(filename, labels):
    _file_name = filename
    _img = sitk.ReadImage(_file_name, sitk.sitkFloat32)
    _img = sitk.GetArrayFromImage(_img)

    # TODO: Extract filename substring and compare to labels

    return _img