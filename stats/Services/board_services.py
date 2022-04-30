from stats.serializers import BoardSerializer, RecordsSerializer
from stats.models.models import Board, Records
from rest_framework import status
import datetime
import json
from django.db import transaction


class BoardService:
    @transaction.atomic()
    def set_board_and_records(self, request: dict, create_user: str) -> str:
        datetime_now = datetime.datetime.now()
        request['board']['create_user'] = create_user
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

    def get_board_list(self, request: dict) -> str:
        board = Board.objects
        if 'start_date' in request.keys():
            board = board.filter(create_datetime__range=[request['start_date'], request['end_date']])
        board_list = board.filter(delete_yn='n', create_user=request['create_user']).values()
        return board_list

    def get_board_detail(self, pk: int) -> str:
        board_detail = Board.objects.values().get(board_id=pk)
        record_detail = Records.objects.values().get(board=pk)
        result = {
            'board': board_detail,
            'record': record_detail
        }
        return result

    def delete_board(self, pk: int) -> str:
        try:
            board_instance = Board.objects.get(board_id=pk)
            board_instance.delete_yn = 'y'
            board_instance.save()
            return {'status': status.HTTP_200_OK}
        except:
            raise ValueError('삭제에 실패하였습니다.')

    def update_board(self, request: dict, pk: int, update_user: str) -> str:
        datetime_now = datetime.datetime.now()
        board_object = Board.objects.get(board_id=pk)
        record_object = Records.objects.get(board=pk)
        request['board']['update_user'] = update_user
        request['board']['update_datetime'] = datetime_now
        board_serializer = BoardSerializer(board_object, data=request['board'])

        if board_serializer.is_valid():
            board = board_serializer.save()
            board_id = board.pk
            request['records']['board'] = board_id
            records_serializer = RecordsSerializer(record_object, data=request['records'])
            if records_serializer.is_valid():
                records = records_serializer.save()

                return {
                    'board_id': records.board_id,
                    'status': status.HTTP_200_OK
                }
            return records_serializer.errors
        return board_serializer.errors
