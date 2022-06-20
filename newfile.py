from skimage import data, io, filters
img = io.imread('https://res.cloudinary.com/https-res-cloudinary-com/image/upload/v1654970085/287098182_135588525752786_8267174775425889726_n_ij51x6.jpg')
edges = filters.sobel(img)
io.imshow(edges)
io.show()