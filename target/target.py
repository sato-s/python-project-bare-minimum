# -*- coding: utf-8 -*-
class Target:
    @property
    def token(self):
        return 'aaa'

    @property
    def token2(self):
        return '2nd '+self.token


if __name__ == '__main__':
    print Target().token # pragma: no cover

