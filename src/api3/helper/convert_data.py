"""
Convert data
------------
Archivo encargado de darle un formato establecido de json, el cual se describe a continuación::
    | {
    |   'code': Codigo error o Aprobatorio
    |   'data': lista de valores con el json de los datos
    |   'message': Sucess - Fail
    | } 
"""
import json
def sendResJson(data, code):
    """Método encargada de Mapear los datos a un json estandarizado

    Parameters
    ----------
    data : list
        lista de datos recibidos de una consulta, ésta puede estar vacía
    code : int
            | 200 -> Satisfactorio.
            | 404 -> No Encontrado.
            | Cualquier otro, dará fail

    Returns
    -------
    JSON
        Json de respuesta
    """
    if code == 200:
        return json.dumps(
            {
                'code': code,
                'data':data
            }
        )
    if code == 404:
        return json.dumps(
            {
                'code': code,
                'message': "Not Found"
            }
        )
    else:
        return json.dumps(
            {
                'code': code,
                'message': "Error!"
            }
        )