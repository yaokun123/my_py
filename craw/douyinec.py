# coding: utf-8
import urllib
import requests


class Dyec(object):

    def __init__(self):
        self.page_size = 30
        self.base_doamin = "https://buyin.jinritemai.com/pc/selection/common/material_list"

    def run(self):
        url = self.get_base_uri()
        body = self.get_request_body("油污净")

        headers = {

            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        res = requests.post(url, data=body, headers=headers, cookies=cookie)
        print res.status_code
        print res.content

    def get_base_uri(self):
        # verifyFp 和 fp 值相同，且分页不变
        # msToken 和 a_bogus 分页就变
        query_params = {
            "verifyFp": "verify_lzt8v23c_5hkouaUM_3ejc_4XKQ_9AAO_u6jCZ2UDfXue",
            "fp": "verify_lzt8v23c_5hkouaUM_3ejc_4XKQ_9AAO_u6jCZ2UDfXue",
            "msToken": "XDXTQN0kGCw3_QLp4oj_hKSP6f7vF0Aw3xSBKTGyIqfj0D28-53Snx-QQFMd2M8B4IuWJlPDvsv5HmWZL7IWm2iYsoqtgmie4OaJ7EYUwvSUaAjUg8ZE",
            "a_bogus": "Q68wQQhfDk2PDf8X5WOLfY3qfrThYMC90SVkMDgbbPKAJL39HMP89exY94GvpLLjN4/kIejjy4hbTNKhrQA90qwf9uhL/2AkmfSDtlQQ524j53iruyRkrzDF4v4-Feep5JV3EcvhqJKcKmuZ09O7-JIlO6ZCcHgjxiSmtn3Fv3u="
        }

        query_string = urllib.urlencode(query_params)
        return self.base_doamin+"?"+query_string

    def get_request_body(self, search_text, page=1):
        cursor = (page - 1) * self.page_size

        # search_id 和 session_id分页不变
        body = {
            "scene": "PCSquareSearch",
            "size": self.page_size,
            "search_text": search_text,
            "cursor": cursor,
            "extra": {
                "new_session_strategy": 1,
                "search_id": "2240ef2d8a855155c5a83bb0482ffccf197cd99dd99017347d914442b8d79bf1fcb027e2011890e2a526d422cc06e55dd151ca1f39a6c46a4fa745789af156f84c4ca95dbab4f9aa75cb0c5db19b44f4",
                "session_id": "2240ef2d8a855155c5a83bb0482ffccf197cd99dd99017347d914442b8d79bf1fcb027e2011890e2a526d422cc06e55dd151ca1f39a6c46a4fa745789af156f84c4ca95dbab4f9aa75cb0c5db19b44f4"
            },
            "filters": {}
        }
        return body


if __name__ == "__main__":

    Dyec().run()