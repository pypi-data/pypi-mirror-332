# Copyright (c) NCC Group, 2018-2020
# Copyright (c) Google LLC., 2024
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import argparse
import sys
import os
import string
import re
import shlex

args = None

# bytes don't have format() b/c python3 sucks, so we emulate it
cmake_template = b'''\
cmake_minimum_required(VERSION 3.9)
project({project_name})

set(CMAKE_CXX_STANDARD 11)

{compiler_defs}

include_directories(SYSTEM
  {system_includes}
)

include_directories(
  {includes}
)

add_executable({project_name}
  {src_files}
)
'''

compiler_defs_template = '''\
add_compile_definitions(
  {vals}
)'''

def raw_print(b):
  sys.stdout.buffer.write(b)
  sys.stdout.buffer.write(b'\n')

def parse_args():
  parser = argparse.ArgumentParser(
    description='Generates 3 (generally non-buildable) cmake files ' +
                'to support code indexing.'
  )
  parser.add_argument('-o', '--output', metavar='<path>', type=str,
                      default="./CMakeLists.txt",
                      help='Output path. Defaults to ./CMakeLists.txt')
  parser.add_argument('-D', '--define', metavar='<VAR=value>', type=str, nargs=1,
                      action='append', default=[],
                      help='Compiler define to add (repeatable).')
  parser.add_argument('-I', '--include', metavar='<path>', type=str, nargs=1,
                      action='append', default=[],
                      help='Raw path to add as an include directory (repatable).')
  parser.add_argument('-S', '--system-include', metavar='<path>', type=str, nargs=1,
                      action='append', default=[],
                      help='Raw path to add as a system include directory (repatable).')
  parser.add_argument('-x', '--exclude', metavar='<path>', type=str, nargs=1,
                      action='append', default=[],
                      help='Path to exclude (repatable). ' +
                           'These are relative to the search root and do ' +
                           'not resolve relative path sequences.')
  parser.add_argument('-X', '--exclude-at', metavar='<path>', type=str, nargs=1,
                      action='append', default=[],
                      help='Directory path to exclude direct file ' +
                            'descendants of (e.g. "-X .", repatable). ' +
                           'These are relative to the search root and do ' +
                           'not resolve relative path sequences.')
  parser.add_argument('-!', '--filter', metavar='<segment>', type=str, nargs=1,
                      action='append', default=[],
                      help='Path segments to filter (repatable). ' +
                           'These are used to exclude any path containing a ' +
                           'matching segment (e.g. `-! test` will exlude ' +
                           '`foo/bar/test/**`).')
  parser.add_argument('-R', '--remove', metavar='<path>', type=str, nargs=1,
                      action='append', default=[],
                      help='Raw path to remove from include directory, system ' +
                           'include directory, and executable file lists ' +
                           '(repatable). To select the lists to remove from, ' +
                           'prefix with "[i][s][e]:"')
  parser.add_argument('-i', '--header-types', metavar='<types,list>', type=str,
                      nargs=1, action='append', default=[],
                      help='Comma-delimited list of header file extensions ' +
                           'to search for. This overrides the defaults.')
  parser.add_argument('-s', '--source-types', metavar='<types,list>', type=str,
                      nargs=1, action='append', default=[],
                      help='Comma-delimited list of source file extensions ' +
                           'to search for. This overrides the defaults.')
  parser.add_argument('-+', '--cpp-headers', action='store_true',
                      help='Attempt to search for extensionless C++ headers.' +
                            ' May result in non-source files being pulled ' +
                            'in, so consider using -X if issues arise.')
  parser.add_argument('-z', '--filter-cmake', action='store_true',
                      help='Shortcut for filtering out typical cmake paths ' +
                           '(CMakeFiles, cmake).')
  parser.add_argument('-d', '--debug', action='store_true',
                      help='Debug output.')
  parser.add_argument('-b', '--base-dir', metavar='<path>', type=str,
                      help='Base directory of provided search roots.')
  parser.add_argument('-C', '--config', metavar='<path>', type=str, nargs=1,
                      action='append', default=[],
                      help='Path to a config file to load additional options ' +
                           'from. Options are specified in CLI argument form ' +
                           'and multiple sets of options may be specified ' +
                           'across multiple lines. Lines starting with "#"' +
                           'are ignored.')
  parser.add_argument('search_roots', metavar='<root>', nargs='+', type=str,
                      help='Directory to search. If multiple are supplied, ' +
                           '-b must also be set', default=[])
  args = None

  _pre_args = parser.parse_args()
  _pre_args.config = [x[0] for x in _pre_args.config]
  sub_args = []
  configs = []
  last_config_index = None
  if len(_pre_args.config) > 0:
    for i in range(len(sys.argv)):
      if sys.argv[i] == "-C" or sys.argv[i] == "--config":
        last_config_index = i + 2
      elif sys.argv[i].startswith("--config="):
        last_config_index = i + 1
    for config_path in _pre_args.config:
      lines = open(config_path, 'r').read().split("\n")
      lines = [line for line in lines if not line.startswith("#") and line.strip() != ""]
      config = " ".join(lines)
      configs += shlex.split(config)

    synth_argv = sys.argv[:last_config_index] + configs + sys.argv[last_config_index:]

    if _pre_args.debug:
      print(repr(synth_argv[1:]))

    args = parser.parse_args(synth_argv[1:])
  else:
    args = _pre_args

  if len(args.search_roots) > 1:
    if args.base_dir == None:
      parser.error('-b must be supplied when passing multiple search roots.')

  args.search_roots = [sr[:-1] if (sr.endswith('/') or sr.endswith('\\'))
                               else sr
                       for sr in args.search_roots]

  if args.base_dir:
    if args.base_dir.endswith('/') or args.base_dir.endswith('\\'):
      args.base_dir = args.base_dir[:-1]

  args.include = [x[0].encode() for x in args.include]
  args.system_include = [x[0].encode() for x in args.system_include]
  args.remove = [x[0].encode() for x in args.remove]
  args.include_remove = set([])
  args.system_include_remove = set([])
  args.executable_remove = set([])
  remove_prefix_matcher = re.compile(b'^([ise]{1,3}:)')
  for rem in args.remove:
    m = remove_prefix_matcher.match(rem)
    if m:
      g = m.groups(0)[0]
      if b'i' in g:
        args.include_remove.add(rem[len(g):])
      if b's' in g:
        args.system_include_remove.add(rem[len(g):])
      if b'e' in g:
        args.executable_remove.add(rem[len(g):])
    else:
      args.include_remove.add(rem)
      args.system_include_remove.add(rem)
      args.executable_remove.add(rem)

  return args


