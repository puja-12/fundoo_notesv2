from django.db import connection
from rest_framework import generics,status
import logging

from rest_framework.decorators import api_view
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


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@api_view(["GET"])
def read_queries(request):

    try:

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM notes_notes where id= 2")
            data = dictfetchall(cursor)




            return Response({'message': "successfully retrieve data", "data": data},status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(e)
        return Response({'success': False,
                         'message': str(e)
                         }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_queries(request):

    try:

        with connection.cursor() as cursor:
            cursor.execute("INSERT into notes_notes values"
                           " ('Colours','I Like Blue',1)")

            r = cursor.fetchone()
            print(r)

            print(connection.queries)

            return Response({'message': "successfully created  data", "data": r},status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(e)
        return Response({'success': False,
                         'message': str(e)
                         }, status=status.HTTP_400_BAD_REQUEST)



@api_view(["PUT"])
def update_queries(request):

    try:

        with connection.cursor() as cursor:
            print(request.data)
            id = request.data.get("id")
            title= request.data.get("title")
            cursor.execute("UPDATE notes_notes SET title = %s where id = %s" % (title,id))
            # cursor.execute("SELECT * from  notes_notes WHERE id = %s" % id)
            print(dir())


            r = cursor.fetchone()
            print(r)

            return Response({'message': " update successfully ", "data": r},status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(e)
        return Response({'success': False,
                         'message': str(e)
                         }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_queries(request):

    try:

        with connection.cursor() as cursor:

            id = request.data.get("id")
            cursor.execute("DELETE from notes_notes WHERE id= %s" % id)

            r = cursor.fetchone()
            print(r)

            return Response({'message': "successfully delete data","data": r},status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(e)
        return Response({'success': False,
                         'message': str(e)
                         }, status=status.HTTP_400_BAD_REQUEST)




