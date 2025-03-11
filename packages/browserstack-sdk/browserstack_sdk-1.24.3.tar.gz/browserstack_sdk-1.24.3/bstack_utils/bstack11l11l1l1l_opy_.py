# coding: UTF-8
import sys
bstack1111l1l_opy_ = sys.version_info [0] == 2
bstack1llll1l_opy_ = 2048
bstack1ll1111_opy_ = 7
def bstack11lll_opy_ (bstack11lll1_opy_):
    global bstack1lll1l_opy_
    bstack1l1l11l_opy_ = ord (bstack11lll1_opy_ [-1])
    bstack11lllll_opy_ = bstack11lll1_opy_ [:-1]
    bstack1ll1lll_opy_ = bstack1l1l11l_opy_ % len (bstack11lllll_opy_)
    bstack11l1_opy_ = bstack11lllll_opy_ [:bstack1ll1lll_opy_] + bstack11lllll_opy_ [bstack1ll1lll_opy_:]
    if bstack1111l1l_opy_:
        bstack11llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack1llll1l_opy_ - (bstack111l1l1_opy_ + bstack1l1l11l_opy_) % bstack1ll1111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack11l1_opy_)])
    else:
        bstack11llll1_opy_ = str () .join ([chr (ord (char) - bstack1llll1l_opy_ - (bstack111l1l1_opy_ + bstack1l1l11l_opy_) % bstack1ll1111_opy_) for bstack111l1l1_opy_, char in enumerate (bstack11l1_opy_)])
    return eval (bstack11llll1_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack11111lll1_opy_, bstack11ll1l1111l_opy_
from bstack_utils.bstack1ll111ll1_opy_ import bstack1l11l1111ll_opy_
class bstack111ll1l111_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111lll1lll1_opy_=None, bstack111lll1ll1l_opy_=True, bstack1l11ll1l1ll_opy_=None, bstack1lllll1ll_opy_=None, result=None, duration=None, bstack111lll1111_opy_=None, meta={}):
        self.bstack111lll1111_opy_ = bstack111lll1111_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111lll1ll1l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111lll1lll1_opy_ = bstack111lll1lll1_opy_
        self.bstack1l11ll1l1ll_opy_ = bstack1l11ll1l1ll_opy_
        self.bstack1lllll1ll_opy_ = bstack1lllll1ll_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack111ll1l1ll_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l11ll111_opy_(self, meta):
        self.meta = meta
    def bstack11l1l1111l_opy_(self, hooks):
        self.hooks = hooks
    def bstack111llll11l1_opy_(self):
        bstack111llll1l1l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11lll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ᱾"): bstack111llll1l1l_opy_,
            bstack11lll_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪ᱿"): bstack111llll1l1l_opy_,
            bstack11lll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᲀ"): bstack111llll1l1l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11lll_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦᲁ") + key)
            setattr(self, key, val)
    def bstack111lllll111_opy_(self):
        return {
            bstack11lll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᲂ"): self.name,
            bstack11lll_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᲃ"): {
                bstack11lll_opy_ (u"࠭࡬ࡢࡰࡪࠫᲄ"): bstack11lll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᲅ"),
                bstack11lll_opy_ (u"ࠨࡥࡲࡨࡪ࠭ᲆ"): self.code
            },
            bstack11lll_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᲇ"): self.scope,
            bstack11lll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᲈ"): self.tags,
            bstack11lll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᲉ"): self.framework,
            bstack11lll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᲊ"): self.started_at
        }
    def bstack111llll111l_opy_(self):
        return {
         bstack11lll_opy_ (u"࠭࡭ࡦࡶࡤࠫ᲋"): self.meta
        }
    def bstack111lllll11l_opy_(self):
        return {
            bstack11lll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪ᲌"): {
                bstack11lll_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬ᲍"): self.bstack111lll1lll1_opy_
            }
        }
    def bstack111lll1llll_opy_(self, bstack111llllll1l_opy_, details):
        step = next(filter(lambda st: st[bstack11lll_opy_ (u"ࠩ࡬ࡨࠬ᲎")] == bstack111llllll1l_opy_, self.meta[bstack11lll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩ᲏")]), None)
        step.update(details)
    def bstack1llllllll_opy_(self, bstack111llllll1l_opy_):
        step = next(filter(lambda st: st[bstack11lll_opy_ (u"ࠫ࡮ࡪࠧᲐ")] == bstack111llllll1l_opy_, self.meta[bstack11lll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᲑ")]), None)
        step.update({
            bstack11lll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᲒ"): bstack11111lll1_opy_()
        })
    def bstack11l11l111l_opy_(self, bstack111llllll1l_opy_, result, duration=None):
        bstack1l11ll1l1ll_opy_ = bstack11111lll1_opy_()
        if bstack111llllll1l_opy_ is not None and self.meta.get(bstack11lll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭Დ")):
            step = next(filter(lambda st: st[bstack11lll_opy_ (u"ࠨ࡫ࡧࠫᲔ")] == bstack111llllll1l_opy_, self.meta[bstack11lll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᲕ")]), None)
            step.update({
                bstack11lll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᲖ"): bstack1l11ll1l1ll_opy_,
                bstack11lll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭Თ"): duration if duration else bstack11ll1l1111l_opy_(step[bstack11lll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᲘ")], bstack1l11ll1l1ll_opy_),
                bstack11lll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭Კ"): result.result,
                bstack11lll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᲚ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111lllllll1_opy_):
        if self.meta.get(bstack11lll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᲛ")):
            self.meta[bstack11lll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᲜ")].append(bstack111lllllll1_opy_)
        else:
            self.meta[bstack11lll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᲝ")] = [ bstack111lllllll1_opy_ ]
    def bstack111llll1l11_opy_(self):
        return {
            bstack11lll_opy_ (u"ࠫࡺࡻࡩࡥࠩᲞ"): self.bstack111ll1l1ll_opy_(),
            **self.bstack111lllll111_opy_(),
            **self.bstack111llll11l1_opy_(),
            **self.bstack111llll111l_opy_()
        }
    def bstack111lllll1ll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11lll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᲟ"): self.bstack1l11ll1l1ll_opy_,
            bstack11lll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᲠ"): self.duration,
            bstack11lll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᲡ"): self.result.result
        }
        if data[bstack11lll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᲢ")] == bstack11lll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᲣ"):
            data[bstack11lll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᲤ")] = self.result.bstack111l11ll1l_opy_()
            data[bstack11lll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᲥ")] = [{bstack11lll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᲦ"): self.result.bstack11lll11l1ll_opy_()}]
        return data
    def bstack111llll11ll_opy_(self):
        return {
            bstack11lll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᲧ"): self.bstack111ll1l1ll_opy_(),
            **self.bstack111lllll111_opy_(),
            **self.bstack111llll11l1_opy_(),
            **self.bstack111lllll1ll_opy_(),
            **self.bstack111llll111l_opy_()
        }
    def bstack111ll11lll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11lll_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨᲨ") in event:
            return self.bstack111llll1l11_opy_()
        elif bstack11lll_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᲩ") in event:
            return self.bstack111llll11ll_opy_()
    def bstack11l1111lll_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1l11ll1l1ll_opy_ = time if time else bstack11111lll1_opy_()
        self.duration = duration if duration else bstack11ll1l1111l_opy_(self.started_at, self.bstack1l11ll1l1ll_opy_)
        if result:
            self.result = result
class bstack11l1l11lll_opy_(bstack111ll1l111_opy_):
    def __init__(self, hooks=[], bstack11l11ll1l1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11l11ll1l1_opy_ = bstack11l11ll1l1_opy_
        super().__init__(*args, **kwargs, bstack1lllll1ll_opy_=bstack11lll_opy_ (u"ࠩࡷࡩࡸࡺࠧᲪ"))
    @classmethod
    def bstack111llll1111_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11lll_opy_ (u"ࠪ࡭ࡩ࠭Ძ"): id(step),
                bstack11lll_opy_ (u"ࠫࡹ࡫ࡸࡵࠩᲬ"): step.name,
                bstack11lll_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭Ჭ"): step.keyword,
            })
        return bstack11l1l11lll_opy_(
            **kwargs,
            meta={
                bstack11lll_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧᲮ"): {
                    bstack11lll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᲯ"): feature.name,
                    bstack11lll_opy_ (u"ࠨࡲࡤࡸ࡭࠭Ჰ"): feature.filename,
                    bstack11lll_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧᲱ"): feature.description
                },
                bstack11lll_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬᲲ"): {
                    bstack11lll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᲳ"): scenario.name
                },
                bstack11lll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᲴ"): steps,
                bstack11lll_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨᲵ"): bstack1l11l1111ll_opy_(test)
            }
        )
    def bstack111llll1ll1_opy_(self):
        return {
            bstack11lll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭Ჶ"): self.hooks
        }
    def bstack111llllll11_opy_(self):
        if self.bstack11l11ll1l1_opy_:
            return {
                bstack11lll_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧᲷ"): self.bstack11l11ll1l1_opy_
            }
        return {}
    def bstack111llll11ll_opy_(self):
        return {
            **super().bstack111llll11ll_opy_(),
            **self.bstack111llll1ll1_opy_()
        }
    def bstack111llll1l11_opy_(self):
        return {
            **super().bstack111llll1l11_opy_(),
            **self.bstack111llllll11_opy_()
        }
    def bstack11l1111lll_opy_(self):
        return bstack11lll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫᲸ")
class bstack11l1l1l111_opy_(bstack111ll1l111_opy_):
    def __init__(self, hook_type, *args,bstack11l11ll1l1_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack111lllll1l1_opy_ = None
        self.bstack11l11ll1l1_opy_ = bstack11l11ll1l1_opy_
        super().__init__(*args, **kwargs, bstack1lllll1ll_opy_=bstack11lll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᲹ"))
    def bstack111ll1l11l_opy_(self):
        return self.hook_type
    def bstack111llll1lll_opy_(self):
        return {
            bstack11lll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᲺ"): self.hook_type
        }
    def bstack111llll11ll_opy_(self):
        return {
            **super().bstack111llll11ll_opy_(),
            **self.bstack111llll1lll_opy_()
        }
    def bstack111llll1l11_opy_(self):
        return {
            **super().bstack111llll1l11_opy_(),
            bstack11lll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪ᲻"): self.bstack111lllll1l1_opy_,
            **self.bstack111llll1lll_opy_()
        }
    def bstack11l1111lll_opy_(self):
        return bstack11lll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨ᲼")
    def bstack11l11llll1_opy_(self, bstack111lllll1l1_opy_):
        self.bstack111lllll1l1_opy_ = bstack111lllll1l1_opy_