def is_excluded(dirpath, excludelst):
  for ex in excludelst:
    if dirpath == ex:
      return True
    elif dirpath.startswith(ex + '/'):
      return True
    elif args.debug:
      if dirpath in ex:
        print('dirpath in ex: %s in %s' % (dirpath, ex))
      elif ex in dirpath:
        print('ex in dirpath: %s in %s' % (ex, dirpath))
  return False

#def is_excludedat(dirpath, excludeatlst):
#  return dirpath in excludeatlst

def to_remove(path, remove_set):
  return path in remove_set

def is_filtered(dirname, filterlst):
  if dirname.startswith('.') and dirname != '.':
    return True
  for f in filterlst:
    if dirname.lower() == f.lower():
      return True
    #elif args.debug:
    #  if dirname in f:
    #    print('dirname in f: %s in %s' % (dirname, f))
    #  elif f in dirname:
    #    print('f in dirname: %s in %s' % (f, dirname))
  return False

def has_ext(filename, exts):
  parts = filename.split(os.extsep)
  if len(parts) == 0:
    return False
  elif len(parts) == 1 and None in exts:
    return True
  return parts[-1] in exts

def get_bytes(s, *, errors='surrogateescape'):
  b = None
  if type(s) is str:
    try:
      b = s.encode()
    except UnicodeEncodeError as e:
      b = s.encode('utf8', errors=errors)
  elif type(s) is bytes:
    b = s
  else:
    raise Exception("invalid type of s: " + str(type(s)))
  return b

def generate_excludelst(args):
  excludelst = []
  for ex in args.exclude:
    e = ex[0]
    if len(e) < 1:
      continue
    if e[-1] in [os.sep,os.altsep]:
      excludelst.append(e[:-1])
    else:
      excludelst.append(e)
  return excludelst

def generate_excludeatlst(args):
  excludeatlst = []
  for ex in args.exclude_at:
    e = ex[0]
    if len(e) < 1:
      continue
    if e[-1] in [os.sep,os.altsep]:
      excludeatlst.append(e[:-1])
    else:
      excludeatlst.append(e)
  excludeatlst = set(excludeatlst)
  return excludeatlst

def generate_filterlst(args):
  filterlst = set([f[0] for f in args.filter])
  if args.filter_cmake:
    filterlst |= set(['CMakeFiles', 'cmake', 'cmake-build-debug'])
  return filterlst

