import time

from shangjian_api.airworks.package_api import AirWorksApi
import json

while 1:

    awp = AirWorksApi(
        base_url="poc.airworks.shangjian.tech:30000",
        access_key="352UKzc5Qkc_10",
        access_secret="aDySVRfe0eMAfp1ZTjB36w",
        default_app_id=49,
    )

    res = awp.mall(
        shop_id="", shop_name="", state="1", page_num=1, page_size=10, api_method="GET"
    )

    print(json.dumps(res, indent=2, ensure_ascii=False))
    time.sleep(0.5)
