from lazysdk import lazyrequests
from lazysdk import lazytime
import showlog
import copy
import json


default_headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection": "keep-alive",
    "Host": "cli2.mobgi.com",
    "Origin": "https://cl.mobgi.com",
    "Referer": "https://cl.mobgi.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0",
}


def get_media_account(
        media_type: str,
        cookie: str = None,
        page: int = 1,
        page_size: int = 20,
        total_count: int = 0
):
    """
    获取 推广-账户管理下的账户列表
    :param media_type: 媒体类型
    :param cookie:
    :param page:
    :param page_size:
    :param total_count:
    :return:
    """

    url = 'https://cli2.mobgi.com/Media/Account/getList'
    data = {
        "media_type": media_type,
        "advertiser_type": "1",
        "page": page,
        "page_size": page_size,
        "total_count": total_count
    }
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie

    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        json=data,
        headers=headers,
        return_json=True
    )


def get_ad_report(
        cookie: str,
        media_type: str,
        start_date: str = None,
        end_date: str = None,
        page: int = 1,
        page_size: int = 20,
        sort_field: str = "cost",
        time_dim: str = "sum",
        sort_direction: str = "desc",
        data_dim: str = "ad",
        data_type: str = "list",
        conditions: dict = None,
        kpis: list = None,
        relate_dims: list = None,
):
    """
    报表-广告报表
    :param cookie:
    :param start_date: 数据开始日期，默认为当日
    :param end_date: 数据结束日期，默认为当日
    :param page: 页码
    :param page_size: 每页数量
    :param media_type: 媒体：gdt_new|广点通(新指标体系)，toutiao_upgrade|今日头条2.0，aggregate|不限
    :param sort_field: 排序字段
    :param time_dim: 数据的时间维度汇总方式
    :param sort_direction: 排序方式，desc降序
    :param data_dim: 数据维度，advertiser_id:账户，ad:广告
    :param data_type:
    :param conditions: 搜索条件
    :param kpis: 需要获取的字段
    :param relate_dims: 关联维度，advertiser_id:账户
    :return:
    """
    if not start_date:
        start_date = lazytime.get_date_string(days=0)
    if not end_date:
        end_date = lazytime.get_date_string(days=0)
    url = "https://cli2.mobgi.com/ReportV23/AdReport/getReport"
    data = {
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
        "page_size": page_size,
        "media_type": media_type,
        "time_dim": time_dim,
        "data_type": data_type,
        "data_dim": data_dim,
        "sort_field": sort_field,
        "sort_direction": sort_direction,
    }
    if media_type == "baidu":
        if not conditions:
            conditions = {
                    "keyword": "",
                    "advertiser_id": [],
                    "app_id": [],
                    "owner_user_id": [],
                    "media_agent_id": []
                }
        if not kpis:
            kpis = [
                    "cost",
                    "weixinfollowsuccessconversions",
                    "weixinfollowsuccessconversionscost",
                    "payreaduv",
                    "payreaduvcost",
                    "cpc"
                ]
        if not relate_dims:
            relate_dims = ["advertiser_id"]

    elif media_type == "gdt_new":
        if not conditions:
            conditions = {
                    "keyword": "",
                    "advertiser_id": [],
                    "app_id": [],
                    "owner_user_id": [],
                    "media_agent_id": [],
                    "landing_type": [],
                    "time_line": "REPORTING_TIME"
                }
        if not kpis:
            kpis = [
                    "cost",
                    "conversions_count",
                    "from_follow_uv",
                    "cheout_fd",
                    "cheout_fd_reward",
                    "thousand_display_price",
                    "first_pay_count",
                    "conversions_cost",
                    "from_follow_cost",
                    "valid_click_count",
                    "cpc"
                ]
        if not relate_dims:
            relate_dims = ["advertiser_id"]

    elif media_type == "toutiao_upgrade":
        if not conditions:
            conditions = {
                "keyword": "",
                "advertiser_id": [],
                "app_id": [],
                "owner_user_id": [],
                "media_agent_id": [],
                "landing_type": [],
                "cl_create_way": []
            }
        if not kpis:
            kpis = [
                "stat_cost",
                "cpm_platform",
                "convert_cnt",
                "conversion_cost",
                "active",
                "active_cost",
                "click_cnt",
                "cpc_platform",
                "attribution_game_in_app_ltv_1day",
                "attribution_game_in_app_roi_1day",
                "ctr"
            ]
        if not relate_dims:
            relate_dims = ["advertiser_id"]

    else:
        showlog.warning("未知媒体类型")
        return

    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    data["conditions"] = conditions
    data["kpis"] = kpis
    data["relate_dims"] = relate_dims
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        json=data,
        headers=headers
    )


