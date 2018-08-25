Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot
>>> import matplotlib.pyplot as plt
>>> w = np.array([  1.58876117,   3.17458055,  11.11863105])
>>> w
array([ 1.58876117,  3.17458055, 11.11863105])
>>> x2 = [w[0], w[1], -w[1], w[0]]
>>> x2
[1.58876117, 3.17458055, -3.17458055, 1.58876117]
>>> x3 = [w[0], w[1], w[1], -w[0]]
>>> x3
[1.58876117, 3.17458055, 3.17458055, -1.58876117]
>>> x2x3 = np.array([x2,x3])
>>> x2x3
array([[ 1.58876117,  3.17458055, -3.17458055,  1.58876117],
       [ 1.58876117,  3.17458055,  3.17458055, -1.58876117]])
>>> list(zip(*x2x3))
[(1.58876117, 1.58876117), (3.17458055, 3.17458055), (-3.17458055, 3.17458055), (1.58876117, -1.58876117)]
>>> X,Y,U,V = zip(*x2x3)
>>> X
(1.58876117, 1.58876117)
>>> Y
(3.17458055, 3.17458055)
>>> U
(-3.17458055, 3.17458055)
>>> V
(1.58876117, -1.58876117)
>>> ax = plt.gca()
>>> ax.quiver(X,Y,U,V,color='blue')
<matplotlib.quiver.Quiver object at 0x0000013810910CF8>
>>> plt.show()
>>> ax.quiver(X,Y,U,V,color='blue',scale=1)
<matplotlib.quiver.Quiver object at 0x0000013810910DA0>
>>> plt.show()
>>> ax = plt.gca()
>>> ax.quiver(X,Y,U,V,color='blue',scale=1)
<matplotlib.quiver.Quiver object at 0x000001381240A9B0>
>>> plt.show()
>>> list(zip(*x2x3))
[(1.58876117, 1.58876117), (3.17458055, 3.17458055), (-3.17458055, 3.17458055), (1.58876117, -1.58876117)]
>>> x2x3
array([[ 1.58876117,  3.17458055, -3.17458055,  1.58876117],
       [ 1.58876117,  3.17458055,  3.17458055, -1.58876117]])
>>> list(zip(x2x3))
[(array([ 1.58876117,  3.17458055, -3.17458055,  1.58876117]),), (array([ 1.58876117,  3.17458055,  3.17458055, -1.58876117]),)]
>>> x = np.array([3,4,5,7,1,2])
>>> y = np.arr
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    y = np.arr
AttributeError: module 'numpy' has no attribute 'arr'
>>> y = np.array([1,2,3,4,5,6])
>>> x
array([3, 4, 5, 7, 1, 2])
>>> y
array([1, 2, 3, 4, 5, 6])
>>> np.meshgrid(x,y)
[array([[3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2]]), array([[1, 1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5, 5],
       [6, 6, 6, 6, 6, 6]])]
>>> xx,yy = np.meshgrid(x,y)
>>> xx
array([[3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2],
       [3, 4, 5, 7, 1, 2]])
>>> yy
array([[1, 1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4, 4],
       [5, 5, 5, 5, 5, 5],
       [6, 6, 6, 6, 6, 6]])
>>> z = xx * yy
>>> plt.contour(x,y,z)
<matplotlib.contour.QuadContourSet object at 0x00000138125F9CC0>
>>> plt.show()
>>> plt.contourf(x,y,z)
<matplotlib.contour.QuadContourSet object at 0x00000138127E6278>
>>> plt.show()
>>> from sklearn.datasets import load_iris
>>> dataset = load_iris()
>>> dataset.head()
Traceback (most recent call last):
  File "C:\Python36\lib\site-packages\sklearn\utils\__init__.py", line 61, in __getattr__
    return self[key]
KeyError: 'head'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dataset.head()
  File "C:\Python36\lib\site-packages\sklearn\utils\__init__.py", line 63, in __getattr__
    raise AttributeError(key)
