# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-19 19:52
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify

slugmap = {
    'Applications and Real-Time Area': 'area-art',
    'Applying IP Flow Information Export (IPFIX) to Network Measurement and Management': 'ipfix',
    'General Area': 'area-gen',
    'IESG-MailingList': 'iesg-stmt-mailinglist',
    'IESG-Meetings': 'iesg-stmt-meetings',
    'IESG-Procedures': 'iesg-stmt-procedures',
    'IESG-Technical': 'iesg-stmt-technical',
    'IETF-LLC': 'ietf-llc',
    'Internet Area': 'area-int',
    'Internet of Things': 'iot',
    'News': 'news',
    'Operations and Management Area': 'area-ops',
    'Real-time Communications': 'rtc',
    'Routing Area': 'area-rtg-unused',
    'Routing Area (rtg)': 'area-rtg',
    'Security & Privacy': 'security-and-privacy',
    'Security Area': 'area-sec-unused',
    'Security Area (sec)': 'area-sec',
    'Transport Area': 'area-tsv-unused',
    'Transport Area (tsv)': 'area-tsv',
}

def forward(apps, schema_editor):
    SecondaryTopic = apps.get_model('snippets.SecondaryTopic')
    for st in SecondaryTopic.objects.all():
        st.slug = slugmap.get(st.title, slugify(st.title))
        st.save()


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0029_secondarytopic_slug'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]

"""
2 : Applications and Real-Time Area
0 : Applying IP Flow Information Export (IPFIX) to Network Measurement and Management
1 : General Area
6 : IESG-MailingList
5 : IESG-Meetings
21 : IESG-Procedures
8 : IESG-Technical
4 : IETF-LLC
0 : Internet Area
2 : Internet of Things
19 : News
1 : Operations and Management Area
0 : Real-time Communications
0 : Routing Area
0 : Routing Area (rtg)
0 : Security & Privacy
0 : Security Area
4 : Security Area (sec)
0 : Transport Area
1 : Transport Area (tsv)
"""