def generate_header_exts(args):
  header_exts = set(['h', 'hpp', 'hh'])
  if len(args.header_types) != 0:
    hexts = []
    for hts in args.header_types:
      hexts += hts[0].split(',')
    header_exts = set(hexts)
  if args.cpp_headers:
    header_exts.add(None)
  return header_exts

def generate_code_exts(args, header_exts):
  code_exts = set(['c', 'cc', 'cpp'])
  if len(args.source_types) != 0:
    cexts = []
    for sts in args.source_types:
      cexts += sts[0].split(',')
    code_exts = set(cexts)
  code_exts = code_exts.union(header_exts)
  return code_exts

def search(args, excludelst, excludeatlst, filterlst, header_exts, code_exts):
  srcfilelst = []
  includelst = set([])
  systemlst = set([])

  for root, dirs, files in os.walk('.', topdown=True):
    if is_excluded(root, excludelst): # or is_filtered(root, filterlst):
      dirs[:] = []
    else:
      if root == '.':
        prefix = ''
      else:
        prefix = root[2:] + os.sep
      dirs[:] = [
        d
        for d in dirs
        if not (
          is_filtered(d, filterlst) or
          is_excluded(prefix + d, excludelst)
        )
      ]

    for f in files:
      if has_ext(f, code_exts):
        if root == '.':
          srcfile = './' + f
        else:
          srcfile = canon_sep(root[2:] + os.sep + f)
        if is_excluded(os.path.dirname(srcfile), excludeatlst):
          continue
        else:
          if root == '.':
            srcfile = f

        sf = get_bytes(srcfile)
        srcfilelst.append(sf)
        if has_ext(f, header_exts):
          if root == '.':
            includelst.add(b'.')
          else:
            path = canon_sepb(get_bytes(root[2:]))
            includelst.add(path)

  #find_include_directories_from_includes(srcfilelst, includelst, systemlst)

  return [srcfilelst, includelst, systemlst]


def bytes_format(fmt, **kwargs):
  out = b'' + fmt
  for (k,v) in kwargs.items():
    out = out.replace(('{'+k+'}').encode(), v)
  return out

def find_include_directories_from_includes(srcfilelst, includelst, systemlst):
  cneedle = b'#include'
  needle = b'include'

  tab = bytes(range(256))
  d = string.whitespace.encode()
  for srcfile in srcfilelst:
    try:
      with open(srcfile, 'rb') as fd:
        contents = fd.read()
        lines = contents.split(b'\n')
        for line in lines:
          if needle not in line:
            continue
          cramped = line.translate(tab, delete=d)
          if not cramped.startswith(cneedle):
            continue
          rem = line[line.find(needle)+len(needle):].strip()
          if len(rem) == 0:
            continue
          quote = False
          system = False
          if rem[0] == b'"'[0]:
            quote = True
          elif rem[0] == b'<'[0]:
            system = True
          else:
            continue
          rem = rem[1:]
          pos = -1
          if quote:
            pos = rem.find(b'"')
          elif system:
            pos = rem.find(b'>')
          if pos == -1:
            continue
          inc = rem[:pos]
          if args.debug:
            if quote:
              raw_print(b'found #include "%s"' % inc)
            elif system:
              raw_print(b'found #include <%s>' % inc)

          lst = None
          if quote:
            lst = includelst
          elif system:
            lst = systemlst

          #if b'/' not in inc:
          if True:
            m = b'/' + inc
            found = False
            for src in srcfilelst:
              s = get_bytes(src)
              if s.endswith(m):
                found = True
                rpos = s.find(m)
                s = s[:rpos]
                if args.debug:
                  if quote:
                    raw_print(b'adding include of %s for #include "%s"'
                        % (s, inc))
                  if system:
                    raw_print(b'adding system include of %s for #include <%s>'
                        % (s, inc))
                lst.add(s)
            if not found and args.debug:
              if inc not in srcfilelst:
                raw_print(b'failed to match %s' % (inc))
            #continue

          incpath = b'/'.join(inc.split(b'/')[:-1])
          npaths = set([])

          for path in lst:
            #path = path.encode()
            if path.endswith(b'/' + incpath):
              npath = path[:len(path)-len(b'/' + incpath)]
              npaths.add(npath)
          for npath in npaths:
            if args.debug:
              if quote:
                raw_print(b'adding include of %s for #include "%s"'
                      % (npath, inc))
              elif system:
                raw_print(b'adding system include of %s for #include <%s>'
                      % (npath, inc))
            lst.add(npath)
    except Exception as e:
      sys.stderr.write("{}: {}\n".format(srcfile, e))
      raise e

