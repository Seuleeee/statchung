from stats.serializers import BoardSerializer, RecordsSerializer
from stats.models.models import Board, Records
from rest_framework import status
import datetime
import json
from django.db import transaction


class BoardService:
    @transaction.atomic()
    def set_board_and_records(self, request: dict) -> str:
        datetime_now = datetime.datetime.now()
        request['board']['create_user'] = 'hsjo'
        request['board']['create_datetime'] = datetime_now
        board_serializer = BoardSerializer(data=request['board'])

        if board_serializer.is_valid():
            board = board_serializer.save()
            board_id = board.pk
            request['records']['board'] = board_id
            records_serializer = RecordsSerializer(data=request['records'])
            if records_serializer.is_valid():
                records = records_serializer.save()

                return {
                    'board_id': records.board_id,
                    'status': status.HTTP_201_CREATED
                }
            return records_serializer.errors
        return board_serializer.errors
