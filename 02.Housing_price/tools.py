from six.moves import urllib
import pandas as pd
import os 
import tarfile
import hashlib
import numpy as np

def fetch_data(url, path, tgz):
    """
    Crea una carpeta dataset/.. en nuestro workspace, y descarga un archivo .tgz, y extrae el .csv
    
    url: address of the file you want to download
    path: folder where that file is located
    tgz: name of the .tgz file to create (add .tgz at the end)
    """
    if not os.path.isdir(path):
        os.makedir(path)
    tgz_path = os.path.join(path, tgz)
    urllib.request.urlretrieve(url, tgz_path)
    file_tgz = tarfile.open(tgz_path)
    file_tgz.extractall(path=path)
    file_tgz.close()

def load_data(path, csv_name):
    """
    Carga el dataset con pandas
    
    path: donde se encuentra el archivo
    csv_name: nombre del archivo csv que contiene el dataset
    """
    csv_path = os.path.join(path, csv_name)
    return pd.read_csv(csv_path)

def test_set_check(identifier, test_ratio, hash):
    """
    Verifica si una instancia pertenece o no a un test_set
    Si pertenece: True
    No pertenece: False
    """
    return hash(np.int64(identifier)).digest()[-1] < 256*test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    """
    Genera test_set y train_set
    """
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]