def get_plan_list(
        cookie: str,
        media_type: str,
        sort_field: str,
        media_account_id: int = None,
        page: int = 1,
        page_size: int = 20,
        start_date: str = None,
        end_date: str = None,
        sort_direction: str = "desc",
        data_type: str = "list",
        conditions: dict = None,
        advertiser_id: int = None,
        cdt_start_date: str = None,
        cdt_end_date: str = None,
        kpis: list = None,
        req_source: str = None
):
    """
    获取推广计划
    :param cookie:
    :param media_type:
    :param media_account_id:
    :param sort_field: 排序字段
    :param page:
    :param page_size:
    :param start_date: 数据开始日期
    :param end_date: 数据结束日期
    :param sort_direction: 排序方式，desc:降序
    :param data_type:
    :param conditions: 搜索条件
    :param advertiser_id: 账户id
    :param cdt_start_date: 创建开始时间
    :param cdt_end_date: 创建结束时间
    :param kpis:
    :param req_source: 腾讯需要的参数
    :return:
    """
    if not start_date:
        start_date = lazytime.get_date_string(days=0)
    if not end_date:
        end_date = lazytime.get_date_string(days=0)
    if not cdt_start_date:
        cdt_start_date = lazytime.get_date_string(days=-365)
    if not cdt_end_date:
        cdt_end_date = lazytime.get_date_string(days=0)
    data = {
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
        "page_size": page_size,
        "sort_field": sort_field,
        "sort_direction": sort_direction,
        "data_type": data_type
    }
    if media_type == "baidu":
        url = "https://cli2.mobgi.com/Baidu/Campaign/getList"
        if not conditions:
            conditions = {
                "cl_project_id": [],
                "optimize_user_id": [],
                "media_account_id": [],
                "extension_subject": [],
                "status": "",
                "keyword": "",
                "companys": [],
                "cdt_start_date": f"{cdt_start_date} 00:00:00",
                "cdt_end_date": f"{cdt_end_date} 23:59:59"
            }
            if media_account_id:
                conditions["media_account_id"] = [media_account_id]
        data["conditions"] = json.dumps(conditions)
    elif media_type == "gdt_new":
        url = "https://cli2.mobgi.com/Gdt/MainList/getList"
        if not conditions:
            conditions = {
                "is_deleted": "",
                "project_id": [],
                "advertiser_id": [],
                "user_id": [],
                "configured_status": ["STATUS_NO_DELETED"],  # 所有未删除
                "keyword": "",
                "companys": [],
                "time_line": "REPORTING_TIME",
                "cdt_start_date": f"{cdt_start_date} 00:00:00",
                "cdt_end_date": f"{cdt_end_date} 23:59:59"
            }
            if advertiser_id:
                conditions["advertiser_id"] = [advertiser_id]
        data["conditions"] = json.dumps(conditions)
        if kpis:
            data["kpis"] = kpis
        if req_source:
            data["req_source"] = req_source
    else:
        return
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        json=data,
        headers=headers
    )


