import numpy as np
import matplotlib.pyplot as plt
from rasterio.plot import show
import rasterio

def nequalize(array,p=5,nodata=0):
    #Si la imagen es una sola banda: (alto, ancho) simplemente calcula el percentil y normaliza
    if len(array.shape)==2:
        vmin=np.percentile(array[array!=nodata],p)
        vmax=np.percentile(array[array!=nodata],100-p)
        eq_array = (array-vmin)/(vmax-vmin)
        eq_array[eq_array>1]=1
        eq_array[eq_array<0]=0
    #Si la imagen tiene varias banda: (cantidad de bandas, alto, ancho), hace lo anterior pero para cada banda por separado
    elif len(array.shape)==3:
        eq_array = np.empty_like(array, dtype=float)
        for i in range(array.shape[0]):
            eq_array[i]=nequalize(array[i], p=p, nodata=nodata)
    return eq_array

def plot_rgb(array, band_list , p = 0, nodata = None, figsize = (12,6), title = None):
    '''
    Esta función toma como parámetros de entrada la matriz a ser ploteada, 
    una lista de índices correspondientes a las bandas que queremos usar, 
    en el orden que deben estar (ej: [1,2,3]), y un parámetro p que es opcional 
    que es el percentil de equalización.
    
    Por defecto tambien asigna un tamaño de figura en (12,6), que también puede ser modificado.
    
    Devuelve solamente un ploteo, no modifica el arreglo original.
    Nota: array debe ser una matriz con estas dimensiones de entrada: [bandas, filas, columnas]
    '''
    if not title:
        title = f'Combinación {band_list} \n (percentil {p}%)'
        
    img = nequalize(array[band_list], p=p, nodata=nodata)
    plt.figure(figsize = figsize)
    plt.title(title , size = 20)
    show(img)
    plt.show()    
    
#Elimina los valores de nodata, por defecto los toma como 0 y normaliza por el factor de reflactancia
def delNone(array, nodata = 0, factor=10000): 
    return array[array!=nodata]/factor

def guardar_GTiff(fn, crs, transform, mat, meta=None, nodata=None, bandnames=[]):
    if len(mat.shape)==2:
        count=1
    else:
        count=mat.shape[0]

    if not meta:
        meta = {}

    meta['driver'] = 'GTiff'
    meta['height'] = mat.shape[-2]
    meta['width'] = mat.shape[-1]
    meta['count'] = count
    meta['crs'] = crs
    meta['transform'] = transform

    if 'dtype' not in meta: #if no datatype is specified, use float32
        meta['dtype'] = np.float32
    

    if nodata==None:
        pass
    else:
        meta['nodata'] = nodata

    with rasterio.open(fn, 'w', **meta) as dst:
        if count==1: #es una matriz bidimensional, la guardo
            dst.write(mat.astype(meta['dtype']), 1)
            if bandnames:
                dst.set_band_description(1, bandnames[0])
        else: #es una matriz tridimensional, guardo cada banda
            for b in range(count):
                dst.write(mat[b].astype(meta['dtype']), b+1)
            for b,bandname in enumerate(bandnames):
                dst.set_band_description(b+1, bandname)#   