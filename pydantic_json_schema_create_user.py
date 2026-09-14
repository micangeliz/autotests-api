from tools.assertions.schema import validate_json_schema
import jsonschema
from clients.users.public_users_client import get_public_users_client
from tools.fakers import get_random_email
from clients.users.public_users_client import CreateUserRequestSchema, CreateUserResponseSchema

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

#del create_user_response_json['user']['email'] - чтобы проверить валидацию, что-то удалить
jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_schema)
validate_json_schema (instance=create_user_response.json(), schema=create_user_response_schema)
