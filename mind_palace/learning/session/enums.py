from mind_palace.application.enums import DjangoChoicesEnum


class UserLearningSessionStatusEnum(DjangoChoicesEnum):

    active = 'active'
    finished = 'finished'
