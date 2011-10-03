# Database Schema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

import db_defaults

# Declares the base
base = declarative_base()

# Tables
class Video(base):
	__tablename__ = 'videos'

	id = Column('video_id', Integer, primary_key = True)
	name = Column('video_name', String(255))
	description = Column('video_description', Text)
	lecturer_name = Column('video_lecturer_name', String(255))

	def __init__(self, name, description, lecturer_name):
		self.name = name
		self.description = description
		self.lecturer_name = lecturer_name

class Task(base):
	__tablename__ = 'tasks'

	id = Column('task_id', Integer, primary_key = True)
	name = Column('task_name', String(255))
	description = Column('task_description', Text)

	def __init__(self, name, description):
		self.name = name
		self.description = description

class Progress_indicator(base):
	__tablename__ = 'progress_indicators'

	id = Column('progress_indicator_id', Integer, primary_key = True)
	video = Column('progress_indicator_video', Integer, ForeignKey('videos.video_id'))
	task = Column('progress_indicator_task', Integer, ForeignKey('tasks.task_id'))

	def __init__(self, video, task):
		self.video = video
		self.task = task

class Meta_attribute(base):
	__tablename__ = 'meta_attributes'

	id = Column('meta_attribute_id', Integer, primary_key = True)
	key = Column('meta_attribute_key', String(255))
	value = Column('meta_attribute_value', String(255))

	def __init__(self, key, value):
		self.key = key
		self.value = value

# Reusable Functions
def Init_project(foldername, unit_coordinator, unit_name):
	engine = create_engine('sqlite:///'+foldername+'/project.sqlite')
	base.metadata.create_all(engine)

	# Open up database session
	Session = sessionmaker(bind=engine)
	session = Session()

	# Apply defaults
	tasks = db_defaults.Task_defaults

	for t in tasks:
		db_task = Task(t['name'], t['description'])
		session.add(db_task)

	# Apply initial meta attributes
	session.add_all([
		Meta_attribute('unit_coordinator', unit_coordinator),
		Meta_attribute('unit_name', unit_name)
		])

	# Commit all changes to db
	session.commit()
