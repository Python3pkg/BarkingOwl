import ConfigParser

import __dbcreds__

import MySQLdb as mdb
import _mysql as mysql
try:
    con = mdb.connect(host   = __dbcreds__.__server__,
                      user   = __dbcreds__.__username__,
                      passwd = __dbcreds__.__password__,
                      db     = __dbcreds__.__database__,
                     )
except Exception,e:
    raise Exception("sql2api error - could not connect to the database:\n\n\t{0}".format(e))


from Users import Users
from Userinfo import Userinfo
from Orgs import Orgs
from Urls import Urls
from Userurls import Userurls
from Phrases import Phrases
from Urlphrases import Urlphrases
from Runs import Runs
from Scrapes import Scrapes
from Docs import Docs
from Finds import Finds

