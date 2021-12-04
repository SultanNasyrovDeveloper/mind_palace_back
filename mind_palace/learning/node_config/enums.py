from mind_palace.application.enums import DjangoChoicesEnum


class LearningCardField(DjangoChoicesEnum):

    name = 'name'
    description = 'title'
    body = 'body'
    media = 'media'