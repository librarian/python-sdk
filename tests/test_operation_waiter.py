import time

from nebiusai._operation_waiter import OperationWaiter


class _OperationMock:
    def __init__(self, done):
        self.id = "some_id"
        self.status = done
        self.finished_at = type("FinishedAt", (), {"seconds": 0})
        if done:
            self.finished_at = type("FinishedAt", (), {"seconds": 1})


class _WaitTenIterations:
    def __init__(self):
        self.__get_count = 0

    def Get(self, id):
        self.__get_count += 1
        return _OperationMock(done=self.__get_count > 10)


def test_ten_iterations():
    waiter = OperationWaiter("", _WaitTenIterations())

    count = 0
    for _ in waiter:
        count += 1

    assert waiter.done is True
    assert count == 10


class _NeverDone:
    def Get(self, id):
        return _OperationMock(done=False)


def test_timeout():
    waiter = OperationWaiter("", _NeverDone(), timeout=10)

    for _ in waiter:
        time.sleep(1)

    assert waiter.done is False
