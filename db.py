# Database Schema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

import defaults

# Declares the base
base = declarative_base()

# Tables
class Video(base):
	__tablename__ = 'videos'

	id = Column('video_id', Integer, primary_key = True)
	name = Column('video_name', String(255))
	description = Column('video_description', Text)
	lecturer_name = Column('video_lecturer_name', String(255))

	def __init__(self, name, lecturer_name, description):
		self.name = name
		self.lecturer_name = lecturer_name
		self.description = description

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
	completed = Column('progress_indicator_completed', Boolean)

	def __init__(self, video, task):
		self.video = video
		self.task = task
		self.completed = False

class Meta_attribute(base):
	__tablename__ = 'meta_attributes'

	id = Column('meta_attribute_id', Integer, primary_key = True)
	key = Column('meta_attribute_key', String(255))
	value = Column('meta_attribute_value', String(255))

	def __init__(self, key, value):
		self.key = key
		self.value = value

# Reusable Functions

# Starts up a database session
def start_session(foldername):
	engine = create_engine('sqlite:///'+foldername+'/project.sqlite')
	Session = sessionmaker(bind=engine)
	return Session()

# Initialises project and creates empty sqlite database with defaults applied
def Init_project(foldername, unit_coordinator, unit_name):
	engine = create_engine('sqlite:///'+foldername+'/project.sqlite')
	base.metadata.create_all(engine)

	session = start_session(foldername)

	# Apply defaults
	tasks = defaults.Task_defaults

	for t in tasks:
		session.add(Task(t['name'], t['description']))

	# Apply initial meta attributes
	session.add_all([
		Meta_attribute('unit_coordinator', unit_coordinator),
		Meta_attribute('unit_name', unit_name)
		])

	# Commit all changes to db
	session.commit()
	
# Initialises video and creates incomplete tasks
def Init_video(foldername, video_name, lecturer_name):
	session = start_session(foldername)

	# Creates video and commits to db
	video = Video(video_name, lecturer_name, '')
	session.add(video)
	session.commit()

	# Gets all tasks
	tasks = session.query(Task)
	for t in tasks:
		session.add(Progress_indicator(video.id, t.id))
	session.commit()
