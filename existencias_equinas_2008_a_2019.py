# -*- coding: utf-8 -*-

# Este programa fue creado utilizado Jupyter Notebook de Google Collaboratory.

def crearDFcsv(archivo):
    from os.path import isdir # Esta forma de importar permite llamar en este caso a la función isdir, sin especificar la ruta del módulo del cual proviene.
    from pandas import read_csv
    ruta = "/content/drive/MyDrive/" # Esta variable debe ser editada para que apunte a la ruta donde se guardan los .csv para importar. En este caso se importó desde Google Drive.

    if isdir('/content/drive'):   # Con isdir se comprueba si el directorio del Drive existe, devuelve true o false, es decir si ya está vinculado el Google Drive devuelve true.
      df = read_csv(ruta + archivo + '.csv')
      return df                                #Si G.Drive ya está vinculado, toma el archivo que se le indique por parámetro y crea un Dataframe llamado df, y devuelve el mismo como resultado.

    else:   #Si el Drive no está montado, pasa a montarlo, y con las funciones importadas lo que hace es evitar mostrar el mensaje "mounted to /content/drive" que arroja la función drive.mount al completarse.
      print('Montando Drive...')
      from contextlib import redirect_stdout
      from io import StringIO

      with redirect_stdout(StringIO()):
        from google.colab.drive import mount
        mount('/content/drive')

      df = read_csv(ruta + archivo + '.csv')
      return df

# tablaventas = crearDFcsv('ventas')   # Ejemplo de creación de dataframe llamado "tablaventas" desde un csv almacenado en la carpeta especificada en la variable 'ruta'.

# Tener en cuenta que el argumento que se le pasa a la función (el nombre del archivo sin su extensión) debe estar entre comillas, para que lo tome como texto directamente.

df_caballos = crearDFcsv('ee0819')  

import pandas as pd

df_caballos_r = pd.read_csv("/content/drive/MyDrive/Archivos auxiliares Curso Python/ee0819r.csv", encoding = 'latin-1') # Este dataset (ee0819r.csv), a diferencia del anterior (ee0819.csv), contiene la información segmentada por provincia.

df_caballos.info()
df_caballos

df_caballos_r.info()
df_caballos_r

def comparar_campos(df1, df2):    # Esta función compara los encabezados de las columnas y detecta los campos comunes y no comunes al comparar dos datagrames.
    campos_df1 = tuple(df1.columns)
    campos_df2 = tuple(df2.columns)
    comunes = []
    no_comunes = []

    for i in campos_df1:
        if i in(campos_df2):
          comunes.append(i)
        else:
          no_comunes.append(i)

    for i in campos_df2:
        if i not in(comunes):
          no_comunes.append(i)

    print('Campos comunes:', comunes)
    print('\n')
    print('Campos no comunes:',no_comunes)

comparar_campos(df_caballos, df_caballos_r)

import matplotlib.pyplot as plt          # Generación de gráficos generales

plt.plot(df_caballos['indice_tiempo'], df_caballos['caballos'], color='blue', label='Caballos')
plt.xlabel('Año')
plt.ylabel('Existencias por millón')
plt.title('Existencias de caballos desde 2008 a 2019')
plt.grid()
plt.show()

plt.plot(df_caballos['indice_tiempo'], df_caballos['padrillos'], color='black', label='Padrillos')
plt.xlabel('Año')
plt.ylabel('Existencias')
plt.title('Existencias de padrillos desde 2008 a 2019')
plt.grid()
plt.show()

plt.plot(df_caballos['indice_tiempo'], df_caballos['burros_asnos'], color='orange', label='Burros / Asnos')
plt.xlabel('Año')
plt.ylabel('Existencias')
plt.title('Existencias de burros_asnos desde 2008 a 2019')
plt.grid()
plt.show()

plt.plot(df_caballos['indice_tiempo'], df_caballos['yeguas'], color='pink', label='Yeguas')
plt.xlabel('Año')
plt.ylabel('Existencias por millón')
plt.title('Existencias de yeguas desde 2008 a 2019')
plt.grid()
plt.show()

plt.plot(df_caballos['indice_tiempo'], df_caballos['mulas'], color='red', label='Mulas')
plt.xlabel('Año')
plt.ylabel('Existencias')
plt.title('Existencias de mulas desde 2008 a 2019')
plt.grid()
plt.show()


plt.plot(df_caballos['indice_tiempo'], df_caballos['potrillos_potrillas'], color='green', label='Potrillos/as')
plt.xlabel('Año')
plt.ylabel('Existencias')
plt.title('Existencias de potrillos_potrillas')
plt.grid()
plt.show()

