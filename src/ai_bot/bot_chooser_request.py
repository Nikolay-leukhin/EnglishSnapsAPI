class RequestChooser:

    @staticmethod
    def get_response(response):
        return response.get('choices')[0].get('message').get('content')
