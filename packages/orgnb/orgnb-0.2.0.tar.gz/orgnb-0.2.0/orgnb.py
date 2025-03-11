#!/usr/bin/env python

import copy
import base64
import re
import os

"""
Convert org mode file as jupyter notebook.
"""

# The following does not transform code blocks into code cells
# output = pypandoc.convert_file(sys.argv[1],
#                                to='ipynb',
#                                format='org')


def parse_headlines_org_file(headlines, file_handle):
    """
    Extract headlines from `file_handle`.

    Parameters:
    ----------
    - headlines : list of headlines
    - file_handle : input org mode file

    Return:
    ------
    - list of headlines
    """
    state = True
    text = []
    for line in file_handle:
        line = line.strip('\n')
        if line.startswith('* '):
            headline = line.split('* ')[1]
            state = False
            for selected_headline in headlines:
                if headline == selected_headline:
                    state = True
                    break
        if state:
            text.append(line)

    return text


def parse_org_file(file_handle):
    """
    Extract code and text blocks from `file_handle`.

    Parameters:
    ----------
    - file_handle : input org mode file

    Return:
    ------
    - list of blocks
    - list of block types
    """
    # TODO: remove cells_type in favor of cella_meta    
    cells, cells_type, cells_meta, block = [], [], [], []
    state = None
    line, prev, meta, name = '', '', {}, ''
    for line in file_handle:
        line = line.strip('\n')

        if line.startswith('#+name'):
            # Store name of next block
            # assert 'name' not in meta, 'there should be no name'
            assert len(name) == 0
            name = line.split(':')[1].strip()
        
        elif line.startswith('#+begin'):
            # We store the current block as text
            # unless all lines are empty
            non_empty = sum([len(_) > 0 for _ in block])
            if non_empty > 0:
                cells.append(block)
                cells_type.append('text')
                meta['type'] = 'text'
                cells_meta.append(copy.copy(meta))

            # Reading a new code block
            block = []
            meta = {}
            state = line[8:]  # strip #+begin
            if len(line.split()) > 1:
                state = line.split()[1]
            if prev.startswith('#+attr_rst: :directive'):
                state = prev.split()[-1]
            meta['type'] = state
            # meta['name'] = name

        elif line.startswith('#+end'):
            # We store the current block as code
            assert state != 'text'
            if state in ['example', 'quote']:
                block.insert(0, '```')
                block.append('```')
            if name:
                meta['name'] = name
            cells.append(block)
            cells_type.append(state)
            cells_meta.append(copy.copy(meta))
            # Reading a new text block. If there are consecutive code
            # blocks, empty text blocks are removed.
            block = []
            state = 'text'
            name = ''
            meta = {'type': state}

        elif ':ARCHIVE:' in line or line.startswith('#+') or line.startswith(':'):
            # Skip results blocks
            pass

        else:
            # This is a text block
            if state is None:
                block = []
                name = ''
                state = 'text'
                meta = {}
            block.append(line)

        prev = line

    if len(block) > 0:
        cells.append(block)
        cells_type.append('text')
        meta['type'] = 'text'
        if name:
            meta['name'] = name
        cells_meta.append(meta)
        
    return cells, cells_type, cells_meta

def insert_noweb(cell, cells, cells_meta, strip=False):
    # TODO: pop lines
    # Check if there is noweb
    def _has_noweb(cell):
        for i, line in enumerate(cell):
            match = re.search(r'<<(\S*)>>', line)
            if match:
                return i, match.group(1)
        return -1, ''

    while True:
        line, name = _has_noweb(cell)
        if line < 0:
            return cell

        cell.pop(line)
        if strip:
            continue
        
        # TODO: use dict for named cells
        for other, meta in zip(cells, cells_meta):
            if 'name' in meta and meta['name'] == name:
                for o in other[-1::-1]:
                    cell.insert(line, o)
            
    return cell

def convert_to_text(cells, cells_type, cells_meta, file_out, dir_inp, include=None, exclude=None, noweb_strip=False):
    """
    Write cells to stdout

    Parameters:
    ----------
    - cells : list of cells
    - cells_type : list of types of cells (text or code)
    """
    # print(len(cells), len(cells_type))
    # for e, m, tt in zip(cells, cells_meta, cells_type):
    #    print(m, tt)

    for e, m in zip(cells, cells_meta):
        t = m['type']
        if t == 'text':
            print('\n'.join(e))
        else:
            line = '-' * 64
            print(line[:-len(t)] + t)
            e = insert_noweb(e, cells, cells_meta, noweb_strip)
            print('\n'.join(e))
            print('-' * 64)


