"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class crazyflie_imu_t(object):
    __slots__ = ["timestamp", "omegax", "omegay", "omegaz", "alphax", "alphay", "alphaz", "dt"]

    def __init__(self):
        self.timestamp = 0
        self.omegax = 0.0
        self.omegay = 0.0
        self.omegaz = 0.0
        self.alphax = 0.0
        self.alphay = 0.0
        self.alphaz = 0.0
        self.dt = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(crazyflie_imu_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qddddddd", self.timestamp, self.omegax, self.omegay, self.omegaz, self.alphax, self.alphay, self.alphaz, self.dt))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != crazyflie_imu_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return crazyflie_imu_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = crazyflie_imu_t()
        self.timestamp, self.omegax, self.omegay, self.omegaz, self.alphax, self.alphay, self.alphaz, self.dt = struct.unpack(">qddddddd", buf.read(64))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if crazyflie_imu_t in parents: return 0
        tmphash = (0x62771ba32598e0f7) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if crazyflie_imu_t._packed_fingerprint is None:
            crazyflie_imu_t._packed_fingerprint = struct.pack(">Q", crazyflie_imu_t._get_hash_recursive([]))
        return crazyflie_imu_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

