from mind_palace_back.application.enums import DjangoChoicesEnum


class UserLearningSessionStatusEnum(DjangoChoicesEnum):

    active = 'active'
    finished = 'finished'
