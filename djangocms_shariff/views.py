import json
import requests

from django.http import JsonResponse
from django.views.generic import TemplateView


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        url = self.request.GET.get('url')
        counts = {}
        if url:
            twitter = self.twitter_count(url)
            if twitter:
                counts['twitter'] = twitter
            facebook = self.facebook_count(url)
            if facebook:
                counts['facebook'] = facebook
            flattr = self.flattr_count(url)
            if flattr:
                counts['flattr'] = flattr
            google_plus = self.google_plus_count(url)
            if google_plus:
                counts['googleplus'] = google_plus
            linkedin = self.linkedin_count(url)
            if linkedin:
                counts['linkedin'] = linkedin
            xing = self.xing_count(url)
            if xing:
                counts['xing'] = xing
            pinterest = self.pinterest_count(url)
            if pinterest:
                counts['pinterest'] = pinterest

        return counts

    def twitter_count(self, url):
        twitter_url = 'http://urls.api.twitter.com/1/urls/count.json?url='
        response = requests.get(twitter_url + url)
        if response.status_code == 200 and u'count' in response.json().keys():
            return response.json()['count']

    def facebook_count(self, url):
        facebook_url = 'https://api.facebook.com/method/fql.query?format=json'
        facebook_url += '&query=select share_count from link_stat where url=\"'
        response = requests.get(facebook_url + url + '\"')
        if (
                response.status_code == 200 and
                len(response.json()) and
                u'share_count' in response.json()[0].keys()
            ):
            return response.json()[0]['share_count']

    def flattr_count(self, url):
        flattr_url = 'https://api.flattr.com/rest/v2/things/lookup/?url='
        response = requests.get(flattr_url + url)
        if response.status_code == 200 and u'flattrs' in response.json().keys():
            return response.json()['flattrs']

    def google_plus_count(self, url):
        google_plus_url = 'https://clients6.google.com/rpc?key=AIzaSyCKSbrvQasunBoV16zDH9R33D88CeLr9gQ'
        if url[:4] != 'http':
            url = 'http://' + url
        payload = {
            'method': 'pos.plusones.get',
            'params': {
                'nolog': True,
                'id': url,
                'source': 'widget',
                'userId': '@viewer',
                'groupId': '@serf'
            },
            'jsonrpc': '2.0',
            'key': 'p',
            'apiVersion': 'v1'
        }
        response = requests.post(google_plus_url, json=payload)
        resp_json = response.json()
        if (
            response.status_code == 200 and
            'error' not in resp_json.keys() and
            'count' in resp_json['result']['metadata']['globalCounts'].keys()
            ):
            return resp_json['result']['metadata']['globalCounts']['count']

    def linkedin_count(self, url):
        linkedin_url = 'https://www.linkedin.com/countserv/count/share?url='
        response = requests.get(linkedin_url + url + '&lang=de_DE&format=json')
        if response.status_code == 200 and u'count' in response.json().keys():
            return response.json()['count']

    def xing_count(self, url):
        xing_url = 'https://www.xing-share.com/spi/shares/statistics'
        payload = {'url': url}
        response = requests.post(xing_url, data=payload)
        if (
                response.status_code == 200 and
                'share_counter' in response.json().keys()
            ):
            return int(response.json()['share_counter'])

    def pinterest_count(self, url):
        pinterest_url = 'http://api.pinterest.com/v1/urls/count.json?callback=_&url='
        if url[:4] != 'http':
            url = 'http://' + url
        response = requests.get(pinterest_url + url)
        json_response = json.loads(response.text[2:-1])
        if response.status_code == 200 and u'count' in json_response.keys():
            return json_response['count']


class DataBackendView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
