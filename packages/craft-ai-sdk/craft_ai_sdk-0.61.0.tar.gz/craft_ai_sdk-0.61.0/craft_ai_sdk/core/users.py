from ..sdk import BaseCraftAiSdk


def get_user(sdk: BaseCraftAiSdk, user_id):
    """Get information about a user.

    Args:
        user_id (:obj:`str`): The id of the user.

    Returns:
        :obj:`dict`: The user information, with the following keys:

          * ``id`` (:obj:`str`): id of the user.
          * ``name`` (:obj:`str`): Name of the user.
          * ``email`` (:obj:`str`): Email of the user.

    """

    url = f"{sdk.base_control_api_url}/users/{user_id}"

    return sdk._get(url)
