from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Renders the "index.html" template for the chat application.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered HTML content of the "index.html" template.
    """
    return render(request, "chat/index.html")

def room(request, room_name):
    """
    Render the chat room.

    Args:
        request (HttpRequest): The request object.
        room_name (str): The name of the chat room.

    Returns:
        HttpResponse: The rendered chat room HTML.

    """
    return render(request, "chat/room.html", {"room_name": room_name})