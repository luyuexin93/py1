#！/bin/env/python3
# -*- coding: utf-8 -*-

#pickle module related
import pickle

with open( "hero.txt", "wb" ) as f:
    f.write( pickle.dumps( "美好的事情即将发生" ) )
with.open( "hero.txt", "rb" ) as f:
    pickle.loads( f.read() )

with.open( "bro.txt", "wb" ) as f:
    pickle.dump( "美好的事情即将发生", f ) 
with.open( "bro.txt", "rb" ) as f:
    pickle.load( f )


#json module related

import json

with open( "a.txt", "w" ) as f:
    f.write( json.dumps( { "name": "xiaohei" } ) )
with.open( "a.txt", "r" ) as f:
    json.loads( f.read() )

with open( "b.txt", "w" ) as f:
    json.dump( { "name": "xiaohei" } )
with open( "b.txt", "r" ) as f:
    json.loas( f )


#练习
# -*- coding: utf-8 -*-

import json      

obj = dict(name='小明', age=20)
#s = json.dumps( obj )
#{"name": "\u5c0f\u660e", "age": 20} 
s = json.dumps( obj, ensure_ascii = False )
#{"name": "小明", "age": 20} 

#json.dumps() 中参数ensure_ascii默认值为True，是否对中文进行ascii编码
```