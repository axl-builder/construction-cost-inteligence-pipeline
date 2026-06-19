# Import modules
import requests
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv

# Import or assign API key
ruta_env = find_dotenv()
print(f"Ruta definida: {ruta_env}, cargando API_KEY...")
load_dotenv(ruta_env)

OBS_ENDPOINT = "series/observations"


class FredAPIClient:
    def __init__(self):
        # 1. Carga tu API Key usando os.getenv('FRED_API_KEY')
        self.api_key = os.getenv('FRED_API_KEY')

        if not self.api_key:
            raise ValueError("FRED_API_KEY no encontrada en las variables de entorno.")

        # 2. Configura tu URL base aquí.
        # URL Base: El cimiento de todas las llamadas a la API
        self.base_url = 'https://api.stlouisfed.org/fred/'

        # 3. Inicializa una sesión: self.session = requests.Session()
        self.session = requests.Session()

    def _make_request(self, endpoint, additional_params=None):
        """Método interno para centralizar peticiones"""

        # 1. Arma tus parámetros base (api_key y file_type)
        params = {
            'api_key': self.api_key, # ¡Nota el self!
            'file_type': 'json'
        }

        # 2. Actualiza el diccionario params si hay additional_params
        if additional_params:
            params.update(additional_params)

        # 3. Construye la url concatenando self.base_url + endpoint
        url = self.base_url + endpoint

        # 4. Usa self.session.get(url, params=params) para hacer la petición
        response = self.session.get(url, params=params, timeout=10)  # timeout opcional para evitar bloqueos prolongados

        # 5. Valida el status_code (200) y devuelve response.json()
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error en la petición: {response.status_code} - {response.text}")

    def get_series_observations(self, series_id, start_date=None, end_date=None):
        """
        Obtiene las observaciones de una serie específica y devuelve un DataFrame limpio.
        """
        endpoint = 'series/observations'

        # 1. Arma el diccionario de parámetros específicos para esta llamada
        # Siempre necesitamos el 'series_id'. 
        params = {
            'series_id': series_id,
        }

        # Agregamos las fechas solo si el usuario las proporcionó
        if start_date:
            params['observation_start'] = start_date
        if end_date:
            params['observation_end'] = end_date

        # 2. Usa tu motor interno para traer los datos crudos (JSON)
        raw_data = self._make_request(endpoint, additional_params=params)

        # 3. Transforma los datos con Pandas
        df = pd.DataFrame(raw_data['observations'])
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)

        # Opcional pero recomendado: FRED devuelve los valores como texto.
        df['value'] = pd.to_numeric(df['value'], errors='coerce') 

        # 4. Retorna el DataFrame limpio
        return df
    
    def get_series(self, series_id, start_date=None, end_date=None):
        """
        Obtiene las observaciones de una serie específica y devuelve un DataFrame limpio.
        """
        endpoint = 'series'

        # 1. Arma el diccionario de parámetros específicos para esta llamada
        # Siempre necesitamos el 'series_id'. 
        params = {
            'series_id': series_id,
        }

        # Agregamos las fechas solo si el usuario las proporcionó
        if start_date:
            params['realtime_start'] = start_date
        if end_date:
            params['realtime_end'] = end_date

        # 2. Usa tu motor interno para traer los datos crudos (JSON)
        raw_data = self._make_request(endpoint, additional_params=params)

        # 3. Transforma los datos con Pandas
        df = pd.DataFrame(raw_data['seriess'])

        columnas_importantes = [
            'id', 
            'title', 
            'frequency', 
            'units', 
            'observation_start', 
            'observation_end'
        ]

        df_filtrado = df[columnas_importantes]

        # 4. Retorna el DataFrame limpio
        return df_filtrado
    
    def get_release_dates(self, release_id):
        """
        Método adicional para obtener las fechas de lanzamiento de una serie.
        """
        endpoint = 'release/dates'
        params = {
            'release_id': release_id,
        }
        raw_data = self._make_request(endpoint, additional_params=params)
        df = pd.DataFrame(raw_data['release_dates'])
        df['release_date'] = pd.to_datetime(df['date'])
        return df
    
    def get_sources(self, source_id):
        """
        Método adicional para obtener las fechas de lanzamiento de una serie.
        """
        endpoint = 'source'
        params = {
            'source_id': source_id,
        }
        raw_data = self._make_request(endpoint, additional_params=params)
        df = pd.DataFrame(raw_data['sources'])
        return df
    


cliente = FredAPIClient()

df_observations = cliente.get_series_observations('PIORECRUSDM', start_date='2020-01-01')
df_release_dates = cliente.get_release_dates('365')
df_series = cliente.get_series('PIORECRUSDM')
df_sources = cliente.get_sources('1')


print(f"\n{df_series['title'].iloc[0].upper()}\n")  # Imprime el título de la serie para verificar que se obtuvo correctamente
print(f"Observations: \n {df_observations}\n")
print(f"Release Dates: \n {df_release_dates}\n")
print(f"Series: \n {df_series}\n")
print(f"Sources: \n {df_sources}\n")

