import requests


import os

def getData() -> str:

    """Obtém os dados de Kepler Objects of Interest (KOI), a partir da API da exoplanetarchive

    Returns
    -------
     str
      Conteúdo do corpo do endpoint da API, no formato de um arquivo csv

    """

    URL = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI"
    params = {
        "table": "cumulative"
    }

    response = requests.request(method="GET", url=URL, params=params)

    if response.status_code == 200:

        data = response.content.decode(response.encoding)

        return data
    
    else:
         
        return None


def saveData() -> None:

    """Salva os dados da API em um arquivo csv
    """

    data = getData()

    if data:

        DATA_DIRPATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                    "data")
        
        FILEPATH = os.path.join(DATA_DIRPATH, "koi_data.csv")

        with open(FILEPATH, "w") as file_stream:

            file_stream.write(data)
        
        print(f"Arquivo salvo em {FILEPATH}")
    
    else:

        print("Houve algum problema!")

if __name__ == "__main__":

    saveData()