def update_ad_batch(
        cookie,
        media_type: str,

        adgroup_id: int = None,
        adgroup_ids: list = None,

        advertiser_id: int = None,
        advertiser_ids: list = None,

        campaign_id: int = None,
        campaign_ids: list = None,

        adgroup_feed_id: int = None,
        adgroup_feed_ids: list = None,

        promotion_id: int = None,
        promotion_ids: list = None,

        campaign_feed_id: int = None,
        campaign_feed_ids: list = None,

        operate: str = "disable"
):
    """
    暂停广告
    :return:
    """
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    if media_type == "gdt_new":
        if not advertiser_ids:
            advertiser_ids = [advertiser_id]
        post_data = {
            "advertiser_ids": advertiser_ids,
            "value": "",
            "field": operate
        }
        if adgroup_id or adgroup_ids:
            url = "https://cli2.mobgi.com/Gdt/MainList/updateAdGroupBatch"
            if not adgroup_ids:
                adgroup_ids = [adgroup_id]
            post_data["adgroup_ids"] = adgroup_ids
        elif campaign_id or campaign_ids:
            url = "https://cli2.mobgi.com/Gdt/MainList/updateCampaignBatch"
            if campaign_id and not campaign_ids:
                campaign_ids = [campaign_id]
            post_data["campaign_ids"] = campaign_ids
        else:
            return

    elif media_type == "baidu":
        if adgroup_feed_id or adgroup_feed_ids:
            url = "https://cli2.mobgi.com/Baidu/AdGroup/batchUpdate"
            if adgroup_feed_id and not adgroup_feed_ids:
                adgroup_feed_ids = [adgroup_feed_id]
            post_data = {
                "adgroup_feed_ids": adgroup_feed_ids,
                "opt_status": operate
            }
        elif campaign_feed_id or campaign_feed_ids:
            url = "https://cli2.mobgi.com/Baidu/Campaign/batchUpdate"
            if campaign_feed_id and not campaign_feed_ids:
                campaign_feed_ids = [campaign_feed_id]
            post_data = {
                "campaign_feed_ids": campaign_feed_ids,
                "opt_status": operate
            }
        else:
            return
    elif media_type == "toutiao_upgrade":
        url = "https://cli2.mobgi.com/Toutiao/Promotion/updateStatus"
        if promotion_id and not promotion_ids:
            promotion_ids = [promotion_id]
        post_data = {
            "promotion_ids": promotion_ids,
            "opt_status": operate
        }
    else:
        return
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        json=post_data,
        headers=headers
    )


def update_creative_batch(
        cookie,
        media_type: str,

        creative_ids: list = None,
        advertiser_ids: list = None,

        operate: str = "creative_disable"
):
    """
    修改创意状态
    :return:
    """
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    if media_type == "gdt_upgrade":
        url = "https://cli2.mobgi.com/Gdt/MainList/updateCreativeBatchV1"
        post_data = {
            "advertiser_ids": advertiser_ids,
            "creative_ids": creative_ids,
            "value": "",
            "field": operate
        }

    else:
        return
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        json=post_data,
        headers=headers
    )


def get_material_report(
        cookie: str,
        start_date: str = None,
        end_date: str = None,
        page: int = 1,
        page_size: int = 20,
        media_type: str = "aggregate",
        kpis: list = None,
        sort_field: str = None,
        time_dim: str = "days",
        data_dim: str = "material",
        data_type: str = "list",
        sort_direction: str = "desc",
        conditions: dict = None,
        relate_dims: list = None
):
    """
    报表-素材报表
    :param cookie:
    :param start_date:
    :param end_date:
    :param page:
    :param page_size:
    :param media_type:媒体：gdt_new|广点通(新指标体系)，toutiao_upgrade|今日头条2.0，aggregate|不限,baidu:百度信息流
    :param data_dim:
    :param data_type:
    :param sort_direction:
    :param sort_field:
    :param time_dim: 时间维度的数据汇总方式，days：分日，sum：汇总
    :param conditions:
    :param kpis:
    :param relate_dims:
    :return:
    """
    if not start_date:
        start_date = lazytime.get_date_string(days=0)
    if not end_date:
        end_date = lazytime.get_date_string(days=0)
    url = "https://cli2.mobgi.com/ReportV23/MaterialReport/getReport"
    data = {
        "time_dim": time_dim,
        "media_type": media_type,
        "data_type": data_type,
        "data_dim": data_dim,
        "sort_field": sort_field,
        "sort_direction": sort_direction,
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
        "page_size": page_size
    }
    if media_type == "baidu":
        if not conditions:
            conditions = {
                "search_type": "name",
                "media_project_id": [],
                "material_special_id": [],
                "make_user_id": [],
                "advertiser_id": [],
                "owner_user_id": [],
                "media_advertiser_company": [],
                "material_type": "",
                "label_ids": [],
                "material_group_id": []
            }
        if not kpis:
            kpis = [
                "cost",
                "weixinfollowsuccessconversions",
                "weixinfollowsuccessconversionscost",
                "payreaduv",
                "payreaduvcost"
            ]
        if not relate_dims:
            relate_dims = [
                "material_create_time",
                "owner_user_id",
                "creative_user_id",
                "adgroup_feed_id"
            ]
    elif media_type == "gdt_new":
        if not conditions:
            conditions = {
                "advertiser_id": [],
                "label_ids": [],
                "make_user_id": [],
                "material_group_id": [],
                "material_special_id": [],
                "material_type": "",
                "media_advertiser_company": [],
                "media_project_id": [],
                "owner_user_id": [],
                "search_type": "name"
            }
        if not kpis:
            kpis = [
                "cost",
                "cheout_fd",
                "cheout_fd_reward",
                "first_pay_count",
                "first_pay_cost",
                "conversions_count",
                "conversions_cost",
                "from_follow_uv",
                "from_follow_cost",
                "thousand_display_price"
            ]
        if not relate_dims:
            relate_dims = []
    else:
        pass

    if conditions:
        data["conditions"] = conditions
    if kpis:
        data["kpis"] = kpis
    if relate_dims:
        data["relate_dims"] = relate_dims
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        json=data,
        headers=headers
    )


