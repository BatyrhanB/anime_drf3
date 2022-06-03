
def get_user_data_middleware(get_response):

    def middleware(request):
        response = get_response(request)
        print(request.user.id)
        return response
    return middleware

