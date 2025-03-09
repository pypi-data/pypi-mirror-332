
class EntityMetas:
    # 框架版本号
    META_SOCKETD_VERSION = "Socket.D"
    # 发起端真实IP
    META_X_IP = "X-IP"
    # 负载均衡哈希
    META_X_HASH = "X-Hash"
    # 不限制流量
    META_X_UNLIMITED = "X-Unlimited"
    # 数据长度
    META_DATA_LENGTH = "Data-Length"
    # 数据类型
    META_DATA_TYPE = "Data-Type"
    # 数据分片索引
    META_DATA_FRAGMENT_IDX = "Data-Fragment-Idx"
    # 数据分片总数
    META_DATA_FRAGMENT_TOTAL = "Data-Fragment-Total"
    # 数据描述之文件名
    META_DATA_DISPOSITION_FILENAME = "Data-Disposition-Filename"
    # 数据范围开始（相当于分页）
    META_RANGE_START = "Data-Range-Start"
    # 数据范围长度
    META_RANGE_SIZE = "Data-Range-Size"