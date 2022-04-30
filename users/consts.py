REG_USER_ID = r'^(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$'
REG_PASSWORD = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,20}$'
REG_PHONE = r'^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$'
REG_EMAIL = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
REG_NICKNAME = r'^(?=[가-힣a-zA-Z0-9._]{4,20}$)(?!.*[_.]{2})[^_.].*[^_.]$'