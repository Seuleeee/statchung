from drf_yasg import openapi

board_get_list_params = [
    openapi.Parameter(
        'start_date',
        openapi.IN_QUERY,
        description="test manual param",
        type=openapi.FORMAT_DATE
    ),
    openapi.Parameter(
        'end_date',
        openapi.IN_QUERY,
        description="test manual param",
        type=openapi.FORMAT_DATE
    ),
]

board_post_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'board': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'comment': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'likes': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }),
        'records': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
            'duration': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            'position': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            "scores": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "rebounds": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "offensive_rebounds": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "assists": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "screen_assists": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "good_screens": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "blockshots": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "threepoints": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "hustle_plays": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "memo": openapi.Schema(type=openapi.TYPE_STRING, description='string')
        }),
    }
)

board_put_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'board': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'comment': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'likes': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }),
        'records': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
            'duration': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            'position': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            "scores": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "rebounds": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "offensive_rebounds": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "assists": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "screen_assists": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "good_screens": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "blockshots": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "threepoints": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "hustle_plays": openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
            "memo": openapi.Schema(type=openapi.TYPE_STRING, description='string')
        }),
    }
)
