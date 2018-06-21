import simplejson

from django.urls import reverse


def get_login_params_dict(client, login_params):
    """
    Returns dict with params which needed for unit tests to login with api point
    """

    user_login_url = reverse('token_obtain_pair')

    resp_login = simplejson.loads(client.post(user_login_url, login_params).content)

    token = "Bearer {}".format(resp_login.get('access'))
    return {'content_type': 'application/json', 'HTTP_AUTHORIZATION': token}
