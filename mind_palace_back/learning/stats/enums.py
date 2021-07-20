from mind_palace_back.application.enums import DjangoChoicesEnum


class UserNodeLearningStatusEnum(DjangoChoicesEnum):

    rookie = 'rookie'
    middle = 'middle'
    senior = 'senior'
