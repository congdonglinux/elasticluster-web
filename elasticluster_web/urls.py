#! /usr/bin/env python
#
# Copyright (C) 2013 GC3, University of Zurich
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
__author__ = 'Nicolas Baer <nicolas.baer@uzh.ch>, Antonio Messina <antonio.s.messina@gmail.com>'


from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # account
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),
    (r'^accounts/logout$', 'django.contrib.auth.views.logout_then_login'),
    (r'^password_change$', 'django.contrib.auth.views.password_change', {'template_name': 'auth/password_change.html'}),
    (r'^password_change_done$', 'django.contrib.auth.views.password_change_done'),

    # home
    url(r'^$', 'elasticluster_base.views.index', name='index'),

)