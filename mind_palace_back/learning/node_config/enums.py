from mind_palace_back.application.enums import DjangoChoicesEnum


class LearningCardField(DjangoChoicesEnum):

    name = 'name'
    description = 'title'
    body = 'body'
    media = 'media'