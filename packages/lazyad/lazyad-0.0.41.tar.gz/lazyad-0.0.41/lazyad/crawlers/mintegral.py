from lazysdk import lazyrequests
from lazysdk import lazytime
import copy


"""
官网：https://adv.mintegral.com/cn/login
"""
default_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflated",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "",
        "Host": "ss-api.mintegral.com",
        "Origin": "https://adv.mintegral.com",
        "Pragma": "no-cache",
        "Referer": "https://adv.mintegral.com/cn/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0"
    }


def auth(
        cookie: str
):
    """
    验证cookie是否有效
    需要登录：{'code': 400, 'msg': 'Please login first', 'data': None}
    验证成功：{'code': 200, 'msg': 'success', 'data': {}

    """
    url = "https://ss-api.mintegral.com/api/v1/auth"
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    return lazyrequests.lazy_requests(
        method="GET",
        url=url,
        headers=headers
    )


def options(
        cookie: str
):
    """
    获取系统的基本选项
    需要登录：{'code': 400, 'msg': 'Please login first', 'data': None}
    验证成功：
        {
            'code': 200,
            'msg': 'success',
            'data': {
                'offer': ...,
                'campaign': ...,
                ...
                }
        }
    """
    scheme = "https"
    host = "ss-api.mintegral.com"
    filename = "/api/v1/options/_batch"
    params = {
        "query": "offer,campaign,offer-status,billing-type,country,timezone,country-region-city"
    }
    url = f"{scheme}://{host}{filename}"
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    return lazyrequests.lazy_requests(
        method="GET",
        params=params,
        url=url,
        headers=headers
    )


def offers(
        cookie: str,
        offer_id: int = None,
        method: str = "GET",
        put_data: dict = None,
        page: int = 1,
        page_size: int = 50
):
    """
    获取广告单元列表
    需要登录：{'code': 400, 'msg': 'Please login first', 'data': None}
    验证成功：{'code': 200, 'msg': 'success', 'data': {}
    """
    scheme = "https"
    host = "ss-api.mintegral.com"
    if not offer_id:
        filename = "/api/v1/offers"
        params = {
            "limit": page_size,
            "page": page,
            "order": "DESC",
            "sort": "id"
        }
    else:
        filename = f"/api/v1/offers/{offer_id}"
        if method == "PUT":
            params = put_data
        else:
            params = {}

    url = f"{scheme}://{host}{filename}"
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    return lazyrequests.lazy_requests(
        method=method,
        params=params,
        url=url,
        headers=headers
    )


def performance(
        cookie: str,
        total: bool = False,

        page: int = 1,
        page_size: int = 50,
        timezone: int = 8,
        start_time: str = None,
        end_time: str = None,
        show_calendar_day: int = 2,
        breakdowns: list = None,
        metrics: list = None,
        sort: str = None,
        order: str = "DESC",
        adv_campaign_id: int = None
):
    """
    获取广告单元列表
    需要登录：{'code': 400, 'msg': 'Please login first', 'data': None}
    验证成功：{'code': 200, 'msg': 'success', 'data': {}
    :param start_time: 开始日期，例如：2025-03-05
    :param end_time: 结束日期，例如：2025-03-05
    :param breakdowns: 分组依据（高级选项）：[]
        (date：天, timestamp：小时，week：周，month：月)
        adv_offer_id：广告单元,
        bid_type：Bid Type,
        country_code：国家或地区
        app：应用id(子渠道)
        package_name：包名(子渠道)
        app_name：应用名称(子渠道)
        adv_campaign_id：广告
        received_price：单价
        ad_type：广告类型
    :param sort: [可选-排序] 排序依据（高级选项）：adv_install：转化
    :param adv_campaign_id: [可选-筛选]广告名称
    """
    scheme = "https"
    host = "ss-api.mintegral.com"
    filename = "/api/v1/reports/performance"  # 获取详细数据
    filename_total = "/api/v1/reports/performance-total"  # 获取总数据数据量，该请求优先

    if not start_time:
        start_time = lazytime.get_date_string(days=0)
    if not end_time:
        end_time = lazytime.get_date_string(days=0)
    if not breakdowns:  # 数据维度
        breakdowns = [
            "date",
            "adv_offer_id"
        ]
    if not metrics:  # 数据指标
        metrics = [
            "adv_impression",  # 展示
            "adv_click",  # 点击
            "adv_install",  # 转化
            "ecpm",  # eCPM
            "ecpc",  # CPC
            "ecpi",  # eCPI
            "ctr",  # CTR
            "ivr",  # IVR
            "cvr",  # CVR
            "adv_original_money",  # 花费
            "iaa_d0_ad_revenue",  # D0 Ad Rev
            "iaa_d0_roas",  # D0 Ad Roas
            "iaa_d3_ad_revenue",  # D3 Ad Rev
            "iaa_d3_roas",  # D3 Ad Roas
            "iaa_d7_ad_revenue",  # D7 Ad Rev
            "iaa_d7_roas",  # D7 Ad Roas
            # "iap_d0_ad_revenue",  # D0 IAP Rev
            # "iap_d0_roas",  # D0 IAP Roas
            # "iap_d3_ad_revenue",  # D3 IAP Rev
            # "iap_d3_roas",  # D3 IAP Roas
            # "iap_d7_ad_revenue",  # D7 IAP Rev
            # "iap_d7_roas",  # D7 IAP Roas
        ]
    params = {
        "limit": page_size,
        "page": page,
        "timezone": timezone,
        "start_time": start_time,
        "end_time": end_time,
        "order": order,  # 排序
        "breakdowns": ",".join(breakdowns),
        "metrics": ",".join(metrics),
        "show_calendar_day": show_calendar_day
    }
    if sort:
        params["sort"] = sort
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    if total:
        return lazyrequests.lazy_requests(
            method="GET",
            params=params,
            url=f"{scheme}://{host}{filename_total}",
            headers=headers
        )
    else:
        return lazyrequests.lazy_requests(
            method="GET",
            params=params,
            url=f"{scheme}://{host}{filename}",
            headers=headers
        )
