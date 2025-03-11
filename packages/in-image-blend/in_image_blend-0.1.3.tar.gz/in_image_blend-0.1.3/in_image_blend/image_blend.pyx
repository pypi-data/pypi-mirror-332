# in_image_blend/image_blend.pyx
# cython: boundscheck=False, wraparound=False, nonecheck=False, cdivision=True
import numpy as np
cimport numpy as cnp

ctypedef cnp.uint8_t UINT8
ctypedef cnp.int32_t INT32

cpdef cnp.ndarray[UINT8, ndim=3] blend_images(
    cnp.ndarray[UINT8, ndim=3] img1, 
    cnp.ndarray[UINT8, ndim=3] img2, 
    cnp.ndarray[UINT8, ndim=2] mask
):
    cdef int h = img1.shape[0]
    cdef int w = img1.shape[1]
    cdef int c = img1.shape[2]
    cdef int i, j, k
    cdef float mask_value
    
    cdef cnp.ndarray[UINT8, ndim=3] result = np.empty((h, w, c), dtype=np.uint8)
    
    for i in range(h):
        for j in range(w):
            mask_value = mask[i, j] / 255.0
            for k in range(c):
                result[i, j, k] = <UINT8>(img1[i, j, k] * (1.0 - mask_value) + img2[i, j, k] * mask_value + 0.5)

    return result