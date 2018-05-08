import web

urls = (
    '/','Index')
app = web.application(urls,globals())
render = web.template.render('C:/Python27/workplace/myweb/gothonweb/templates/')



class Index(object):
    def GET(self):
        greeting="Hello world"
        return render.index(greeting = greeting)
    
if __name__ == "__main__" :
    app.run() 