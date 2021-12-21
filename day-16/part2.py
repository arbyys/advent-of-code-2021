from aocd import get_data

data = get_data(day=16, year=2021)

data = format(int(data, 16), "0{}b".format(len(data)*4))
index = 0
depth = 0
lastPacketType = "" # o / l

packets = {}

class Packet:
    def __init__(self, version, type, value, lengthTypeID, length):
        self.version = version
        self.type = type
        self.value = value
        self.lengthTypeID = lengthTypeID
        self.length = length
    def __str__(self):
        return "{} packet, version {}, value {}, lengthTypeID {}, length {}".format("Literal" if self.type == 4 else "Operational", self.version, self.value, self.lengthTypeID, self.length)


while True:
    if("".join(set(data)) == "0"):
        break
    version = int(data[:3], 2)
    type = int(data[3:6], 2)
    currentPacketType = "l" if type == 4 else "o"
    data = data[6:]
    if(type == 4): # literal
        binaryValue = ""
        length = 0
        lengthTypeID = 0
        runLiteralScan = True
        while runLiteralScan:
            if(int(data[0]) == 0):
                runLiteralScan = False
            data = data[1:]
            binaryValue += str(data[:4])
            data = data[4:]
        value = int(binaryValue, 2)
    else: # operational
        lengthTypeID = int(data[0])
        data = data[1:]
        value = 0
        if(lengthTypeID == 0):
            length = data[:15]
            data = data[15:]
        elif(lengthTypeID == 1):
            length = data[:11]
            data = data[11:]
    if((currentPacketType == "o" and lastPacketType == "o") or (currentPacketType == "l" and lastPacketType == "o")):
        depth += 1
    elif(currentPacketType == "o" and lastPacketType == "l"):
            depth -= 1

    currentPacket = Packet(version, type, value, lengthTypeID, length)
    if(depth not in packets):
        packets[depth] = [currentPacket]
    else:
        packets[depth].append(currentPacket)

    lastPacketType = currentPacketType

versionSum = 0
for depth, packetList in packets.items():
  for packet in packetList:
      versionSum += packet.version

print(versionSum)
