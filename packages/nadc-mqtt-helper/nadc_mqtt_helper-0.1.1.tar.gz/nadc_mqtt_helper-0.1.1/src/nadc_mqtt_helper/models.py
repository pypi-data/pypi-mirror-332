from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional, List

@dataclass
class EnvironmentData:
    """环境数据模型"""
    time: datetime
    temperature: float
    humidity: float
    dewtemperature: float
    pressure: float
    height: float
    windspeed: float
    windspeed_2: float
    windspeed_10: float
    windDirection: int
    Rainfall: float
    Rainfall_all: float
    pm25: float
    pm10: float
    voltage: float
    TimeStamp: datetime

    @classmethod
    def from_dict(cls, data: dict):
        """从字典创建实例，忽略多余的字段，并处理时间字符串"""
        valid_fields = cls.__annotations__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}
        
        # 转换时间字符串为datetime对象
        if isinstance(filtered_data.get('time'), str):
            filtered_data['time'] = datetime.fromisoformat(filtered_data['time'].replace('Z', '+00:00'))
        if isinstance(filtered_data.get('TimeStamp'), str):
            filtered_data['TimeStamp'] = datetime.fromisoformat(filtered_data['TimeStamp'].replace('Z', '+00:00'))
            
        return cls(**filtered_data)

    def to_dict(self):
        """转换为字典，处理datetime的序列化"""
        data = asdict(self)
        data['time'] = self.time.isoformat()
        data['TimeStamp'] = self.TimeStamp.isoformat()
        return {k: v for k, v in data.items() if v is not None}

@dataclass
class TelescopeStatus:
    """望远镜状态模型"""
    telescope: str
    instrument: str
    observation_assistant: str
    assistant_telephone: str
    status: str
    is_observable: bool
    daytime: str
    too_observing: str
    date: datetime

    @classmethod
    def from_dict(cls, data: dict):
        """从字典创建实例，忽略多余的字段，并处理时间字符串"""
        valid_fields = cls.__annotations__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}
        
        # 转换时间字符串为datetime对象
        if isinstance(filtered_data.get('date'), str):
            filtered_data['date'] = datetime.fromisoformat(filtered_data['date'].replace('Z', '+00:00'))
            
        return cls(**filtered_data)

    def to_dict(self):
        """转换为字典，处理datetime的序列化"""
        data = asdict(self)
        data['date'] = self.date.isoformat()
        return {k: v for k, v in data.items() if v is not None} 

@dataclass
class TelescopeStatusInfo:
    """望远镜信息总模型"""
    environment: List[EnvironmentData]
    telescope_status: TelescopeStatus

    @classmethod
    def from_dict(cls, data: dict):
        """从字典创建TelescopeStatusInfo对象"""
        env_data = [EnvironmentData.from_dict(item) for item in data.get('environment', [])]
        telescope_status = TelescopeStatus.from_dict(data.get('telescope_status', {}))
        return cls(
            environment=env_data,
            telescope_status=telescope_status
        )

    def to_dict(self):
        """转换为可JSON序列化的字典"""
        return {
            'environment': [env.to_dict() for env in self.environment],
            'telescope_status': self.telescope_status.to_dict()
        }

@dataclass
class ObservationData:
    """观测数据模型"""
    telescope: str
    Instrument: str
    pointing_ra: float
    pointing_dec: float
    start_time: datetime
    end_time: datetime
    duration: float
    event_name: str
    observer: str
    obs_type: str
    comment: Optional[str] = None
    update_time: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data: dict):
        """从字典创建实例，忽略多余的字段，并处理时间字符串"""
        valid_fields = cls.__annotations__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}
        
        # 转换时间字符串为datetime对象
        time_fields = ['start_time', 'end_time', 'update_time']
        for field in time_fields:
            if isinstance(filtered_data.get(field), str):
                filtered_data[field] = datetime.fromisoformat(filtered_data[field].replace('Z', '+00:00'))
            
        return cls(**filtered_data)

    def to_dict(self):
        """转换为字典，处理datetime的序列化"""
        data = asdict(self)
        # 处理所有datetime字段
        time_fields = ['start_time', 'end_time', 'update_time']
        for field in time_fields:
            if hasattr(self, field) and getattr(self, field) is not None:
                data[field] = getattr(self, field).isoformat()
        
        # 移除值为 None 的字段
        return {k: v for k, v in data.items() if v is not None} 