from mind_palace_back.application.enums import DjangoChoicesEnum


class NodeBodyTypeEnum(DjangoChoicesEnum):

    TEXT = 'text'
    CODE = 'code'
    CHESS = 'chess'
    TRANSLATION = 'translation'
    MICROEXPRESSION = 'microexpression'
