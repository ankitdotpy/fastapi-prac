from fastapi import HTTPException

def item_not_found():
    return HTTPException(
        status_code=404,
        detail='Book can not be found',
        headers={
            'X-Header-Error':'Nothing to be seen at the UUID'
        }
    )