from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from human import Customer
class Letter:

    def __init__(self, sender: Customer, message: str, receiver: Customer):
        self._message = message
        self.receiver = receiver
        self.sender = sender
        self._is_read = False


    @property
    def is_read(self):
        return self._is_read


    def __str__(self):
        return f"From: {self.sender.name} {self.sender.address}\n {self._message} \n To: {self.receiver.name}" \
               f" {self.receiver.address}"