def escape_bstring(path):
  r = b""
  for i in range(len(path)):
    b = path[i:i+1]
    if b in [b'"', b"\\", b"$"]:
      r += b"\\"
    r += b
  return r

def escape_string(path):
  if type(path) == bytes:
    return escape_bstring(path)

  r = ""
  for c in path:
    if c in ['"', "\\", "$"]:
      r += "\\"
    r += c
  return r

def canon_sep(path):
  if os.sep != "/":
    return path.replace(os.sep, '/')
  else:
    return path

def canon_sepb(path):
  if os.sep != "/":
    return path.replace(os.sep.encode(), b'/')
  else:
    return path

def generate_output(args, cwd, systemlst, includelst, srcfilelst):
  proj_path = ""
  if args.base_dir:
    proj_path = args.base_dir
  else:
    proj_path = args.search_roots[0]

  projname = b'"' + escape_string(get_bytes(proj_path.split('/')[-1].split('\\')[-1], errors="ignore")) + b'"'
  systemlst = [b'"' + escape_string(inc) + b'"' for inc in systemlst]
  systemlst.sort()
  systemstr = b'\n  '.join(systemlst)
  includelst = [b'"' + escape_string(inc) + b'"' for inc in includelst]
  includelst.sort()
  includestr = b'\n  '.join(includelst)
  srcfilelst = [b'"' + escape_string(src) + b'"' for src in srcfilelst]
  srcfilelst.sort()
  srcfilestr = b'\n  '.join(srcfilelst)

  compiler_defs = ''
  if len(args.define) > 0:
    compiler_defs
  for d in args.define:
    compiler_defs = compiler_defs_template.format(vals='\n  '.join([('"' + escape_string(pairl[0]) + '"') for pairl in args.define]).strip())

  format_args = {
    'project_name': projname,
    'compiler_defs': compiler_defs.encode(),
    'system_includes': systemstr,
    'includes': includestr,
    'src_files': srcfilestr,
  }

  #output = cmake_template % (projname, systemstr, includestr,
  #                         projname, srcfilestr)
  output = bytes_format(cmake_template, **format_args)

  if args.output == '-':
    sys.stdout.buffer.write(output)
  else:
    try:
      os.chdir(cwd)
    except OSError as e:
      sys.stderr.write("{}\n".format(e))
      sys.exit(1)
    with open(args.output, 'wb') as fd:
      fd.write(output)

def main():
  global args
  args = parse_args()

  if args.debug:
    print(repr(args))

  excludelst = generate_excludelst(args)
  excludeatlst = generate_excludeatlst(args)
  filterlst = generate_filterlst(args)
  header_exts = generate_header_exts(args)
  code_exts = generate_code_exts(args, header_exts)

  full_srcfilelst = []
  full_includelst = set(args.include)
  full_systemlst = set(args.system_include)

  cwd = os.getcwd()
  nwd = None
  base_dir = b""

  if args.base_dir:
    base_dir = get_bytes(args.base_dir)
    try:
      os.chdir(args.base_dir)
      nwd = os.getcwd()
    except OSError as e:
      sys.stderr.write("{}\n".format(e))
      sys.exit(1)

  for search_root in args.search_roots:
    try:
      os.chdir(search_root)
    except OSError as e:
      sys.stderr.write("{}\n".format(e))
      sys.exit(1)

    srcfilelst, includelst, systemlst = search(args, excludelst, excludeatlst,
                                               filterlst, header_exts,
                                               code_exts)
    prefix = b''
    if args.base_dir:
      if search_root != '.':
        prefix = get_bytes(search_root) + b'/'

    full_srcfilelst += [prefix + sf for sf in srcfilelst]
    full_includelst |= {prefix + i for i in includelst}
    full_systemlst |= {prefix + s for s in systemlst}

    try:
      os.chdir(nwd if nwd else cwd)
    except OSError as e:
      sys.stderr.write("{}\n".format(e))
      sys.exit(1)

  find_include_directories_from_includes(full_srcfilelst, full_includelst, full_systemlst)

  full_srcfilelst = [x for x in set(full_srcfilelst) if x not in args.executable_remove]
  full_includelst = set([x for x in full_includelst if x not in args.include_remove])
  full_systemlst = set([x for x in full_systemlst if x not in args.system_include_remove])

  generate_output(args, cwd, full_systemlst, full_includelst, full_srcfilelst)

if __name__ == '__main__':
  main()

__all__ = ["parse_args", "main"]
