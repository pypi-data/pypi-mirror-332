# (C) Copyright 2015 Frankfurt Institute for Advanced Studies
# (C) Copyright 2016 Max-Planck Institute for Brain Research
#
# Author: Philipp Huelsdunk  <huelsdunk@fias.uni-frankfurt.de>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#     * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#     * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#     * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

__author__ = 'Philipp Hülsdunk'
__email__ ='philipp.huelsdunk@brain.mpg.de'

import numpy as np
import cv2
import scipy.optimize
import scipy.fftpack

def cross_correlation_fft(source_fft, target_fft, upsample_factor=None):
    # Compute cross correlation in fft
    # CC(f, g) = Conv(f, g(-x)) = F^(-1){F{f} * F{g(-x)}}
    # Then, the conjugation property is used:
    # F{g(-x)} = F{g(x)}.conj
    # resulting in
    # CC(f, g) = F^(-1){F{f} * F{g}.conj}
    image_product = source_fft * target_fft.conj()
    cross_correlation = scipy.fftpack.fftshift( \
            scipy.fftpack.ifft2(image_product))
    
    # Find the peak
    maxima = np.unravel_index(np.argmax(cross_correlation.real), \
            cross_correlation.shape)
    shifts = np.array(maxima, 'float32') - np.array(target_fft.shape) / 2.

    if upsample_factor is None:
        return -shifts[::-1], cross_correlation[maxima].real
        
    # Initial shift estimate in upsampled grid
    shifts = np.round(shifts * upsample_factor) / upsample_factor
    upsampled_region_size = np.ceil(upsample_factor * 1.5)
    # Center of output array at dftshift + 1
    upsample_factor = np.array(upsample_factor, 'float32')
    dftshift = np.fix(upsampled_region_size / 2.)
    
    # Sum up all cross correlations in the smaller region
    # Matrix multiply DFT around the current shift estimate
    sample_region_offset = dftshift - shifts * upsample_factor
    cross_correlation = __upsampled_dft(image_product.conj(),
                                        upsampled_region_size,
                                        upsample_factor,
                                        sample_region_offset).conj()

    # Locate maximum and map back to original pixel grid
    maxima = np.unravel_index(np.argmax(cross_correlation.real),
            cross_correlation.shape)
    upsampled_shifts = np.array(maxima, 'float32')
    shifts += (upsampled_shifts - dftshift) / upsample_factor
        
    return -shifts[::-1], cross_correlation[maxima].real

def phase_correlation(source_fft, target_fft, upsample_factor=None):
    # Compute the phase correlation
    image_product = source_fft * target_fft.conj()
    phase_correlation = image_product / np.abs(image_product)
    cross_correlation = scipy.fftpack.fftshift( \
            scipy.fftpack.ifft2(phase_correlation))
    
    # Find the shift
    maxima = np.unravel_index(np.argmax(np.abs(cross_correlation)),
            cross_correlation.shape)
    shifts = np.array(maxima, 'float32') - np.array(target_fft.shape) / 2.
    
    if upsample_factor is None:
        return -shifts[::-1], np.abs(cross_correlation[maxima])

    # Initial shift estimate in upsampled grid
    shifts = np.round(shifts * upsample_factor) / upsample_factor
    upsampled_region_size = np.ceil(upsample_factor * 1.5)
    # Center of output array at dftshift + 1
    upsample_factor = np.array(upsample_factor, 'float32')
    dftshift = np.fix(upsampled_region_size / 2.)
    
    # Sum up all cross correlations in the smaller region
    # Matrix multiply DFT around the current shift estimate
    sample_region_offset = dftshift - shifts * upsample_factor
    cross_correlation = __upsampled_dft(phase_correlation.conj(),
                                        upsampled_region_size,
                                        upsample_factor,
                                        sample_region_offset).conj()

    # Locate maximum and map back to original pixel grid
    maxima = np.unravel_index(np.argmax(np.abs(cross_correlation)),
            cross_correlation.shape)
    upsampled_shifts = np.array(maxima, 'float32')
    shifts += (upsampled_shifts - dftshift) / upsample_factor
        
    return -shifts[::-1], np.abs(cross_correlation[maxima])

