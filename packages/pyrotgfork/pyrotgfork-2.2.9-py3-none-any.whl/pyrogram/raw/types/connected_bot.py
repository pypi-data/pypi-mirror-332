#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ConnectedBot(TLObject):  # type: ignore
    """Contains info about a connected business bot ».

    Constructor of :obj:`~pyrogram.raw.base.ConnectedBot`.

    Details:
        - Layer: ``200``
        - ID: ``BD068601``

    Parameters:
        bot_id (``int`` ``64-bit``):
            ID of the connected bot

        recipients (:obj:`BusinessBotRecipients <pyrogram.raw.base.BusinessBotRecipients>`):
            Specifies the private chats that a connected business bot » may receive messages and interact with.

        can_reply (``bool``, *optional*):
            Whether the the bot can reply to messages it receives through the connection

    """

    __slots__: list[str] = ["bot_id", "recipients", "can_reply"]

    ID = 0xbd068601
    QUALNAME = "types.ConnectedBot"

    def __init__(self, *, bot_id: int, recipients: "raw.base.BusinessBotRecipients", can_reply: Optional[bool] = None) -> None:
        self.bot_id = bot_id  # long
        self.recipients = recipients  # BusinessBotRecipients
        self.can_reply = can_reply  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConnectedBot":
        
        flags = Int.read(b)
        
        can_reply = True if flags & (1 << 0) else False
        bot_id = Long.read(b)
        
        recipients = TLObject.read(b)
        
        return ConnectedBot(bot_id=bot_id, recipients=recipients, can_reply=can_reply)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_reply else 0
        b.write(Int(flags))
        
        b.write(Long(self.bot_id))
        
        b.write(self.recipients.write())
        
        return b.getvalue()
