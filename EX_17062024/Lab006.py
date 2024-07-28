from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def payFee(self):
        pass


class B(A):

    def payFee(self):
        print("fee done")


b = B()
b.payFee()
