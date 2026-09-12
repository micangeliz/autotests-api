from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
import uuid


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def get_user_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))  # генерирует uuid 4 версии и возвращает строку
    title: str = "Playwright"
    max_score: int = 1000
    min_score: int = 100
    estimated_time: str = "1 week"
    description: str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")

    # max_score : int = Field(alias='maxScore', default = 1000) - явно прописанные алиасы
    # min_score : int = Field(alias='minScore')
    # estimated_time: str = Field(alias='estimatedTime')


course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week",
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses"
    ),
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice"
    )
)
print("Course default model:", course_default_model)

# Инициализация на основе словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
}
course_dict_model = CourseSchema(**course_dict)
print("Course dict model:", course_dict_model)

# Инициализация на основе json-строки
course_json = """
    {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 1000,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
    }
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print("Course JSON model:", course_json_model)
print(course_json_model.model_dump(by_alias=True))  # сериализация модели в словарь
print(course_json_model.model_dump_json(by_alias=True))  # сериализация модели в json

user = UserSchema(
    id="user-id",
    email="user@gmail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alice"
)
print(user.get_user_name(), user.username)

try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses"
    )
except ValidationError as error:
    print(error)
    print (error.errors())
