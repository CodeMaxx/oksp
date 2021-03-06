# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 20:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('intime', models.DateTimeField(blank=True,
                                                null=True)),
                ('outtime', models.DateTimeField(blank=True,
                                                 null=True)),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ], ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('roll', models.CharField(blank=True,
                                          max_length=9,
                                          null=True)),
                ('sex', models.CharField(blank=True,
                                         choices=[('male', 'Male'),
                                                  ('female', 'Female'),
                                                  ('other', 'Other')],
                                         max_length=10,
                                         null=True)),
                ('password', models.CharField(blank=True,
                                              max_length=50,
                                              null=True)),
                ('contact', models.CharField(blank=True,
                                             max_length=12,
                                             null=True)),
                ('hostel', models.CharField(
                    blank=True,
                    choices=[
                        ('Hostel 1', 'Hostel 1'), ('Hostel 2', 'Hostel 2'),
                        ('Hostel 3', 'Hostel 3'), ('Hostel 4', 'Hostel 4'),
                        ('Hostel 5', 'Hostel 5'), ('Hostel 6', 'Hostel 6'),
                        ('Hostel 7', 'Hostel 7'), ('Hostel 8', 'Hostel 8'),
                        ('Hostel 9', 'Hostel 9'), ('Hostel 10', 'Hostel 10'),
                        ('Hostel 11', 'Hostel 11'), ('Hostel 12', 'Hostel 12'),
                        ('Hostel 13', 'Hostel 13'), ('Hostel 14', 'Hostel 14'),
                        ('Hostel 15', 'Hostel 15'), ('Tansa', 'Tansa'),
                        ('QIP', 'QIP')
                    ],
                    max_length=20,
                    null=True)),
                ('room', models.CharField(blank=True,
                                          max_length=5,
                                          null=True)),
                ('discipline', models.CharField(
                    blank=True,
                    choices=[
                        ('Aerospace Engineering', 'Aerospace Engineering'),
                        ('Animation', 'Animation'), (
                            'Application Software Centre',
                            'Application Software Centre'),
                        ('Applied Geophysics', 'Applied Geophysics'), (
                            'Applied Statistics and Informatics',
                            'Applied Statistics and Informatics'),
                        ('Biomedical Engineering', 'Biomedical Engineering'), (
                            'Biosciences and Bioengineering',
                            'Biosciences and Bioengineering'),
                        ('Biotechnology', 'Biotechnology'),
                        ('Centre for Aerospace Systems Design and Engineering',
                         'Centre for Aerospace Systems Design and Engineering'
                         ),
                        ('Centre for Distance Engineering Education Programme',
                         'Centre for Distance Engineering Education Programme'
                         ),
                        ('Centre for Environmental Science and Engineering',
                         'Centre for Environmental Science and Engineering'),
                        ('Centre for Formal Design and Verification of Software',
                         'Centre for Formal Design and Verification of Software'
                         ),
                        ('Centre for Research in Nanotechnology and Science',
                         'Centre for Research in Nanotechnology and Science'),
                        ('Centre for Technology Alternatives for Rural Areas',
                         'Centre for Technology Alternatives for Rural Areas'),
                        ('Centre for Urban Science and Engineering',
                         'Centre for Urban Science and Engineering'), (
                             'Centre of Studies in Resources Engineering',
                             'Centre of Studies in Resources Engineering'),
                        ('Chemical Engineering',
                         'Chemical Engineering'), ('Chemistry', 'Chemistry'), (
                             'Civil Engineering', 'Civil Engineering'), (
                                 'Climate Studies', 'Climate Studies'), (
                                     'Computer Centre', 'Computer Centre'), (
                                         'Computer Science & Engineering',
                                         'Computer Science & Engineering'),
                        ('Continuing Education Programme',
                         'Continuing Education Programme'), (
                             'Corrosion Science and Engineering',
                             'Corrosion Science and Engineering'), (
                                 'Desai Sethi Centre for Entrepreneurship',
                                 'Desai Sethi Centre for Entrepreneurship'), (
                                     'Earth Sciences', 'Earth Sciences'),
                        ('Educational Technology', 'Educational Technology'),
                        ('Electrical Engineering', 'Electrical Engineering'), (
                            'Energy Science and Engineering',
                            'Energy Science and Engineering'), (
                                'Humanities & Social Science',
                                'Humanities & Social Science'), (
                                    'IITB-Monash Research Academy',
                                    'IITB-Monash Research Academy'), (
                                        'Industrial Design Centre',
                                        'Industrial Design Centre'),
                        ('Industrial Design Centre',
                         'Industrial Design Centre'), (
                             'Industrial Engineering and Operations Research',
                             'Industrial Engineering and Operations Research'),
                        ('Industrial Management', 'Industrial Management'), (
                            'Interaction Design', 'Interaction Design'),
                        ('Kanwal Rekhi School of Information Technology',
                         'Kanwal Rekhi School of Information Technology'), (
                             'Material Science', 'Material Science'), (
                                 'Materials, Manufacturing and Modelling',
                                 'Materials, Manufacturing and Modelling'), (
                                     'Mathematics', 'Mathematics'),
                        ('Mechanical Engineering', 'Mechanical Engineering'), (
                            'Metallurgical Engineering & Materials Science',
                            'Metallurgical Engineering & Materials Science'), (
                                'Mobility and Vehicle Design',
                                'Mobility and Vehicle Design'),
                        ('National Centre for Aerospace Innovation and Research',
                         'National Centre for Aerospace Innovation and Research'
                         ), ('National Centre for Mathematics',
                             'National Centre for Mathematics'), (
                                 'Physical Education',
                                 'Physical Education'), ('Physics', 'Physics'),
                        ('Physics, Material Science',
                         'Physics, Material Science'), ('Preparatory Course',
                                                        'Preparatory Course'),
                        ('Reliability Engineering', 'Reliability Engineering'),
                        ('Shailesh J. Mehta School of Management',
                         'Shailesh J. Mehta School of Management'), (
                             'Sophisticated Analytical Instrument Facility',
                             'Sophisticated Analytical Instrument Facility'), (
                                 'Systems and Control Engineering',
                                 'Systems and Control Engineering'),
                        ('Tata Center for Technology and Design',
                         'Tata Center for Technology and Design'), (
                             'Visual Communication', 'Visual Communication'), (
                                 'Wadhwani Research Centre for Bioengineering',
                                 'Wadhwani Research Centre for Bioengineering')
                    ],
                    max_length=100,
                    null=True)),
                ('join_year',
                 models.CharField(blank=True,
                                  choices=[('2010', '2010'), ('2011', '2011'),
                                           ('2012', '2012'), ('2013', '2013'),
                                           ('2014', '2014'), ('2015', '2015'),
                                           ('2016', '2016')],
                                  max_length=4,
                                  null=True)),
                ('graduation_year',
                 models.CharField(blank=True,
                                  choices=[('2015', '2015'), ('2016', '2016'),
                                           ('2017', '2017'), ('2018', '2018'),
                                           ('2019', '2019'), ('2020', '2020'),
                                           ('2021', '2021')],
                                  max_length=4,
                                  null=True)),
                ('degree', models.CharField(
                    blank=True,
                    choices=[('Bachelor of Technology',
                              'Bachelor of Technology'),
                             ('Master of Technology', 'Master of Technology'),
                             ('B.Tech. + M.Tech. Dual Degree',
                              'B.Tech. + M.Tech. Dual Degree'),
                             ('Master of Science', 'Master of Science'),
                             ('Doctor of Philosophy', 'Doctor of Philosophy'),
                             ('Bachelor of Design', 'Bachelor of Design'),
                             ('Master of Design', 'Master of Design'),
                             ('Master of Philosophy', 'Master of Philosophy'),
                             ('Master of Management', 'Master of Management'),
                             ('M.S. (Exit Degree)', 'M.S. (Exit Degree)'), (
                                 'Master of Technology (Exit Degree)',
                                 'Master of Technology (Exit Degree)'), (
                                     'M.Tech. + Ph.D. Dual Degree',
                                     'M.Tech. + Ph.D. Dual Degree'),
                             ('Preparatory Course', 'Preparatory Course'),
                             ('Visiting Student', 'Visiting Student'), (
                                 'Master of Philosophy (Exit Degree)',
                                 'Master of Philosophy (Exit Degree)'), (
                                     'Master of Science (Exit Degree)',
                                     'Master of Science (Exit Degree)'), (
                                         'M.Sc. + Ph.D. Dual Degree',
                                         'M.Sc. + Ph.D. Dual Degree'), (
                                             'M.Phil. + Ph.D. Dual Degree',
                                             'M.Phil. + Ph.D. Dual Degree'), (
                                                 'Executive MBA',
                                                 'Executive MBA'), (
                                                     'Four Year BS',
                                                     'Four Year BS'),
                             ('Integrated M.Tech.', 'Integrated M.Tech.'), (
                                 'Master of Science By Research',
                                 'Master of Science By Research'), (
                                     'Two Year M.Sc.', 'Two Year M.Sc.'), (
                                         'Five Year Integrated M.Sc.',
                                         'Five Year Integrated M.Sc.'), (
                                             'D.I.I.T.', 'D.I.I.T.'), (
                                                 'D.I.T.T. (Exit Degree)',
                                                 'D.I.T.T. (Exit Degree)')],
                    max_length=50,
                    null=True)),
                ('current_status', models.CharField(blank=True,
                                                    choices=[('IN', 'IN'),
                                                             ('OUT', 'OUT')],
                                                    max_length=5,
                                                    null=True)),
                ('secondary_email', models.CharField(blank=True,
                                                     max_length=50,
                                                     null=True)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('access_token', models.TextField()),
                ('current_log', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='account.Log')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ], ),
    ]
