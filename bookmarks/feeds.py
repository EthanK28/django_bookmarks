# encoding: utf-8

__author__ = 'Eunseok'

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from bookmarks.models import Bookmark

class RecentBookmarks(Feed):
    title = u'장고 북마크 | 최신 북마크'
    link = '/feeds/recent/'
    description = u'장고 부가크 서비스를 토해서 등록된 북마크 '

def items(self):
    return Bookmark.objects.order_by('-id')[:10]



