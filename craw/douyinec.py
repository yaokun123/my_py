# coding: utf-8


class Dyec(object):

    def __init__(self):
        self.page_size = 30
        self.base_doamin = "https://buyin.jinritemai.com/pc/selection/common/material_list"

    def run(self):
        pass

    def get_base_uri(self):
        # verifyFp 和 fp 值相同，且分页不变
        # msToken 和 a_bogus 分页就变
        query_params = {
            "verifyFp": "verify_lzt6bjbg_nDsGiprv_nU8h_4f1G_AqMl_kvKOjB4Zj1ve",
            "fp": "verify_lzt6bjbg_nDsGiprv_nU8h_4f1G_AqMl_kvKOjB4Zj1ve",
            "msToken": "wsIac-xvAgWcmPmo_YWeeAMqCTICgZvGApsQ1TYCfK50VMFcx4kciVqd1jMOrTUsKz-ZJszCx86YRmfA065h9CVwdm-mwVhO3ZpSjyhYsomYW_1ilfaS",
            "a_bogus": "E7WwQDL6Dk2TgDuD5WOLfY3qfbGJYMey0SVkMDgbhEAAXy39HMO69exY9UJvqJgjN4/kIeyjy4hbTNKhrQQn8Hwf9uhL/2AkmfSsSPPg-nSSs1feeLbQrsJO4kY3SFlm5XNAEOJ0y75tFbJ0l9o7mhK4bfebYyDWxp6Fa31oxE=="
        }

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
                "search_id": "e49d85971bb8c7a565fd0aedc9fdb80e33e4e1e52bc7d06b23d6263d195350872c7b268d3afebbdb1318f34f3b5d3739d905bc3538b8cffea93d2419416ac96fd58cad2d30f82747fa72df05effac8d5",
                "session_id": "2240ef2d8a855155c5a83bb0482ffccf197cd99dd99017347d914442b8d79bf1fcb027e2011890e2a526d422cc06e55d1e1bf3a83ca5f2a2e88590def8139afd49e13f4311d642acedffe142b6bb6426"
            },
            "filters": {}
        }
        return body


if __name__ == "__main__":

    Dyec().run()