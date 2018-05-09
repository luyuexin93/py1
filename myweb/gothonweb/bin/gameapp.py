#-*- coding:utf-8 -*-
import web
import sys
sys.path.append('C:/Python27/workplace/myweb/gothonweb/gothonweb')
import map

urls = (
    '/game','GameEngine',
    '/','Index')
app = web.application(urls,globals())


# little hack so that debug mode works with sessions
if web.config.get('_session')is None:
    store=web.session.DiskStore('C:/Python27/workplace/myweb/gothonweb/sessions')
    session=web.session.Session(app,store)
    web.config._session=session
else:
    session = web.config._session
    
render = web.template.render('C:/Python27/workplace/myweb/gothonweb/templates/',base="layout")




class Index(object):
    def GET(self):
        #this is used to "setup" the session with starting values
        session.room = map.START
        session.put=None
        web.seeother("/game")
    
class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room,put=session.put)
        else:
            # why is there here? do you need it ?
             return render.you_died()
    
    def POST(self):
        form = web.input(action=None)
        #there is a bug here,can you fix it?
        if session.room and form.action:
            if (session.room !=map.the_end_winner or session.room !=map.the_end_loser):
                session.room = session.room.go(form.action)
                session.put=form.action
        
        web.seeother("/game")



if __name__ == "__main__" :
    app.run() 