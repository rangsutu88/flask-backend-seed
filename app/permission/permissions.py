import logging


class Permission(object):
    @classmethod
    def validate(cls, user_id):
        # Override when subclassing to add additional checks
        raise NotImplementedError("Need to implement it in subclass!")


class AlwaysPass(Permission):
    @classmethod
    def validate(cls, user_id):
        logging.info("Pass!")
        return True


class AlwaysFail(Permission):
    @classmethod
    def validate(cls, user_id):
        logging.info("Fail!")
        return False
