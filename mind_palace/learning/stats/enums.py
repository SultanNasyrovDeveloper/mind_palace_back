from mind_palace.application.enums import DjangoChoicesEnum


class UserNodeLearningStatusEnum(DjangoChoicesEnum):

    rookie = 'rookie'
    middle = 'middle'
    senior = 'senior'
