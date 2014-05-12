#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import web
from controller import SinaController
render = web.template.render('templates/',base='layout')
# render_without_layout = web.template.render('templates/')
urls = (
    '/sina',SinaController.app,
    '/friends/', 'friend',
    '/userinfo/','userinfo',
    '/','home',
    '/micro-bo/','microbo',
    '/influence/','influence'
)

class friend:
    def GET(self):
        return render.friends()

class home:
	def GET(self):
		return render.home()
class influence:
    def GET(self):
        return render.influence()

class userinfo:
    def GET(self):
        return render.userinfo()
class microbo:
    def GET(self):
        return render.microbo()
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()