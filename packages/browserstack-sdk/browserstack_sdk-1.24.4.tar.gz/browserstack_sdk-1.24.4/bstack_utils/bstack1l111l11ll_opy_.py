# coding: UTF-8
import sys
bstack1111ll1_opy_ = sys.version_info [0] == 2
bstack1ll11l_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11ll1l_opy_ (bstack111l1l1_opy_):
    global bstack1l111_opy_
    bstack1l1lll_opy_ = ord (bstack111l1l1_opy_ [-1])
    bstack1l1llll_opy_ = bstack111l1l1_opy_ [:-1]
    bstack1l11ll1_opy_ = bstack1l1lll_opy_ % len (bstack1l1llll_opy_)
    bstack1l11ll_opy_ = bstack1l1llll_opy_ [:bstack1l11ll1_opy_] + bstack1l1llll_opy_ [bstack1l11ll1_opy_:]
    if bstack1111ll1_opy_:
        bstack11l1111_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll11l_opy_ - (bstack111ll_opy_ + bstack1l1lll_opy_) % bstack11lllll_opy_) for bstack111ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack11l1111_opy_ = str () .join ([chr (ord (char) - bstack1ll11l_opy_ - (bstack111ll_opy_ + bstack1l1lll_opy_) % bstack11lllll_opy_) for bstack111ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack11l1111_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack1l11111lll1_opy_, bstack1l11111l1ll_opy_
import tempfile
import json
bstack11l1lllllll_opy_ = os.getenv(bstack11ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡍ࡟ࡇࡋࡏࡉࠧ᫐"), None) or os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠢ᫑"))
bstack11ll1111lll_opy_ = os.path.join(bstack11ll1l_opy_ (u"ࠨ࡬ࡰࡩࠥ᫒"), bstack11ll1l_opy_ (u"ࠧࡴࡦ࡮࠱ࡨࡲࡩ࠮ࡦࡨࡦࡺ࡭࠮࡭ࡱࡪࠫ᫓"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11ll1l_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫ᫔"),
      datefmt=bstack11ll1l_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧ᫕"),
      stream=sys.stdout
    )
  return logger
def bstack1lll1ll11ll_opy_():
  bstack11ll11l1111_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡇࡉࡇ࡛ࡇࠣ᫖"), bstack11ll1l_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥ᫗"))
  return logging.DEBUG if bstack11ll11l1111_opy_.lower() == bstack11ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥ᫘") else logging.INFO
def bstack1ll1111l11l_opy_():
  global bstack11l1lllllll_opy_
  if os.path.exists(bstack11l1lllllll_opy_):
    os.remove(bstack11l1lllllll_opy_)
  if os.path.exists(bstack11ll1111lll_opy_):
    os.remove(bstack11ll1111lll_opy_)