def get_account_report(
        cookie: str,
        media_type: str,
        start_date: str = None,
        end_date: str = None,
        page: int = 1,
        page_size: int = 20,
        sort_field: str = "cost",
        sort_direction: str = "desc",
        data_type: str = "list",
        conditions: dict = None,
        kpis: list = None,
        base_infos: list = None,
        time_line: str = "REPORTING_TIME"
):
    """
    推广-广告管理-媒体账户
    :param cookie:
    :param start_date: 数据开始日期，默认为当日
    :param end_date: 数据结束日期，默认为当日
    :param page: 页码
    :param page_size: 每页数量
    :param media_type: 媒体：gdt_upgrade|腾讯广告3.0，
    :param sort_field: 排序字段
    :param sort_direction: 排序方式，desc降序
    :param data_type:
    :param conditions: 搜索条件
    :param kpis: 需要获取的字段
    :return:
    """
    if not start_date:
        start_date = lazytime.get_date_string(days=0)
    if not end_date:
        end_date = lazytime.get_date_string(days=0)
    url = "https://cli2.mobgi.com/MainPanelReport/AccountReport/getReport"
    data = {
        "data_type": data_type,
        "media_type": media_type,
        "sort_field": sort_field,
        "sort_direction": sort_direction,
        "page": page,
        "page_size": page_size,
        "start_date": start_date,
        "end_date": end_date,
        "time_line": time_line
    }
    if media_type == "gdt_upgrade":
        if not conditions:
            conditions = {
                "keyword": "",
                "owner_user_id": [],
                "company": [],
                "media_project_id": [],
                "balance": "",
                "time_line": "REPORTING_TIME"
            }
        if not kpis:
            kpis = [
                "cost",
                "thousand_display_price",
                "cpc",
                "conversions_count",
                "conversions_cost",
                "from_follow_uv",
                "from_follow_cost",
                "cheout_fd"
            ]
        if not base_infos:
            base_infos = [
                "advertiser_id",
                "advertiser_nick",
                "user_name",
                "advertiser_name",
                "balance",
                "daily_budget"
            ]
    else:
        showlog.warning("未知媒体类型")
        return

    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    data["conditions"] = conditions
    data["kpis"] = kpis
    data["base_infos"] = base_infos
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        json=data,
        headers=headers
    )