AttributeError: head
>>> dataset.data()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dataset.data()
TypeError: 'numpy.ndarray' object is not callable
>>> dataset.data
array([[5.1, 3.5, 1.4, 0.2],
       [4.9, 3. , 1.4, 0.2],
       [4.7, 3.2, 1.3, 0.2],
       [4.6, 3.1, 1.5, 0.2],
       [5. , 3.6, 1.4, 0.2],
       [5.4, 3.9, 1.7, 0.4],
       [4.6, 3.4, 1.4, 0.3],
       [5. , 3.4, 1.5, 0.2],
       [4.4, 2.9, 1.4, 0.2],
       [4.9, 3.1, 1.5, 0.1],
       [5.4, 3.7, 1.5, 0.2],
       [4.8, 3.4, 1.6, 0.2],
       [4.8, 3. , 1.4, 0.1],
       [4.3, 3. , 1.1, 0.1],
       [5.8, 4. , 1.2, 0.2],
       [5.7, 4.4, 1.5, 0.4],
       [5.4, 3.9, 1.3, 0.4],
       [5.1, 3.5, 1.4, 0.3],
       [5.7, 3.8, 1.7, 0.3],
       [5.1, 3.8, 1.5, 0.3],
       [5.4, 3.4, 1.7, 0.2],
       [5.1, 3.7, 1.5, 0.4],
       [4.6, 3.6, 1. , 0.2],
       [5.1, 3.3, 1.7, 0.5],
       [4.8, 3.4, 1.9, 0.2],
       [5. , 3. , 1.6, 0.2],
       [5. , 3.4, 1.6, 0.4],
       [5.2, 3.5, 1.5, 0.2],
       [5.2, 3.4, 1.4, 0.2],
       [4.7, 3.2, 1.6, 0.2],
       [4.8, 3.1, 1.6, 0.2],
       [5.4, 3.4, 1.5, 0.4],
       [5.2, 4.1, 1.5, 0.1],
       [5.5, 4.2, 1.4, 0.2],
       [4.9, 3.1, 1.5, 0.1],
       [5. , 3.2, 1.2, 0.2],
       [5.5, 3.5, 1.3, 0.2],
       [4.9, 3.1, 1.5, 0.1],
       [4.4, 3. , 1.3, 0.2],
       [5.1, 3.4, 1.5, 0.2],
       [5. , 3.5, 1.3, 0.3],
       [4.5, 2.3, 1.3, 0.3],
       [4.4, 3.2, 1.3, 0.2],
       [5. , 3.5, 1.6, 0.6],
       [5.1, 3.8, 1.9, 0.4],
       [4.8, 3. , 1.4, 0.3],
       [5.1, 3.8, 1.6, 0.2],
       [4.6, 3.2, 1.4, 0.2],
       [5.3, 3.7, 1.5, 0.2],
       [5. , 3.3, 1.4, 0.2],
       [7. , 3.2, 4.7, 1.4],
       [6.4, 3.2, 4.5, 1.5],
       [6.9, 3.1, 4.9, 1.5],
       [5.5, 2.3, 4. , 1.3],
       [6.5, 2.8, 4.6, 1.5],
       [5.7, 2.8, 4.5, 1.3],
       [6.3, 3.3, 4.7, 1.6],
       [4.9, 2.4, 3.3, 1. ],
       [6.6, 2.9, 4.6, 1.3],
       [5.2, 2.7, 3.9, 1.4],
       [5. , 2. , 3.5, 1. ],
       [5.9, 3. , 4.2, 1.5],
       [6. , 2.2, 4. , 1. ],
       [6.1, 2.9, 4.7, 1.4],
       [5.6, 2.9, 3.6, 1.3],
       [6.7, 3.1, 4.4, 1.4],
       [5.6, 3. , 4.5, 1.5],
       [5.8, 2.7, 4.1, 1. ],
       [6.2, 2.2, 4.5, 1.5],
       [5.6, 2.5, 3.9, 1.1],
       [5.9, 3.2, 4.8, 1.8],
       [6.1, 2.8, 4. , 1.3],
       [6.3, 2.5, 4.9, 1.5],
       [6.1, 2.8, 4.7, 1.2],
       [6.4, 2.9, 4.3, 1.3],
       [6.6, 3. , 4.4, 1.4],
       [6.8, 2.8, 4.8, 1.4],
       [6.7, 3. , 5. , 1.7],
       [6. , 2.9, 4.5, 1.5],
       [5.7, 2.6, 3.5, 1. ],
       [5.5, 2.4, 3.8, 1.1],
       [5.5, 2.4, 3.7, 1. ],
       [5.8, 2.7, 3.9, 1.2],
       [6. , 2.7, 5.1, 1.6],
       [5.4, 3. , 4.5, 1.5],
       [6. , 3.4, 4.5, 1.6],
       [6.7, 3.1, 4.7, 1.5],
       [6.3, 2.3, 4.4, 1.3],
       [5.6, 3. , 4.1, 1.3],
       [5.5, 2.5, 4. , 1.3],
       [5.5, 2.6, 4.4, 1.2],
       [6.1, 3. , 4.6, 1.4],
       [5.8, 2.6, 4. , 1.2],
       [5. , 2.3, 3.3, 1. ],
       [5.6, 2.7, 4.2, 1.3],
       [5.7, 3. , 4.2, 1.2],
       [5.7, 2.9, 4.2, 1.3],
       [6.2, 2.9, 4.3, 1.3],
       [5.1, 2.5, 3. , 1.1],
       [5.7, 2.8, 4.1, 1.3],
       [6.3, 3.3, 6. , 2.5],
       [5.8, 2.7, 5.1, 1.9],
       [7.1, 3. , 5.9, 2.1],
       [6.3, 2.9, 5.6, 1.8],
       [6.5, 3. , 5.8, 2.2],
       [7.6, 3. , 6.6, 2.1],
       [4.9, 2.5, 4.5, 1.7],
       [7.3, 2.9, 6.3, 1.8],
       [6.7, 2.5, 5.8, 1.8],
       [7.2, 3.6, 6.1, 2.5],
       [6.5, 3.2, 5.1, 2. ],
       [6.4, 2.7, 5.3, 1.9],
       [6.8, 3. , 5.5, 2.1],
       [5.7, 2.5, 5. , 2. ],
       [5.8, 2.8, 5.1, 2.4],
       [6.4, 3.2, 5.3, 2.3],
       [6.5, 3. , 5.5, 1.8],
       [7.7, 3.8, 6.7, 2.2],
       [7.7, 2.6, 6.9, 2.3],
       [6. , 2.2, 5. , 1.5],
       [6.9, 3.2, 5.7, 2.3],
       [5.6, 2.8, 4.9, 2. ],
       [7.7, 2.8, 6.7, 2. ],
       [6.3, 2.7, 4.9, 1.8],
       [6.7, 3.3, 5.7, 2.1],
       [7.2, 3.2, 6. , 1.8],
       [6.2, 2.8, 4.8, 1.8],
       [6.1, 3. , 4.9, 1.8],
       [6.4, 2.8, 5.6, 2.1],
       [7.2, 3. , 5.8, 1.6],
       [7.4, 2.8, 6.1, 1.9],
       [7.9, 3.8, 6.4, 2. ],
       [6.4, 2.8, 5.6, 2.2],
       [6.3, 2.8, 5.1, 1.5],
       [6.1, 2.6, 5.6, 1.4],
       [7.7, 3. , 6.1, 2.3],
       [6.3, 3.4, 5.6, 2.4],
       [6.4, 3.1, 5.5, 1.8],
       [6. , 3. , 4.8, 1.8],
       [6.9, 3.1, 5.4, 2.1],
       [6.7, 3.1, 5.6, 2.4],
       [6.9, 3.1, 5.1, 2.3],
       [5.8, 2.7, 5.1, 1.9],
       [6.8, 3.2, 5.9, 2.3],
       [6.7, 3.3, 5.7, 2.5],
       [6.7, 3. , 5.2, 2.3],
       [6.3, 2.5, 5. , 1.9],
       [6.5, 3. , 5.2, 2. ],
       [6.2, 3.4, 5.4, 2.3],
       [5.9, 3. , 5.1, 1.8]])
