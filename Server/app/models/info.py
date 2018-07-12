from app.models import db
from sqlalchemy.dialects.mysql import INTEGER as Integer
from enum import Enum
from datetime import datetime


class AdmissionEnum(Enum):
    NORMAL = 1
    MEISTER = 2
    SOCIAL = 3


class AdmissionDetailEnum(Enum):
    DEFAULT = 0
    BENEFICIARY = 1
    ONE_PARENT = 2
    CHA_UPPER = 3
    CHACHA_UPPER = 4
    FROM_NORTH = 5
    MULTI_CULTURE = 6
    ETC = 7


class Info(db.Model):
    __tablename__ = "info"

    info_id = db.Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    user_id = db.Column(db.VARCHAR(32))
    address_base = db.Column(db.VARCHAR(100), default="")
    address_detail = db.Column(db.VARCHAR(50), default="")
    admission = db.Column(db.Enum(AdmissionEnum), default=AdmissionEnum.NORMAL)
    admission_detail = db.Column(db.Enum(AdmissionDetailEnum), default=AdmissionDetailEnum.DEFAULT)
    region = db.Column(db.Boolean(), default=False)
    name = db.Column(db.VARCHAR(12), default="")
    sex = db.Column(db.Boolean(), default=True)
    parent_name = db.Column(db.VARCHAR(12), default="")
    parent_tell = db.Column(db.VARCHAR(20), default="")
    my_tel = db.Column(db.VARCHAR(20), default="")
    introduce = db.Column(db.VARCHAR(1600), default="")
    study_plan = db.Column(db.VARCHAR(1600), default="")
    img_path = db.Column(db.VARCHAR(50), default="")
    exam_code = db.Column(db.VARCHAR(6), default="", unique=True)
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now)