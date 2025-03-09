"""
枚举类型定义，从 market_data.proto 中导出
"""

from enum import Enum, IntEnum

# 从 proto 文件中导入枚举类型
from .proto.market_data_pb2 import (
    TransFlagEnum,
    TrdBSFlag,
    DirectionEnum,
    OrdActionEnum,
    TickStatusFlagEnum
)

# 交易标志枚举
class TransFlag(IntEnum):
    """逐笔行情数据标识"""
    ALONE = TransFlagEnum.TF_Alone    # 逐笔独立编号
    UNIFIED = TransFlagEnum.TF_Unified  # 逐笔统一编号

    def __str__(self):
        return {
            TransFlag.ALONE: f"逐笔独立编号({self.name}={self.value})",
            TransFlag.UNIFIED: f"逐笔统一编号({self.name}={self.value})"
        }[self]

    @classmethod
    def _missing_(cls, value):
        """处理无效的枚举值"""
        return cls.ALONE  # 返回默认值

class TrdType(IntEnum):
    """交易类型"""
    UNKNOWN = TrdBSFlag.TT_UNKNOWN  # 未知
    BUY = TrdBSFlag.TT_BUY          # SH.主动买
    SELL = TrdBSFlag.TT_SELL        # SH.主动卖
    CANCEL = TrdBSFlag.TT_CANCEL    # SZ.撤单
    DEAL = TrdBSFlag.TT_DEAL        # SZ.成交

    def __str__(self):
        return {
            TrdType.UNKNOWN: f"未知({self.name}={self.value})",
            TrdType.BUY: f"主动买({self.name}={self.value})",
            TrdType.SELL: f"主动卖({self.name}={self.value})",
            TrdType.CANCEL: f"撤单({self.name}={self.value})",
            TrdType.DEAL: f"成交({self.name}={self.value})"
        }[self]

    @classmethod
    def _missing_(cls, value):
        """处理无效的枚举值"""
        return cls.UNKNOWN  # 返回默认值

# 交易方向枚举
class Direction(IntEnum):
    """交易方向"""
    UNKNOWN = DirectionEnum.DIR_UNKNOWN  # 未知
    BUY = DirectionEnum.DIR_BUY          # 买单
    SELL = DirectionEnum.DIR_SELL        # 卖单

    def __str__(self):
        return {
            Direction.UNKNOWN: f"未知({self.name}={self.value})",
            Direction.BUY: f"买入({self.name}={self.value})",
            Direction.SELL: f"卖出({self.name}={self.value})"
        }[self]

    @classmethod
    def _missing_(cls, value):
        """处理无效的枚举值"""
        return cls.UNKNOWN  # 返回默认值

class OrdAction(IntEnum):
    """订单操作类型"""
    UNKNOWN = OrdActionEnum.OT_UNKNOWN  # 未知
    ADD = OrdActionEnum.OT_ADD          # SH.增加订单
    DELETE = OrdActionEnum.OT_DELETE    # SH.删除订单
    STATUS = OrdActionEnum.OT_STATUS    # SH.产品状态订单
    MARKET = OrdActionEnum.OT_MARKET    # SZ.市价委托
    LIMIT = OrdActionEnum.OT_LIMIT      # SZ.限价委托
    BFZY = OrdActionEnum.OT_BFZY        # SZ.本方最优

    def __str__(self):
        return {
            OrdAction.UNKNOWN: f"未知({self.name}={self.value})",
            OrdAction.ADD: f"增加订单({self.name}={self.value})",
            OrdAction.DELETE: f"删除订单({self.name}={self.value})",
            OrdAction.STATUS: f"产品状态订单({self.name}={self.value})",
            OrdAction.MARKET: f"市价委托({self.name}={self.value})",
            OrdAction.LIMIT: f"限价委托({self.name}={self.value})",
            OrdAction.BFZY: f"本方最优({self.name}={self.value})"
        }[self]

    @classmethod
    def _missing_(cls, value):
        """处理无效的枚举值"""
        return cls.UNKNOWN  # 返回默认值

class TickStatusFlag(IntEnum):
    """行情状态标志"""
    UNKNOWN = TickStatusFlagEnum.TSF_UNKNOWN  # 未知
    ADD = TickStatusFlagEnum.TSF_ADD          # 产品未上市
    START = TickStatusFlagEnum.TSF_START      # 启动
    OCALL = TickStatusFlagEnum.TSF_OCALL      # 开市集合竞价
    TRADE = TickStatusFlagEnum.TSF_TRADE      # 连续自动撮合
    SUSP = TickStatusFlagEnum.TSF_SUSP        # 停牌
    CCALL = TickStatusFlagEnum.TSF_CCALL      # 收盘集合竞价
    CLOSE = TickStatusFlagEnum.TSF_CLOSE      # 闭市
    ENDTR = TickStatusFlagEnum.TSF_ENDTR      # 交易结束

    def __str__(self):
        return {
            TickStatusFlag.UNKNOWN: f"未知({self.name}={self.value})",
            TickStatusFlag.ADD: f"产品未上市({self.name}={self.value})",
            TickStatusFlag.START: f"启动({self.name}={self.value})",
            TickStatusFlag.OCALL: f"开市集合竞价({self.name}={self.value})",
            TickStatusFlag.TRADE: f"连续自动撮合({self.name}={self.value})",
            TickStatusFlag.SUSP: f"停牌({self.name}={self.value})",
            TickStatusFlag.CCALL: f"收盘集合竞价({self.name}={self.value})",
            TickStatusFlag.CLOSE: f"闭市({self.name}={self.value})",
            TickStatusFlag.ENDTR: f"交易结束({self.name}={self.value})"
        }[self]

    @classmethod
    def _missing_(cls, value):
        """处理无效的枚举值"""
        return cls.UNKNOWN  # 返回默认值
