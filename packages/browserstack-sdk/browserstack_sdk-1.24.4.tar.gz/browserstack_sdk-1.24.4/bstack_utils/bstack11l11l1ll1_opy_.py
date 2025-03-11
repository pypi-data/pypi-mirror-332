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
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l1ll1111l_opy_, bstack11ll1l111ll_opy_
from bstack_utils.bstack11lll1l11_opy_ import bstack11l111l1lll_opy_
class bstack111llll1ll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111llll1lll_opy_=None, bstack111llllll11_opy_=True, bstack1l1l111l1l1_opy_=None, bstack11111ll1_opy_=None, result=None, duration=None, bstack111ll11lll_opy_=None, meta={}):
        self.bstack111ll11lll_opy_ = bstack111ll11lll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111llllll11_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111llll1lll_opy_ = bstack111llll1lll_opy_
        self.bstack1l1l111l1l1_opy_ = bstack1l1l111l1l1_opy_
        self.bstack11111ll1_opy_ = bstack11111ll1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack111ll1llll_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l11ll11l_opy_(self, meta):
        self.meta = meta
    def bstack11l1l1l1l1_opy_(self, hooks):
        self.hooks = hooks
    def bstack111llll1ll1_opy_(self):
        bstack111lllll1ll_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11ll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ᱾"): bstack111lllll1ll_opy_,
            bstack11ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪ᱿"): bstack111lllll1ll_opy_,
            bstack11ll1l_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᲀ"): bstack111lllll1ll_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11ll1l_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦᲁ") + key)
            setattr(self, key, val)
    def bstack111llll11l1_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᲂ"): self.name,
            bstack11ll1l_opy_ (u"ࠬࡨ࡯ࡥࡻࠪᲃ"): {
                bstack11ll1l_opy_ (u"࠭࡬ࡢࡰࡪࠫᲄ"): bstack11ll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧᲅ"),
                bstack11ll1l_opy_ (u"ࠨࡥࡲࡨࡪ࠭ᲆ"): self.code
            },
            bstack11ll1l_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᲇ"): self.scope,
            bstack11ll1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᲈ"): self.tags,
            bstack11ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᲉ"): self.framework,
            bstack11ll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᲊ"): self.started_at
        }
    def bstack111llll1l11_opy_(self):
        return {
         bstack11ll1l_opy_ (u"࠭࡭ࡦࡶࡤࠫ᲋"): self.meta
        }
    def bstack111lllll111_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪ᲌"): {
                bstack11ll1l_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬ᲍"): self.bstack111llll1lll_opy_
            }
        }
    def bstack111llll1111_opy_(self, bstack111llllll1l_opy_, details):
        step = next(filter(lambda st: st[bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬ᲎")] == bstack111llllll1l_opy_, self.meta[bstack11ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩ᲏")]), None)
        step.update(details)
    def bstack1lllllll1l_opy_(self, bstack111llllll1l_opy_):
        step = next(filter(lambda st: st[bstack11ll1l_opy_ (u"ࠫ࡮ࡪࠧᲐ")] == bstack111llllll1l_opy_, self.meta[bstack11ll1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᲑ")]), None)
        step.update({
            bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᲒ"): bstack1l1ll1111l_opy_()
        })
    def bstack11l11lllll_opy_(self, bstack111llllll1l_opy_, result, duration=None):
        bstack1l1l111l1l1_opy_ = bstack1l1ll1111l_opy_()
        if bstack111llllll1l_opy_ is not None and self.meta.get(bstack11ll1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭Დ")):
            step = next(filter(lambda st: st[bstack11ll1l_opy_ (u"ࠨ࡫ࡧࠫᲔ")] == bstack111llllll1l_opy_, self.meta[bstack11ll1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᲕ")]), None)
            step.update({
                bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᲖ"): bstack1l1l111l1l1_opy_,
                bstack11ll1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭Თ"): duration if duration else bstack11ll1l111ll_opy_(step[bstack11ll1l_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᲘ")], bstack1l1l111l1l1_opy_),
                bstack11ll1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭Კ"): result.result,
                bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᲚ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111lll1llll_opy_):
        if self.meta.get(bstack11ll1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᲛ")):
            self.meta[bstack11ll1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᲜ")].append(bstack111lll1llll_opy_)
        else:
            self.meta[bstack11ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩᲝ")] = [ bstack111lll1llll_opy_ ]
    def bstack111llll111l_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠫࡺࡻࡩࡥࠩᲞ"): self.bstack111ll1llll_opy_(),
            **self.bstack111llll11l1_opy_(),
            **self.bstack111llll1ll1_opy_(),
            **self.bstack111llll1l11_opy_()
        }
    def bstack111llll11ll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11ll1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᲟ"): self.bstack1l1l111l1l1_opy_,
            bstack11ll1l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᲠ"): self.duration,
            bstack11ll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᲡ"): self.result.result
        }
        if data[bstack11ll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᲢ")] == bstack11ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᲣ"):
            data[bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᲤ")] = self.result.bstack111l11ll1l_opy_()
            data[bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᲥ")] = [{bstack11ll1l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᲦ"): self.result.bstack11lll11ll11_opy_()}]
        return data
    def bstack111llll1l1l_opy_(self):
        return {
            bstack11ll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᲧ"): self.bstack111ll1llll_opy_(),
            **self.bstack111llll11l1_opy_(),
            **self.bstack111llll1ll1_opy_(),
            **self.bstack111llll11ll_opy_(),
            **self.bstack111llll1l11_opy_()
        }
    def bstack11l111l11l_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11ll1l_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨᲨ") in event:
            return self.bstack111llll111l_opy_()
        elif bstack11ll1l_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᲩ") in event:
            return self.bstack111llll1l1l_opy_()
    def bstack111ll111ll_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1l1l111l1l1_opy_ = time if time else bstack1l1ll1111l_opy_()
        self.duration = duration if duration else bstack11ll1l111ll_opy_(self.started_at, self.bstack1l1l111l1l1_opy_)
        if result:
            self.result = result
class bstack11l11l1l1l_opy_(bstack111llll1ll_opy_):
    def __init__(self, hooks=[], bstack11l11l11l1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11l11l11l1_opy_ = bstack11l11l11l1_opy_
        super().__init__(*args, **kwargs, bstack11111ll1_opy_=bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺࠧᲪ"))
    @classmethod
    def bstack111lllll1l1_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11ll1l_opy_ (u"ࠪ࡭ࡩ࠭Ძ"): id(step),
                bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡸࡵࠩᲬ"): step.name,
                bstack11ll1l_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭Ჭ"): step.keyword,
            })
        return bstack11l11l1l1l_opy_(
            **kwargs,
            meta={
                bstack11ll1l_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧᲮ"): {
                    bstack11ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᲯ"): feature.name,
                    bstack11ll1l_opy_ (u"ࠨࡲࡤࡸ࡭࠭Ჰ"): feature.filename,
                    bstack11ll1l_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧᲱ"): feature.description
                },
                bstack11ll1l_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬᲲ"): {
                    bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᲳ"): scenario.name
                },
                bstack11ll1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᲴ"): steps,
                bstack11ll1l_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨᲵ"): bstack11l111l1lll_opy_(test)
            }
        )
    def bstack111llllllll_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭Ჶ"): self.hooks
        }
    def bstack11l11111111_opy_(self):
        if self.bstack11l11l11l1_opy_:
            return {
                bstack11ll1l_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧᲷ"): self.bstack11l11l11l1_opy_
            }
        return {}
    def bstack111llll1l1l_opy_(self):
        return {
            **super().bstack111llll1l1l_opy_(),
            **self.bstack111llllllll_opy_()
        }
    def bstack111llll111l_opy_(self):
        return {
            **super().bstack111llll111l_opy_(),
            **self.bstack11l11111111_opy_()
        }
    def bstack111ll111ll_opy_(self):
        return bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫᲸ")
class bstack11l1l11l11_opy_(bstack111llll1ll_opy_):
    def __init__(self, hook_type, *args,bstack11l11l11l1_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack111lllll11l_opy_ = None
        self.bstack11l11l11l1_opy_ = bstack11l11l11l1_opy_
        super().__init__(*args, **kwargs, bstack11111ll1_opy_=bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᲹ"))
    def bstack111lllll11_opy_(self):
        return self.hook_type
    def bstack111lllllll1_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᲺ"): self.hook_type
        }
    def bstack111llll1l1l_opy_(self):
        return {
            **super().bstack111llll1l1l_opy_(),
            **self.bstack111lllllll1_opy_()
        }
    def bstack111llll111l_opy_(self):
        return {
            **super().bstack111llll111l_opy_(),
            bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪ᲻"): self.bstack111lllll11l_opy_,
            **self.bstack111lllllll1_opy_()
        }
    def bstack111ll111ll_opy_(self):
        return bstack11ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨ᲼")
    def bstack11l1l11l1l_opy_(self, bstack111lllll11l_opy_):
        self.bstack111lllll11l_opy_ = bstack111lllll11l_opy_