def bstack1llll1l1l_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack11lll1l1l_opy_(config, log_level):
  bstack11ll111lll1_opy_ = log_level
  if bstack11ll1l_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨ᫙") in config and config[bstack11ll1l_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩ᫚")] in bstack1l11111lll1_opy_:
    bstack11ll111lll1_opy_ = bstack1l11111lll1_opy_[config[bstack11ll1l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪ᫛")]]
  if config.get(bstack11ll1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫ᫜"), False):
    logging.getLogger().setLevel(bstack11ll111lll1_opy_)
    return bstack11ll111lll1_opy_
  global bstack11l1lllllll_opy_
  bstack1llll1l1l_opy_()
  bstack11l1llll1l1_opy_ = logging.Formatter(
    fmt=bstack11ll1l_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭᫝"),
    datefmt=bstack11ll1l_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩ᫞"),
  )
  bstack11ll111111l_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11l1lllllll_opy_)
  file_handler.setFormatter(bstack11l1llll1l1_opy_)
  bstack11ll111111l_opy_.setFormatter(bstack11l1llll1l1_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11ll111111l_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11ll1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡶࡪࡳ࡯ࡵࡧ࠱ࡶࡪࡳ࡯ࡵࡧࡢࡧࡴࡴ࡮ࡦࡥࡷ࡭ࡴࡴࠧ᫟"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11ll111111l_opy_.setLevel(bstack11ll111lll1_opy_)
  logging.getLogger().addHandler(bstack11ll111111l_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11ll111lll1_opy_
def bstack11ll111llll_opy_(config):
  try:
    bstack11l1lllll11_opy_ = set(bstack1l11111l1ll_opy_)
    bstack11l1llll1ll_opy_ = bstack11ll1l_opy_ (u"࠭ࠧ᫠")
    with open(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪ᫡")) as bstack11ll1111111_opy_:
      bstack11ll11111l1_opy_ = bstack11ll1111111_opy_.read()
      bstack11l1llll1ll_opy_ = re.sub(bstack11ll1l_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠦ࠲࠯ࠪ࡜࡯ࠩ᫢"), bstack11ll1l_opy_ (u"ࠩࠪ᫣"), bstack11ll11111l1_opy_, flags=re.M)
      bstack11l1llll1ll_opy_ = re.sub(
        bstack11ll1l_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃ࠭࠭᫤") + bstack11ll1l_opy_ (u"ࠫࢁ࠭᫥").join(bstack11l1lllll11_opy_) + bstack11ll1l_opy_ (u"ࠬ࠯࠮ࠫࠦࠪ᫦"),
        bstack11ll1l_opy_ (u"ࡸࠧ࡝࠴࠽ࠤࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨ᫧"),
        bstack11l1llll1ll_opy_, flags=re.M | re.I
      )
    def bstack11ll111l1l1_opy_(dic):
      bstack11l1lllll1l_opy_ = {}
      for key, value in dic.items():
        if key in bstack11l1lllll11_opy_:
          bstack11l1lllll1l_opy_[key] = bstack11ll1l_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫ᫨")
        else:
          if isinstance(value, dict):
            bstack11l1lllll1l_opy_[key] = bstack11ll111l1l1_opy_(value)
          else:
            bstack11l1lllll1l_opy_[key] = value
      return bstack11l1lllll1l_opy_
    bstack11l1lllll1l_opy_ = bstack11ll111l1l1_opy_(config)
    return {
      bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫ᫩"): bstack11l1llll1ll_opy_,
      bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡳࡧ࡬ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬ᫪"): json.dumps(bstack11l1lllll1l_opy_)
    }
  except Exception as e:
    return {}
def bstack11l1llllll1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11ll1l_opy_ (u"ࠪࡰࡴ࡭ࠧ᫫"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11ll111l11l_opy_ = os.path.join(log_dir, bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷࠬ᫬"))
  if not os.path.exists(bstack11ll111l11l_opy_):
    bstack11ll111l111_opy_ = {
      bstack11ll1l_opy_ (u"ࠧ࡯࡮ࡪࡲࡤࡸ࡭ࠨ᫭"): str(inipath),
      bstack11ll1l_opy_ (u"ࠨࡲࡰࡱࡷࡴࡦࡺࡨࠣ᫮"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳ࠯࡬ࡶࡳࡳ࠭᫯")), bstack11ll1l_opy_ (u"ࠨࡹࠪ᫰")) as bstack11ll1111ll1_opy_:
      bstack11ll1111ll1_opy_.write(json.dumps(bstack11ll111l111_opy_))
def bstack11ll111ll11_opy_():
  try:
    bstack11ll111l11l_opy_ = os.path.join(os.getcwd(), bstack11ll1l_opy_ (u"ࠩ࡯ࡳ࡬࠭᫱"), bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩ᫲"))
    if os.path.exists(bstack11ll111l11l_opy_):
      with open(bstack11ll111l11l_opy_, bstack11ll1l_opy_ (u"ࠫࡷ࠭᫳")) as bstack11ll1111ll1_opy_:
        bstack11ll111ll1l_opy_ = json.load(bstack11ll1111ll1_opy_)
      return bstack11ll111ll1l_opy_.get(bstack11ll1l_opy_ (u"ࠬ࡯࡮ࡪࡲࡤࡸ࡭࠭᫴"), bstack11ll1l_opy_ (u"࠭ࠧ᫵")), bstack11ll111ll1l_opy_.get(bstack11ll1l_opy_ (u"ࠧࡳࡱࡲࡸࡵࡧࡴࡩࠩ᫶"), bstack11ll1l_opy_ (u"ࠨࠩ᫷"))
  except:
    pass
  return None, None
def bstack11ll111l1ll_opy_():
  try:
    bstack11ll111l11l_opy_ = os.path.join(os.getcwd(), bstack11ll1l_opy_ (u"ࠩ࡯ࡳ࡬࠭᫸"), bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩ᫹"))
    if os.path.exists(bstack11ll111l11l_opy_):
      os.remove(bstack11ll111l11l_opy_)
  except:
    pass
def bstack1l1lllll_opy_(config):
  from bstack_utils.helper import bstack1l1l11lll_opy_
  global bstack11l1lllllll_opy_
  try:
    if config.get(bstack11ll1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭᫺"), False):
      return
    uuid = os.getenv(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ᫻")) if os.getenv(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ᫼")) else bstack1l1l11lll_opy_.get_property(bstack11ll1l_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤ᫽"))
    if not uuid or uuid == bstack11ll1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭᫾"):
      return
    bstack11ll11111ll_opy_ = [bstack11ll1l_opy_ (u"ࠩࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳ࠯ࡶࡻࡸࠬ᫿"), bstack11ll1l_opy_ (u"ࠪࡔ࡮ࡶࡦࡪ࡮ࡨࠫᬀ"), bstack11ll1l_opy_ (u"ࠫࡵࡿࡰࡳࡱ࡭ࡩࡨࡺ࠮ࡵࡱࡰࡰࠬᬁ"), bstack11l1lllllll_opy_, bstack11ll1111lll_opy_]
    bstack11ll1111l1l_opy_, root_path = bstack11ll111ll11_opy_()
    if bstack11ll1111l1l_opy_ != None:
      bstack11ll11111ll_opy_.append(bstack11ll1111l1l_opy_)
    if root_path != None:
      bstack11ll11111ll_opy_.append(os.path.join(root_path, bstack11ll1l_opy_ (u"ࠬࡩ࡯࡯ࡨࡷࡩࡸࡺ࠮ࡱࡻࠪᬂ")))
    bstack1llll1l1l_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡬ࡰࡩࡶ࠱ࠬᬃ") + uuid + bstack11ll1l_opy_ (u"ࠧ࠯ࡶࡤࡶ࠳࡭ࡺࠨᬄ"))
    with tarfile.open(output_file, bstack11ll1l_opy_ (u"ࠣࡹ࠽࡫ࡿࠨᬅ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11ll11111ll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11ll111llll_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11ll1111l11_opy_ = data.encode()
        tarinfo.size = len(bstack11ll1111l11_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11ll1111l11_opy_))
    bstack1l1111lll1_opy_ = MultipartEncoder(
      fields= {
        bstack11ll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧᬆ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11ll1l_opy_ (u"ࠪࡶࡧ࠭ᬇ")), bstack11ll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱ࡻ࠱࡬ࢀࡩࡱࠩᬈ")),
        bstack11ll1l_opy_ (u"ࠬࡩ࡬ࡪࡧࡱࡸࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧᬉ"): uuid
      }
    )
    response = requests.post(
      bstack11ll1l_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡶࡲ࡯ࡳࡦࡪ࠭ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡧࡱ࡯ࡥ࡯ࡶ࠰ࡰࡴ࡭ࡳ࠰ࡷࡳࡰࡴࡧࡤࠣᬊ"),
      data=bstack1l1111lll1_opy_,
      headers={bstack11ll1l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ᬋ"): bstack1l1111lll1_opy_.content_type},
      auth=(config[bstack11ll1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪᬌ")], config[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᬍ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡸࡴࡱࡵࡡࡥࠢ࡯ࡳ࡬ࡹ࠺ࠡࠩᬎ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11ll1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡴࡤࡪࡰࡪࠤࡱࡵࡧࡴ࠼ࠪᬏ") + str(e))
  finally:
    try:
      bstack1ll1111l11l_opy_()
      bstack11ll111l1ll_opy_()
    except:
      pass