def update_budget_batch(
        cookie: str,
        media_type: str,
        media_account_id: str = None,
        media_account_ids: list = None,
        daily_budget: str = None
):
    """
    修改账户日预算
    :param cookie:
    :return:
    """
    if media_type == "gdt":
        # 目前只有旧版可以改，新版的无法改
        url = "https://cli2.mobgi.com/Gdt/MainList/updateBudgetBatch"
        if media_account_id:
            inner_data = [
                {
                    "media_account_id": media_account_id,
                    "daily_budget": daily_budget
                }
            ]
        elif media_account_ids:
            inner_data = list()
            for media_account_id_ in media_account_ids:
                inner_data.append(
                    {
                        "media_account_id": media_account_id_,
                        "daily_budget": daily_budget
                    }
                )
        else:
            return
        data = {
            "data": inner_data,
            "time": "now"
        }
    else:
        showlog.warning("未知媒体类型")
        return

    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        json=data,
        headers=headers
    )


def get_task_result(
        cookie: str,
        batch_id: str
):
    """
    获取任务结果
    :param cookie:
    :param batch_id:
    :return:
    """
    url = "https://cli2.mobgi.com/Toutiao/Tools/getTaskResult"
    data = {"batch_id": batch_id}
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        json=data,
        headers=headers
    )


def get_task_result_end(
        cookie: str,
        batch_id: str
):
    """
    获取任务结果，等待任务结束
    :param cookie:
    :param batch_id:
    :return:
    """
    while True:
        res = get_task_result(
            cookie=cookie,
            batch_id=batch_id
        )
        if res.get("code") == 0:
            processing = res["data"]["processing"]
            if not processing:
                return res
            else:
                lazytime.count_down(1)
        else:
            return res


def get_project_report(
        cookie: str,
        media_type: str = "aggregate",
        start_date: str = None,
        end_date: str = None,
        page: int = 1,
        page_size: int = 20,
        sort_field: str = "aggregate_cost",
        sort_direction: str = "desc",
        data_type: str = "list",
        conditions: dict = None,
        kpis: list = None,
        relate_dims: list = None,
        time_line: str = "REPORTING_TIME",
        time_dim: str = "days",
        data_dim: str = "media_project_id"
):
    """
    报表-项目报表
    :param cookie:
    :param media_type: 媒体：aggregate|不限
    :param start_date: 数据开始日期，默认为当日
    :param end_date: 数据结束日期，默认为当日
    :param page: 页码
    :param page_size: 每页数量
    :param sort_field: 排序字段
    :param sort_direction: 排序方式，desc降序
    :param data_type:
    :param conditions: 搜索条件
    :param kpis: 需要获取的字段
    :param relate_dims:
    :param time_line:
    :param time_dim:
    :param data_dim:
    :return:
    """
    if not start_date:
        start_date = lazytime.get_date_string(days=0)
    if not end_date:
        end_date = lazytime.get_date_string(days=0)
    url = "https://cli2.mobgi.com/ReportV23/ProjectReport/getReport"
    data = {
        "time_dim": time_dim,
        "media_type": media_type,
        "data_type": data_type,
        "data_dim": data_dim,
        "sort_field": sort_field,
        "sort_direction": sort_direction,
        "start_date": start_date,
        "end_date": end_date,
        "page": page,
        "page_size": page_size
    }

    if not conditions:
        conditions = {
            "media_project_id": [],
            "advertiser_id": [],
            "media_type": "",
            "project_id": [],
            "owner_user_id": [],
            "media_agent_id": [],
            "time_line": time_line
        }
    if not kpis:
        kpis = [
            "aggregate_cost"
        ]
    if not relate_dims:
        relate_dims = [
            "owner_user_id",
            "media_type"
        ]

    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    data["conditions"] = conditions
    data["kpis"] = kpis
    data["relate_dims"] = relate_dims
    return lazyrequests.lazy_requests(
        method="POST",
        url=url,
        json=data,
        headers=headers
    )


def get_material_detail(
        cookie: str,
        material_id: str,
):
    """
    获取素材详情
    :param cookie:
    :param material_id: 素材ID
    :return:
    """
    url = "https://cli2.mobgi.com/Material/Manage/detail"
    data = {
        "material_id": material_id
    }
    headers = copy.deepcopy(default_headers)
    headers["Cookie"] = cookie
    return lazyrequests.lazy_requests(
        method="GET",
        url=url,
        params=data,
        headers=headers
    )
