from sklearn.cluster import KMeans

raster_fn = 'Imagenes enero 2021/Norte_20mTODOS.tif'

with rasterio.open(raster_fn) as src:
    img = src.read()
    crs = src.crs
    gt = src.transform
    
d,x,y = s2_mask.shape
X = s2_mask.reshape([d,x*y]).T
X = X/10000

bandas = ['Banda 1', 'Azul', 'Verde', 'Rojo', 'Banda 5', 'Banda 6', 'Banda 7', 'NIR', 'Banda 9', 'SWIR 1', 'SWIR 2']

Cantidad_de_grupos = [5,7,9,11,13,15]

for i in Cantidad_de_grupos:
    kmeans = KMeans(n_clusters=i)#, random_state=0)
    kmeans.fit(X)
    L = kmeans.labels_
    Yimg = L.reshape([x,y])
    Yimg = Yimg.astype('float64')
    Yimg[Yimg==0.] = np.nan
    
    plt.figure(figsize=(15,10))
    plt.title('n_cluster: '+str(i), fontsize = 20)
    show(Yimg, cmap='Spectral')
    
    bandx, bandy = 3,7
    
    N = 5000
    R = np.random.randint(low=0, high=X.shape[0],size=N)#X.shape[0])
    plt.figure(figsize=(7,4))
    plt.scatter(X[R,bandx], X[R,bandy], c=L[R], cmap='Spectral')
    plt.xlabel(bandas[bandx])
    plt.ylabel(bandas[bandy])