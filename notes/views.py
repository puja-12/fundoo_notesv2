from rest_framework import generics,status
import logging
from rest_framework.response import Response
from notes.models import Notes
from notes.serializers import NotesSerializer
logger = logging.getLogger('django')

class ListAPIView(generics.ListAPIView):
    """
    API for creating Notes and performing all CRUD operation
    """
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()



class CreateAPIView(generics.CreateAPIView):

    serializer_class = NotesSerializer
    queryset = Notes.objects.all()


class UpdateNotesAPIView(generics.UpdateAPIView):
    """
    API for updating notes
    """
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()

    def get_objects(self, pk):
        """
        function for get the note id for updating
        """
        try:
            return Notes.objects.get(pk=pk)
        except Exception as e:
            return Response({'success': False,
                             'message': f"Something Went Wrong {e}",
                             }, status=status.HTTP_400_BAD_REQUEST)

class RetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    """
       API for updating notes
    """

    serializer_class = NotesSerializer
    queryset = Notes.objects.all()


    def get_objects(self, pk):
        """
        function for get the note id for updating
        """
        try:
            return Notes.objects.get(pk=pk)
        except Exception as e:
            return Response({'success': False,
                             'message': f"Something Went Wrong {e}",
                             }, status=status.HTTP_400_BAD_REQUEST)