# Se definen las regiones según la provincia a la que pertenezcan, y se agregá la información a una nueva columna en el dataframe indicado, utilizando el método apply+lambda.
Pampeana = 'Santa Fe', 'Entre Ríos', 'La Pampa', 'Córdoba', 'Buenos Aires'
Cuyo = 'Mendoza', 'San Juan', 'San Luis'
Patagonia = 'Chubut', 'Neuquén',  'Río Negro', 'Santa Cruz', 'Tierra del Fuego'
Noreste = 'Formosa', 'Chaco', 'Corrientes', 'Misiones'
Noroeste = 'Jujuy', 'Salta', 'Tucumán', 'Catamarca', 'La Rioja', 'Santiago del Estero'

df_caballos_r['Region'] = df_caballos_r['provincia'].apply(lambda x: 'Pampeana' if x in(Pampeana) else (
                                                                      'Cuyo' if x in(Cuyo) else (
                                                                        'Patagonia' if x in(Patagonia) else (
                                                                            'Noreste' if x in(Noreste) else (
                                                                                'Noroeste' if x in(Noroeste) else 'Otra')))))

df_caballos_r

import matplotlib.pyplot as plt
import pandas as pd

df_caballos_pampeana = df_caballos_r[df_caballos_r['Region'] == 'Pampeana']    # Se separa la información en distitnos datasets según región.
df_caballos_cuyo = df_caballos_r[df_caballos_r['Region'] == 'Cuyo']
df_caballos_patagonia = df_caballos_r[df_caballos_r['Region'] == 'Patagonia']
df_caballos_noroeste = df_caballos_r[df_caballos_r['Region'] == 'Noroeste']
df_caballos_noreste = df_caballos_r[df_caballos_r['Region'] == 'Noreste']

columnas_eliminar = ['provincia', 'provincia_id', 'departamento', 'departamento_id'] # selección de columnas a eliminar de los datasets 

df_caballos_pampeana = df_caballos_pampeana.drop(columns = columnas_eliminar)  # Reducción de dimensionalidad.
df_caballos_cuyo = df_caballos_cuyo.drop(columns = columnas_eliminar)
df_caballos_patagonia = df_caballos_patagonia.drop(columns = columnas_eliminar)
df_caballos_noreste = df_caballos_noreste.drop(columns = columnas_eliminar)
df_caballos_noroeste = df_caballos_noroeste.drop(columns = columnas_eliminar)

campos_comunes = ['padrillos', 'caballos', 'yeguas', 'potrillos_potrillas', 'mulas', 'burros_asnos']

df_caballos_pampeana = df_caballos_pampeana.groupby('anio')[campos_comunes].sum()   # Se agrupa la información por las columnas indicadas en la lista 'campos_comunes', para poder luego ser graficadas o analizada según la necesidad del usuario.
df_caballos_cuyo = df_caballos_cuyo.groupby('anio')[campos_comunes].sum()
df_caballos_patagonia = df_caballos_patagonia.groupby('anio')[campos_comunes].sum()
df_caballos_noreste = df_caballos_noreste.groupby('anio')[campos_comunes].sum()
df_caballos_noroeste = df_caballos_noroeste.groupby('anio')[campos_comunes].sum()

# A continuación se grafican las existencias de mulas comparando la región Noroeste y la región Patagonia.

plt.plot(df_caballos_noroeste.index, df_caballos_noroeste['mulas'], color='orange', label='Noroeste') 
plt.plot(df_caballos_noroeste.index, df_caballos_patagonia['mulas'], color='blue', label='Patagonia')
plt.xlabel('Año')
plt.ylabel('Existencias')
plt.title('Existencias de mulas desde 2008 a 2019, por región')
plt.legend(loc='upper right', bbox_to_anchor=(1.4, 1))
plt.grid()
plt.show()

# Analizando los gráficos, se observa una gran diferencia, siendo mucho mayor la existencia de mulas en la región Noroeste, lo cual es razonable, ya que en dichas zonas
# la mula es más utilizada y más demandada que cualquier otro tipo de equino, debido a su mayor resistencia, heredada de la cruza entre un asno y una yegua.
# Por último, se presenta la misma información pero en formáto texto, con datos numéricos específicos.

print('Región Noroeste:')
print(df_caballos_noroeste['mulas'])
print('\nRegión Patagonia:')
print(df_caballos_patagonia['mulas'])