def __upsampled_dft(data, upsampled_region_size,
                    upsample_factor=1, axis_offsets=None):
    """
    Upsampled DFT by matrix multiplication.
    This code is intended to provide the same result as if the following
    operations were performed:
        - Embed the array "data" in an array that is ``upsample_factor`` times
          larger in each dimension.  ifftshift to bring the center of the
          image to (1,1).
        - Take the FFT of the larger array.
        - Extract an ``[upsampled_region_size]`` region of the result, starting
          with the ``[axis_offsets+1]`` element.
    It achieves this result by computing the DFT in the output array without
    the need to zeropad. Much faster and memory efficient than the zero-padded
    FFT approach if ``upsampled_region_size`` is much smaller than
    ``data.size * upsample_factor``.
    Parameters
    ----------
    data : 2D ndarray
        The input data array (DFT of original data) to upsample.
    upsampled_region_size : integer or tuple of integers, optional
        The size of the region to be sampled.  If one integer is provided, it
        is duplicated up to the dimensionality of ``data``.
    upsample_factor : integer, optional
        The upsampling factor.  Defaults to 1.
    axis_offsets : tuple of integers, optional
        The offsets of the region to be sampled.  Defaults to None (uses
        image center)
    Returns
    -------
    output : 2D ndarray
            The upsampled DFT of the specified region.
    """

    # if people pass in an integer, expand it to a list of equal-sized sections
    if not hasattr(upsampled_region_size, "__iter__"):
        upsampled_region_size = [upsampled_region_size, ] * data.ndim
    else:
        if len(upsampled_region_size) != data.ndim:
            raise ValueError("shape of upsampled region sizes must be equal "
                             "to input data's number of dimensions.")

    if axis_offsets is None:
        axis_offsets = [0, ] * data.ndim
    else:
        if len(axis_offsets) != data.ndim:
            raise ValueError("number of axis offsets must be equal to input "
                             "data's number of dimensions.")

    col_kernel = np.exp(
        (-1.j * 2. * np.pi / (data.shape[1] * upsample_factor)) *
        (scipy.fftpack.ifftshift(np.arange(data.shape[1]))[:, None] -
         np.floor(data.shape[1] / 2.)).dot(
             np.arange(upsampled_region_size[1])[None, :] - axis_offsets[1])
    )
    row_kernel = np.exp(
        (-1.j * 2. * np.pi / (data.shape[0] * upsample_factor)) *
        (np.arange(upsampled_region_size[0])[:, None] - axis_offsets[0]).dot(
            scipy.fftpack.ifftshift(np.arange(data.shape[0]))[None, :] -
            np.floor(data.shape[0] / 2.))

    )

    return row_kernel.dot(data).dot(col_kernel)


def match_template_brute(template, img_fft,
        logscale_x=slice(0, 1, 1), \
        logscale_y=slice(0, 1, 1), \
        rotation=slice(-np.pi, np.pi, 2. * np.pi / 180.), \
        shear=slice(0, 1, 1),
        upsample_factor=None, \
        find_translation=phase_correlation,
        return_rotation_shear=False):
    '''
    Brute force image registration.

    Parameters:
    ===========
    template : Image to be aligned
    img_fft : Fourier representation of the input image
    logscale_x, logscale_y, rotation, shear : grid to evaluate over
    upsample_factor : sub-pixel shift evaluation
    find_translation : method for finding the shift
    return_rotation_shear : if True, return the optimal rotation and shear
    '''

    # Input image can be of different size; we have to do a embedding in the
    # Fourier space lateron, this requires to shift the template to the
    # center of the image, with the help of the fourier shift theorem, we
    # calculate the scale factors in the Fourier domain:
    template_mid = np.array(template.shape, 'float32')[::-1] / 2.
    img_mid = np.array(img_fft.shape, 'float32')[::-1] / 2.
    midshift = img_mid - template_mid
    gy, gx = (scipy.fftpack.fftfreq(s) for s in img_fft.shape)
    factor = 2. * np.pi \
            * (gy[:, None] * midshift[1] + gx[None, :] * midshift[0])
    midshift_fft = np.cos(factor) - 1j * np.sin(factor)

    def __corr_opt_function(params):
        log_scale_x, log_scale_y, rotation, shear = params
        # Create transform matrix
        t = np.zeros((2,3), 'float32')

        # Set up rotation, scale and shear
        rot_mat = np.array([[+np.cos(rotation), +np.sin(rotation)], \
                            [-np.sin(rotation), +np.cos(rotation)]], \
                            'float32')
        scale_mat = np.array([[np.exp(log_scale_x), 0], \
                              [0, np.exp(log_scale_y)]], \
                              'float32')
        shear_mat = np.array([[1, shear], \
                              [0, 1]], \
                              'float32')
        t[:, 0:2] = np.dot(rot_mat, np.dot(scale_mat, shear_mat))

        # Set shift
        t[:, 2] = template_mid - np.dot(t[:, :2], template_mid) + t[:, 2]

        # Warp the source map given the too opt transform
        template_t = cv2.warpAffine(template, t, template.shape[::-1])

        # Do the phase correlation
        template_t_fft = scipy.fftpack.fft2(template_t, img_fft.shape) \
                * midshift_fft
        t[:, 2] += midshift

        # Find shift
        shifts, cross_correlation = find_translation(template_t_fft, img_fft, \
                upsample_factor=upsample_factor)
        t[:, 2] += shifts

        return t, cross_correlation
    
    # Run optimizer
    opt_result = scipy.optimize.brute( \
        func=lambda x: -__corr_opt_function(x)[1], \
        ranges=(logscale_x, logscale_y, rotation, shear),
        finish=None)

    # Extract transformation and return result
    optimal_transformation, optimal_correlation = __corr_opt_function(opt_result)

    if return_rotation_shear:
        optimal_rotation = opt_result[2]
        optimal_shear = opt_result[3]
        return optimal_transformation, optimal_rotation, optimal_shear, optimal_correlation
    else:
        return optimal_transformation, optimal_correlation