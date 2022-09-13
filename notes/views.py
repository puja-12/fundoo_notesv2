from django.db import connection
from rest_framework import status
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
logger = logging.getLogger('django')



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
            cursor.execute("SELECT * FROM notes_notes ")
            data = dictfetchall(cursor)
            return Response({'message': "successfully retrieve data", "data": data}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(e)
        return Response({'success': False,
                         'message': str(e)
                         }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_queries(request):
    try:
        title, description, user = request.data.values()

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO notes_notes(title,description,user_id) VALUES('%s', '%s', '%s')" % (
            title, description, user))
            cursor.execute("SELECT * FROM notes_notes")
            data = dictfetchall(cursor)
            print(data)
            # data = list(map(lambda obj: model_to_dict(obj), query_set))

            return Response({'message': "successfully created data", "data": data}, status=status.HTTP_200_OK)

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
            description = request.data.get("description")
            cursor.execute("UPDATE notes_notes SET description ='%s' WHERE id = %s" % (description, id))
            cursor.execute("SELECT * from  notes_notes ")
            data = dictfetchall(cursor)
            print(data)

            return Response({'message': "updated successfully", "data": data}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(e)
        return Response({'success': False,
                         'message': str(e)
                         }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_queries(request):
    try:

        with connection.cursor() as cursor:
            print(request.data)
            id = request.data.get("id")
            cursor.execute("DELETE FROM  notes_notes where id = %s" % id)
            cursor.execute("SELECT * from  notes_notes ")
            data = dictfetchall(cursor)

            return Response({'message': "successfully delete data", "data": data}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.exception(e)
        return Response({'success': False,
                         'message': str(e)
                         }, status=status.HTTP_400_BAD_REQUEST)