>>> dataset.target
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
>>> dataset.target_names
array(['setosa', 'versicolor', 'virginica'], dtype='<U10')
>>> from sklearn.datasets import load_digits
>>> digits = load_digits()
>>> len(digits.data)
1797
>>> digits.target
array([0, 1, 2, ..., 8, 9, 8])
>>> digits.data[0]
array([ 0.,  0.,  5., 13.,  9.,  1.,  0.,  0.,  0.,  0., 13., 15., 10.,
       15.,  5.,  0.,  0.,  3., 15.,  2.,  0., 11.,  8.,  0.,  0.,  4.,
       12.,  0.,  0.,  8.,  8.,  0.,  0.,  5.,  8.,  0.,  0.,  9.,  8.,
        0.,  0.,  4., 11.,  0.,  1., 12.,  7.,  0.,  0.,  2., 14.,  5.,
       10., 12.,  0.,  0.,  0.,  0.,  6., 13., 10.,  0.,  0.,  0.])
>>> plt.imshow(digits.data[0])
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    plt.imshow(digits.data[0])
  File "C:\Python36\lib\site-packages\matplotlib\pyplot.py", line 3157, in imshow
    **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\__init__.py", line 1898, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 5124, in imshow
    im.set_data(X)
  File "C:\Python36\lib\site-packages\matplotlib\image.py", line 600, in set_data
    raise TypeError("Invalid dimensions for image data")
