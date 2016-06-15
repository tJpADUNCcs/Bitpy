import hashlib
from Utils.dataTypes import *

class PacketCreator():
    def __init__(self, payload):
        self.payload = payload.forge()  # The message payload forged

        #create the header
        self.magic = to_hexa("F9BEB4D9")  # The Magic number of the Main network -> This message will be accepted by the main network
        self.command = self.command_padding(payload.command_name)
        self.length = to_uint32(len(self.payload))
        self.checksum = self.get_checksum()

    def command_padding(self,command):  # The message command should be padded to be 12 bytes long.
        command = command + (12 - len(command)) * "\00"
        return command

    def get_checksum(self):
        check = hashlib.sha256(hashlib.sha256(self.payload).digest()).digest()[:4]
        return check

    def forge_header(self):
        return self.magic + self.command + self.length + self.checksum

    def forge_packet(self):
        return self.forge_header() + self.payload
