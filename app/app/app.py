#!/usr/bin/env python
# -*- coding: utf-8 -*-

import responder

api = responder.API()

@api.route("/")
def hello_world(req, resp, *, hoge):
    resp.text = "Hello, world!"

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
