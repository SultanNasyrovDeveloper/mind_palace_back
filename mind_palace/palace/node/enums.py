from mind_palace.application.enums import DjangoChoicesEnum


class NodeBodyTypeEnum(DjangoChoicesEnum):

    TEXT = 'text'
    CODE = 'code'
    CHESS = 'chess'
    TRANSLATION = 'translation'
    # MICROEXPRESSION = 'microexpression'
    # BIOGRAPHY = 'biography'
    # HISTORICAL_EVENT = 'historical_event'


class NodeMediaTypeEnum(DjangoChoicesEnum):

    NOT_SET = 'not_set'
    IMAGE = 'image'
    YOUTUBE = 'youtube'
