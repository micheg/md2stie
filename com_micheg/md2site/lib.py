# libs
import os
import shutil
import json
from datetime import datetime
# deps
from jinja2 import Environment, PackageLoader
from markdown2 import markdown

HOME_TEMPLATE = 'home.html'
DOC_TEMPLATE = 'post.html'
STATIC_DIR = 'static'

class Staticizer:
    'static site generator'
    
    def __init__(self, template_dir, public_dir, input_dir, output_dir, LOG=None):
        self.LOG = LOG
        self.template_dir = template_dir
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.public_dir = public_dir
        # making output dir
        isExist = os.path.exists(self.output_dir)
        if not isExist:
            os.makedirs(self.output_dir)
        # loading templates
        self.env = self.load_templates()
        # parsing documents
        self.DOCS = self.read_all_items()
      
    def copy_static_files(self):
        subfolders = [ os.path.basename(os.path.normpath(f.path)) for f in os.scandir(self.public_dir) if f.is_dir() ]
        for _dir in subfolders:
            _src_dir = os.path.join(self.public_dir, _dir)
            _tgt_dir = os.path.join(self.output_dir, STATIC_DIR, _dir)
            shutil.copytree(_src_dir, _tgt_dir, dirs_exist_ok=True)
    
    def read_all_items(self):
        DOCS = {}
        'read all content from files'
        for md_file in os.listdir(self.input_dir):
            file_path = os.path.join(self.input_dir, md_file)

            with open(file_path, 'r') as _file:
                DOCS[md_file] = markdown(_file.read(), extras=['metadata', 'fenced-code-blocks'])

        DOCS = {
            item: DOCS[item] for item in sorted(DOCS, key=lambda item: datetime.strptime(DOCS[item].metadata['date'], '%Y-%m-%d'), reverse=True)
        }
        
        return DOCS

    def load_templates(self):
        return Environment(loader=PackageLoader('main', self.template_dir))

    def render_home(self):
        DOCS = self.DOCS
        home_template = self.env.get_template('home.html')

        DOCS_metadata = [DOCS[item].metadata for item in DOCS]
        tags = [item['tags'] for item in DOCS_metadata]
        #import pdb; pdb.set_trace()
        home_html = home_template.render(DOCS=DOCS_metadata, tags=tags)

        with open('{output_dir}/index.html'.format(output_dir=self.output_dir), 'w') as file:
            file.write(home_html)

    def render_files(self):
        DOCS = self.DOCS
        json_data = []
        post_template = self.env.get_template('post.html')
        for item in DOCS:
            post_metadata = DOCS[item].metadata

            post_data = {
                'content': DOCS[item],
                'title': post_metadata['title'],
                'date': post_metadata['date'],
            }
            
            json_data.append(
            {
                'title': post_metadata['title'],
                'subtitle': post_metadata['subtitle'],
                'tags': post_metadata['tags'],
                'date': post_metadata['date'],
                'summary': post_metadata['summary'],
                'slug': post_metadata['slug'],
            })

            post_html = post_template.render(post=post_data)

            post_file_path = '{output_dir}/article/{slug}.html'.format(slug=post_metadata['slug'], output_dir=self.output_dir)

            os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
            with open(post_file_path, 'w') as file:
                file.write(post_html)
        
        json_file_name = os.path.join(self.output_dir, 'data.json')
        with open(json_file_name, 'w') as json_file:
            json.dump(json_data, json_file)
