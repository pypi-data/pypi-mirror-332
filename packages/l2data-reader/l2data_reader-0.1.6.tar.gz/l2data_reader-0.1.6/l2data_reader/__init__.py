"""
L2Data Reader - A package for reading level 2 market data.
"""

__version__ = '0.1.0'

from .reader import MarketDataReader, MarketDataHeader, IndexEntry
from .models import Snapshot, Slice, MarketDataResult
from .exceptions import NoDataException, DataFormatException

# 导入 proto 文件中的主要类结构
from .proto.global_pb2 import Envelope
from .proto.market_data_pb2 import (
    SecuDepthMarketData,
    TransactionEntrustData,
    TransactionTradeData,
    FutuDepthMarketData,
    FutuInstrumentStaticInfo,
    SecuDepthMarketDataPlus,
    SecuInstrumentStaticInfo,
    OptInstrumentStaticInfo,
    BondTradeInfo,
    OptDepthMarketData,
    HktInstrumentStaticInfo,
    HktDepthMarketData,
    BondTransactionTradeData,
    BondTransactionEntrustData
)

# 导出枚举类型
from .enums import (
    TransFlag, TrdType, Direction, OrdType, TickStatusFlag,
    ExerciseStyle, HktTradeLimit, BondTradeType, SecurityType,
    OptionsType, InstrumentTradeStatus, SettleType,
    BondBidExecInstType, BondBidTransType, RebuildTransType,
    SubSecurityType, MarketBizType, InvestorType
)

__all__ = [
    'MarketDataReader',
    'MarketDataHeader',
    'IndexEntry',
    'Snapshot',
    'Slice',
    'MarketDataResult',
    
    # 异常类
    'NoDataException',
    'DataFormatException',
    
    # Proto 消息类型
    'Envelope',
    'SecuDepthMarketData',
    'TransactionEntrustData',
    'TransactionTradeData',
    'FutuDepthMarketData',
    'FutuInstrumentStaticInfo',
    'SecuDepthMarketDataPlus',
    'SecuInstrumentStaticInfo',
    'OptInstrumentStaticInfo',
    'BondTradeInfo',
    'OptDepthMarketData',
    'HktInstrumentStaticInfo',
    'HktDepthMarketData',
    'BondTransactionTradeData',
    'BondTransactionEntrustData',
    
    # 枚举类型
    'TransFlag',
    'TrdType',
    'Direction',
    'OrdType',
    'TickStatusFlag',
    'ExerciseStyle',
    'HktTradeLimit',
    'BondTradeType',
    'SecurityType',
    'OptionsType',
    'InstrumentTradeStatus',
    'SettleType',
    'BondBidExecInstType',
    'BondBidTransType',
    'RebuildTransType',
    'SubSecurityType',
    'MarketBizType',
    'InvestorType',

    # 枚举映射
    'TRANS_FLAG_MAP',
    'TRD_TYPE_MAP',
    'DIRECTION_MAP',
    'ORD_TYPE_MAP',
    'TICK_STATUS_FLAG_MAP',
]