TypeError: Invalid dimensions for image data
>>> len(digits.data[0])
64
>>> plt.imshow(digits.data[0].reshape(8,8))
<matplotlib.image.AxesImage object at 0x00000138113912B0>
>>> plt.show()
>>> plt.imshow(digits.data[0].reshape(8,8), cmap='gist-gray')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    plt.imshow(digits.data[0].reshape(8,8), cmap='gist-gray')
  File "C:\Python36\lib\site-packages\matplotlib\pyplot.py", line 3157, in imshow
    **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\__init__.py", line 1898, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 5122, in imshow
    resample=resample, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\image.py", line 753, in __init__
    **kwargs
  File "C:\Python36\lib\site-packages\matplotlib\image.py", line 228, in __init__
    cm.ScalarMappable.__init__(self, norm, cmap)
  File "C:\Python36\lib\site-packages\matplotlib\cm.py", line 208, in __init__
    self.cmap = get_cmap(cmap)
  File "C:\Python36\lib\site-packages\matplotlib\cm.py", line 173, in get_cmap
    % (name, ', '.join(sorted(cmap_d.keys()))))
ValueError: Colormap gist-gray is not recognized. Possible values are: Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Vega10, Vega10_r, Vega20, Vega20_r, Vega20b, Vega20b_r, Vega20c, Vega20c_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
>>> plt.imshow(digits.data[0].reshape(8,8), cmap='gist_gray')
<matplotlib.image.AxesImage object at 0x00000138133B84E0>
>>> plt.show()
>>> plt.imshow(digits.data[10].reshape(8,8), cmap='gist_gray')
<matplotlib.image.AxesImage object at 0x00000138100D46A0>
>>> plt.show()
>>> plt.imshow(digits.data[55].reshape(8,8), cmap='gist_gray')
<matplotlib.image.AxesImage object at 0x0000013810177198>
>>> plt.show()
>>> plt.imshow(digits.data[58].reshape(8,8), cmap='gist_gray')
<matplotlib.image.AxesImage object at 0x0000013810389BA8>
>>> plt.show()
>>> plt.imshow(digits.data[59].reshape(8,8), cmap='gist_gray')
<matplotlib.image.AxesImage object at 0x000001381080AE48>
>>> plt.show()
>>> import array
>>> x = array.array([1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    x = array.array([1,2,3,4,5])
TypeError: array() argument 1 must be a unicode character, not list
>>> x = array.array(5)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    x = array.array(5)
TypeError: array() argument 1 must be a unicode character, not int
>>> x = array('l', [1, 2, 3, 4, 5])
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    x = array('l', [1, 2, 3, 4, 5])
TypeError: 'module' object is not callable
>>> 
