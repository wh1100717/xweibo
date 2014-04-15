#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import web
from controller import SinaController

urls = (
    '/api/sina',SinaController.app,
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()