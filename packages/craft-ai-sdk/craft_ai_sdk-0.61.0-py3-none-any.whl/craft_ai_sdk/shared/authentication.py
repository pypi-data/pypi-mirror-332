import functools
from datetime import datetime


def use_authentication(action_func):
    @functools.wraps(action_func)
    def wrapper(sdk, *args, headers=None, **kwargs):
        actual_headers = None
        if (
            sdk._access_token_data is None
            or sdk._access_token_data["exp"]
            < (datetime.now() + sdk._access_token_margin).timestamp()
        ):
            sdk._refresh_access_token()
        actual_headers = {"Authorization": f"Bearer {sdk._access_token}"}
        if headers is not None:
            actual_headers.update(headers)

        response = action_func(sdk, *args, headers=actual_headers, **kwargs)
        if response.status_code == 401:
            sdk._clear_access_token()
        return response

    return wrapper