def attach_images(block, dir_inp):
    """
    Attach images in markdown broken links like (`![](...)`) as
    attachments and fix the link.
    """
    new_block = []
    attachments = {}
    for line in block.split('\n'):
        if line.startswith('![]'):
            match = re.search(r'!\[\]\((\S*)\)', line)
            file_path = match.group(1)
            if file_path.startswith('file:'):
                file_path = file_path.strip[5:]
            line = f'![{file_path}](attachment:{file_path})'
            full_path = os.path.join(dir_inp, file_path)            
            if not os.path.exists(full_path):
                print('skip missing file image', full_path)
                continue
            try:
                # First encode image in base64, then attach it
                image = open(full_path, "rb").read()
                image = base64.b64encode(image)
                image = image.decode('utf-8')
                attachments[file_path] = {'image/png': image}
            except UnicodeDecodeError:
                print(f'Error: attachment {full_path}')
                continue
            attachments[file_path] = {'image/png': image}
        new_block.append(line)
    block = '\n'.join(new_block)
    return block, attachments


def convert_to_nb(cells, cells_type, cells_meta, file_out, dir_inp, include=None, exclude=None, noweb_strip=False):
    """
    Convert list of cells to jupyter notebook format

    Parameters:
    ----------
    - cells : list of cells
    - cells_type : list of types of cells (text or code)
    - file_out : path to output notebook file
    """
    import nbformat
    nb = nbformat.v4.new_notebook()
    for e, t in zip(cells, cells_type):
        if (include and t not in include) or (exclude and t in exclude):
            continue
        if t == 'text':
            # This is a text block
            from pypandoc import convert_text
            block = '\n'.join(e)
            block = convert_text(block, 'markdown-simple_tables+grid_tables', 'org')
            # Fix generic verbatim code blocks
            block = re.sub('\{.verbatim\}', '', block)
            block, attachments = attach_images(block, dir_inp)
            nb['cells'].append(nbformat.v4.new_markdown_cell(source=block, attachments=attachments))
        elif t == 'python':
            # This is a python code block
            e = insert_noweb(e, cells, cells_meta, noweb_strip)
            block = '\n'.join(e)
            nb['cells'].append(nbformat.v4.new_code_cell(source=block))
        elif t == 'sh' or t == 'bash':
            # This is a shell block, we add ! to the beginning of the lines
            block = '\n'.join(['! '+ line for line in e])
            nb['cells'].append(nbformat.v4.new_code_cell(source=block))
        elif t == 'fortran':
            # This includes example and quote blocks
            block = '\n'.join(e)
            block = '```\n' + block + '\n' + '```\n'
            nb['cells'].append(nbformat.v4.new_markdown_cell(source=block))
        elif t in ['example', 'quote', 'results']:
            # This includes example and quote blocks
            block = '\n'.join(e)
            nb['cells'].append(nbformat.v4.new_markdown_cell(source=block))
        #elif t in ['warning', 'note']:
        else:
            # This is an rst admonition block
            e.insert(0, '**' + t.capitalize() + '**:')
            block = '\n'.join(e)
            block = convert_text(block, 'markdown-simple_tables+grid_tables', 'org')
            nb['cells'].append(nbformat.v4.new_markdown_cell(source=block))

    nbformat.write(nb, file_out)


def main(debug=False, include='', exclude='ditaa', noweb_strip=False, *files):
    convert = convert_to_nb
    if debug:
        convert = convert_to_text

    for file_inp in files:
        if debug:
            file_out = '/dev/stdout'
        else:
            file_out = file_inp[:-4] + '.ipynb'
        with open(file_inp) as fh:
            cells, cells_type, cells_meta = parse_org_file(fh)
            convert(cells, cells_type, cells_meta, file_out, os.path.dirname(fh.name), include, exclude, noweb_strip=noweb_strip)

def cli():
    import argh
    argh.dispatch_command(main)


if __name__ == '__main__':
    import argh
    argh.dispatch_command(main)
