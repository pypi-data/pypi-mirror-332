# in_image_blend/image_blend.pyx
# cython: boundscheck=False, wraparound=False, nonecheck=False, cdivision=True
import numpy as np
cimport numpy as cnp

ctypedef cnp.float32_t FLOAT32

cpdef cnp.ndarray[FLOAT32, ndim=3] blend_images(
    cnp.ndarray[FLOAT32, ndim=3] img1, 
    cnp.ndarray[FLOAT32, ndim=3] img2, 
    cnp.ndarray[FLOAT32, ndim=2] mask
):
    """
    使用 mask 对两张图像进行混合
    """
    cdef int h = img1.shape[0]
    cdef int w = img1.shape[1]
    cdef int c = img1.shape[2]
    cdef int i, j, k
    cdef float mask_value

    cdef cnp.ndarray[FLOAT32, ndim=3] result = np.empty((h, w, c), dtype=np.float32)

    for i in range(h):
        for j in range(w):
            mask_value = mask[i, j]
            for k in range(c):
                result[i, j, k] = img1[i, j, k] * (1.0 - mask_value) + img2[i, j, k] * mask_value

    return result
